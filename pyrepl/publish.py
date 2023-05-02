from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import (
    DeleteRowsEvent,
    UpdateRowsEvent,
    WriteRowsEvent,
)
from kafka import KafkaProducer, KafkaClient
import logging
import sys
import pymysql
import os
import datetime
from json import dumps
from time import sleep
from dotenv import load_dotenv
from ipapi import getIpJson

# Loading .env file for conn details
load_dotenv()

from kafka.admin import KafkaAdminClient, NewTopic

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s %(levelname)-8s %(message)s',
	datefmt='%Y-%m-%d %H:%M:%S'
	)

mysql_settings = {
	'host': os.getenv('DB_HOST'),
	'port': int(os.getenv('DB_PORT')), 
	'user': os.getenv('DB_USERNAME'), 
	'passwd': os.getenv('DB_PASSWORD'),
} 
additional_db_settings = {
	'dbname': "ca",
	'charset': "utf8mb4"
}

COLUMNS = ('ip', "lead_created_at")

def create_connection():
	connectionObject   = pymysql.connect(host=mysql_settings['host'], user=mysql_settings['user'], password=mysql_settings['passwd'],
                                     db=additional_db_settings['dbname'], charset=additional_db_settings['charset'])
	return connectionObject

def insert_row(connection, data:dict):
	try:
		ts = datetime.datetime.now()
		timestamp = ts.strftime('%Y-%m-%d %H:%M:%S')
		cursor = connection.cursor()
		query = "INSERT INTO `leads` (`ip`, `iso_state`, `iso_country`, `country_name`, `city`, `lat`, `lon`, `lead_created_at`, `table`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
		cursor.execute(query, (data["ip"], data["region"], data["country_code"], data["country_name"], data["city"], data["lat"], data["lon"], timestamp, data["table"]))
		connection.commit()
	except Exception as e:
		logging.info("Exeception occured: {}".format(e))


def create_topic():
	admin_client = KafkaAdminClient(
		bootstrap_servers="kafka:9093", 
		client_id='test'
	)
	topic_list = []
	topic_list.append(NewTopic(name="topic2", num_partitions=1, replication_factor=1))
	admin_client.create_topics(new_topics=topic_list, validate_only=False)

def build_message(binlog_event, row):
	schema_name = str(getattr(binlog_event, 'schema', ''))
	tbl_name = str(getattr(binlog_event, 'table', ''))
	table = {'table': schema_name + "." + tbl_name}
	if isinstance(binlog_event,WriteRowsEvent) and 'test_leads' == tbl_name:
		event_data = row['values']
		event_data = {k: event_data.get(k, None) for k in COLUMNS}
		return {'event':'INSERT', 'table':table, 'data':event_data}

def send_event():
	logging.info(f"Creating Kafka producer...")

	conn = create_connection()

	producer = KafkaProducer(
		bootstrap_servers=['kafka:9092'],
		value_serializer=lambda x:dumps(x, default=str).encode('utf-8')
		)

	logging.info(f"Connecting to Mysql at host {mysql_settings['host']}...")
	try:
		stream = BinLogStreamReader(
			connection_settings = mysql_settings,
			server_id=1,
			resume_stream=True,
			blocking=True,
			only_events=[DeleteRowsEvent, WriteRowsEvent, UpdateRowsEvent]
		)
		logging.info("connected. Listening for changes...")
	except Exception as e:
		logging.error(e)

	for event in stream:
		for e_row in event.rows:
			msg = build_message(event, e_row)
			if msg:
				logging.info(f"Table: {msg['table']} received {msg['event']} type of change")
				encriched_data = getIpJson(msg['data']['ip'])
				if encriched_data:
					encriched_data["table"] = msg["table"]["table"]
					try:
						producer.send('topic2', value=encriched_data)
						insert_row(conn, encriched_data)
						producer.flush()
					except:
						sleep(1)
						producer.send('topic2', value=encriched_data)
						insert_row(conn, encriched_data)
						producer.flush()

	conn.close()
	stream.close()

if __name__ == "__main__":
    send_event()