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
    Logger.info(msg="Logged to Neo4j")
except Exception as e:
    Logger.error(msg="Failed to log in to Neo4J", error=str(e))
    raise

try:
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(os.getenv("RABBITMQ_URL"))
    )
    channel = connection.channel()
    channel.queue_declare(queue="loader")
    Logger.info(msg="Connected to RabbitMQ")
except Exception as e:
    Logger.error(msg="Failed to connect to RabbitMQ", error=str(e))
    raise
    
def callback(ch, method, properties, body):
    try:
        job = Job.Job()
        job.ParseFromString(body)
        msg = MessageToDict(job)
        Logger.info(msg="Message unmarshalled", message=msg)
    except Exception as e:
        Logger.error(msg="Unmarshalling message failed", error=str(e), message=body)
        raise
    
    try:
        DataLoader.load(neo=neo, data=msg)
        Logger.info(msg="Data loaded", data=msg)
    except Exception as e:
        Logger.error(msg="Data failed to load", error=str(e), data=msg)
        raise

channel.basic_consume(queue="loader", auto_ack=True, on_message_callback=callback)

Logger.info(msg="Waiting for messages")
channel.start_consuming()
