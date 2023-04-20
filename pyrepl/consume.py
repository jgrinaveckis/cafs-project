import json
import sys
import asyncio
import websockets
import aiokafka
import logging

WEBSOCKET_PORT=3003
CLIENTS=set()
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s %(levelname)-8s %(message)s',
	datefmt='%Y-%m-%d %H:%M:%S'
	)

async def consumer_handler(websocket):
	CLIENTS.add(websocket)
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

	except Exception as e:
		logging.exception(exc_info=e)
	try:
		async for msg in consumer:
			for ws in CLIENTS.copy():
				try:
					await ws.send(json.dumps(msg.value))
					logging.info(msg.value)
				except websockets.ConnectionClosed:
					CLIENTS.remove(ws)
	finally:
		await consumer.stop()



async def send_msg(websocket):
		
	handler = asyncio.ensure_future(consumer_handler(websocket))

	done, pending = await asyncio.wait(
		[handler],
		return_when=asyncio.FIRST_COMPLETED
	)

	for task in pending:
		task.cancel()

while True:
	start_server = websockets.serve(send_msg, "0.0.0.0", WEBSOCKET_PORT)

	logging.info(f"Started Websocket on port {WEBSOCKET_PORT}")

	asyncio.get_event_loop().run_until_complete(start_server)
	asyncio.get_event_loop().run_forever()