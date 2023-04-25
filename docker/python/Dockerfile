FROM python:3.11-bullseye

WORKDIR /pyrepl/
RUN chmod -R 777 /pyrepl/

RUN pip --version
RUN pip install cryptography mysql-replication kafka-python websockets aiokafka pymysql python-dotenv