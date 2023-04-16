from kafka.consumer import KafkaConsumer
import json
import sys
import logging
from time import sleep

#--------------------------------------
#-----------ONLY FOR TESTING-----------
#--------------------------------------

logging.basicConfig(
    #filename='/tmp/snowflake_python_connector.log',
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s %(levelname)-8s %(message)s',
	datefmt='%Y-%m-%d %H:%M:%S'
	)


def main():
	print("Starting consumer", 'kafka:9092')
	consumer = KafkaConsumer(
	'topic2',
	bootstrap_servers=['kafka:9092'],
	auto_offset_reset="earliest",
	enable_auto_commit=True,
	group_id="test-grp",
	value_deserializer=lambda x: json.loads(x.decode("utf-8"))
	)

	for message in consumer:
		message = f"""
		Message received: {message.value}
		Message key: {message.key}
		Message partition: {message.partition}
		Message offset: {message.offset}
		"""
		logging.info(message)
		sleep(2)
	pass

if __name__=="__main__":
  main()