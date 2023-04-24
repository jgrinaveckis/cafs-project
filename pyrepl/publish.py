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
from json import dumps
from time import sleep

from kafka.admin import KafkaAdminClient, NewTopic

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s %(levelname)-8s %(message)s',
	datefmt='%Y-%m-%d %H:%M:%S'
	)

mysql_settings = {
	'host': "mysql",
	'port': 3306, 
	'user': "ca", 
	'passwd': "ca",
} 
additional_db_settings = {
	'dbname': "ca",
	'charset': "utf8mb4"
}

COLUMNS = ('ip', 'iso_state', "iso_country", "created_at", "lat", "lon")

def create_connection():
	connectionObject   = pymysql.connect(host=mysql_settings['host'], user=mysql_settings['user'], password=mysql_settings['passwd'],
                                     db=additional_db_settings['dbname'], charset=additional_db_settings['charset'])
	return connectionObject

def insert_row(connection, data:dict):
	try:
		cursor = connection.cursor()
		query = f"""
			INSERT INTO test_leads_insert(ip, iso_state, iso_country, lat, lon, lead_created_at)
			VALUES("{data['ip']}", "{data['iso_state']}", "{data['iso_country']}", "{data['lat']}", "{data['lon']}", "{data['lead_created_at']}")
		"""
		cursor.execute(query)
	except Exception as e:
		print("Exeception occured:{}".format(e))
	finally:
		connection.close()


def create_topic():
	admin_client = KafkaAdminClient(
    bootstrap_servers="kafka:9093", 
    client_id='test'
	)
	topic_list = []
	topic_list.append(NewTopic(name="topic2", num_partitions=1, replication_factor=1))
	admin_client.create_topics(new_topics=topic_list, validate_only=False)


def build_message(binlog_event, row):
	table = {'table': str(getattr(binlog_event, 'schema', '')) + "." + str(getattr(binlog_event, 'table', ''))}
	if isinstance(binlog_event,WriteRowsEvent):
		event_data = row['values']
		event_data = {k: event_data.get(k, None) for k in COLUMNS}
		return {'event':'INSERT', 'table':table, 'data':event_data}

def send_event():
	logging.info(f"Creating Kafka producer...")

	# create_topic()
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
			logging.info(f"Table: {msg['table']} received {msg['event']} type of change")
			try:
				producer.send('topic2', value=msg)
				# insert_row(conn, msg['data'])
				producer.flush()
			except:
				sleep(1)
				producer.send('topic2', value=msg)
				# insert_row(conn, msg['data'])
				producer.flush()
	stream.close()

if __name__ == "__main__":
    send_event()