from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import (
    DeleteRowsEvent,
    UpdateRowsEvent,
    WriteRowsEvent,
)
from Kafka import KafkaProducer
import logging
import sys
from json import dumps
from time import sleep

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

	producer = KafkaProducer(
		bootstrap_servers=['localhost:9092'],
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
				producer.send('cafs-project-topic', value=msg)
			except:
				sleep(1)
				producer.send('cafs-project-topic', value=msg)
	stream.close()

if "__name__" == "__main__":
    send_event()