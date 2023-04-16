from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import (
    DeleteRowsEvent,
    UpdateRowsEvent,
    WriteRowsEvent,
)
from kafka import KafkaProducer, KafkaClient
import logging
import sys
from json import dumps
from time import sleep

from kafka.admin import KafkaAdminClient, NewTopic



logging.basicConfig(
    #filename='/tmp/snowflake_python_connector.log',
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s %(levelname)-8s %(message)s',
	datefmt='%Y-%m-%d %H:%M:%S'
	)

mysql_settings = {'host': "mysql",
					'port': 3306, 
					'user': "ca", 
					'passwd': "ca"
				}


def create_topic():
	admin_client = KafkaAdminClient(
    bootstrap_servers="kafka:9093", 
    client_id='test'
	)
	topic_list = []
	topic_list.append(NewTopic(name="example_topic", num_partitions=1, replication_factor=1))
	admin_client.create_topics(new_topics=topic_list, validate_only=False)


def build_message(binlog_event, row):
	table = {'table': str(getattr(binlog_event, 'schema', '')) + "." + str(getattr(binlog_event, 'table', ''))}
	if isinstance(binlog_event,WriteRowsEvent):
		return {'event':'INSERT', 'table':table, 'data':row['values']}
	elif isinstance(binlog_event,UpdateRowsEvent):
		return {'event':'UPDATE', 'table':table, 'data':row['after_values']}
	elif isinstance(binlog_event,DeleteRowsEvent):
		return {'event':'DELETE', 'table':table, 'data':row['values']}

def send_event():
	logging.info(f"Creating Kafka producer...")

	# create_topic()

	producer = KafkaProducer(
		bootstrap_servers=['kafka:9092'],
		value_serializer=lambda x:dumps(x).encode('utf-8')
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
			logging.info(f"Table: {msg['table']['table']} received {msg['event']} type of change")
			logging.info(msg['data'])
			try:
				r = producer.send('topic2', value=msg)
				producer.flush()
			except:
				sleep(1)
				producer.send('topic2', value=msg)
				producer.flush()
	stream.close()

if __name__ == "__main__":
    send_event()