import os

import pika
from dataloader.data_loader import DataLoader
from dataloader.logger import logger
from dataloader.types.job_pb2 import Job
from google.protobuf.json_format import MessageToDict
from graph_driver.neo4j_oop import Neo4jOOP

try:
    neo = Neo4jOOP(
        os.environ["NEO4J_URL"],
        user=os.environ["NEO4J_USERNAME"],
        password=os.environ["NEO4J_PASSWORD"],
    )
    logger.info("Logged to Neo4j")
except Exception as e:
    logger.error("Failed to log in to Neo4J", error=str(e))
    raise

try:
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(os.getenv("RABBITMQ_URL"))
    )
    channel = connection.channel()
    channel.queue_declare(queue="loader")
    logger.info("Connected to RabbitMQ")
except Exception as e:
    logger.error("Failed to connect to RabbitMQ", error=str(e))
    raise


def callback(ch, method, properties, body):
    try:
        job = Job()
        job.ParseFromString(body)
        msg = MessageToDict(job)
        logger.info("Message unmarshalled", message=msg)
    except Exception as e:
        logger.error("Unmarshalling message failed", error=str(e), message=body)
        raise

    try:
        DataLoader.load(neo=neo, data=msg)
        logger.info("Data loaded", data=msg)
    except Exception as e:
        logger.error("Data failed to load", error=str(e), data=msg)
        raise


channel.basic_consume(queue="loader", auto_ack=True, on_message_callback=callback)

logger.info("Waiting for messages")
channel.start_consuming()
