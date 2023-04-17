from kafka.consumer import KafkaConsumer
import json
import sys
import asyncio
import websockets
import aiokafka
import logging
from time import sleep

WEBSOCKET_PORT=3003

logging.basicConfig(
    #filename='/tmp/snowflake_python_connector.log',
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s %(levelname)-8s %(message)s',
	datefmt='%Y-%m-%d %H:%M:%S'
	)

async def consumer_handler(websocket):
	try:
		print("Starting consumer", 'kafka:9092')
		consumer = aiokafka.AIOKafkaConsumer(
		'topic2',
		loop=asyncio.get_event_loop(),
		bootstrap_servers=['kafka:9092'],
		auto_offset_reset="earliest",
		enable_auto_commit=True,
		group_id="test-grp",
		consumer_timeout_ms=1000000,
		max_poll_interval_ms=2147483647,
		value_deserializer=lambda x: json.loads(x.decode("utf-8"))
		)
		logging.info("Consumer created")

		await consumer.start()
		try:
			async for msg in consumer:
				await websocket.send(json.dumps(msg.value))
				logging.info(msg.value)
		finally:
			await consumer.stop()
	except Exception as e:
		logging.exception(exc_info=e)

async def send_msg(websocket):
	consumer = asyncio.ensure_future(
		consumer_handler(websocket)
	)

	done, pending = await asyncio.wait(
		[consumer],
		return_when=asyncio.FIRST_COMPLETED
	)

	for task in pending:
		task.cancel()

while True:
	start_server = websockets.serve(send_msg, "0.0.0.0", WEBSOCKET_PORT)

	logging.info(f"Started Websocket on port {WEBSOCKET_PORT}")

	asyncio.get_event_loop().run_until_complete(start_server)
	asyncio.get_event_loop().run_forever()