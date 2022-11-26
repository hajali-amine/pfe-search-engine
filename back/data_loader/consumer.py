from logging import Logger
import os

import data_loader.types.job_pb2 as Job
import pika
from google.protobuf.json_format import MessageToDict
from graph_driver.neo4j_oop import Neo4jOOP
from data_loader.data_loader import DataLoader

try:
    neo = Neo4jOOP(
        os.environ["NEO4J_URL"],
        user=os.environ["NEO4J_USERNAME"],
        password=os.environ["NEO4J_PASSWORD"],
    )
    Logger.info("Logged to Neo4j")
except Exception as e:
    Logger.error("Failed to log in to Neo4J", msg=str(e))
    raise

try:
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(os.getenv("RABBITMQ_URL"))
    )
    channel = connection.channel()
    channel.queue_declare(queue="loader")
    Logger.info("Connected to RabbitMQ")
except Exception as e:
    Logger.error("Failed to connect to RabbitMQ", msg=str(e))
    raise
    
def callback(ch, method, properties, body):
    try:
        job = Job.Job()
        job.ParseFromString(body)
        msg = MessageToDict(job)
        Logger.info("Message unmarshalled", message=msg)
    except Exception as e:
        Logger.error("Unmarshalling message failed", message=str(e), msg=body)
        raise
    
    try:
        DataLoader.load(neo=neo, data=msg)
        Logger.info("Data loaded", data=msg)
    except Exception as e:
        Logger.error("Data failed to load", message=str(e), data=msg)
        raise

channel.basic_consume(queue="loader", auto_ack=True, on_message_callback=callback)

Logger.info("Waiting for messages")
channel.start_consuming()
