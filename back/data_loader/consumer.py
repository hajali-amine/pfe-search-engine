import os

import loader.types.job_pb2 as Job
import pika
from google.protobuf.json_format import MessageToDict
from graph_driver.neo4j_oop import Neo4jOOP
from loader.data_loader import DataLoader

neo = Neo4jOOP(
    os.environ["NEO4J_URL"],
    user=os.environ["NEO4J_USERNAME"],
    password=os.environ["NEO4J_PASSWORD"],
)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(os.getenv("RABBITMQ_URL"))
)
channel = connection.channel()
channel.queue_declare(queue="loader")


def callback(ch, method, properties, body):
    job = Job.Job()
    job.ParseFromString(body)
    msg = MessageToDict(job)
    print("[x] Loading %r" % msg)
    DataLoader.load(neo=neo, data=msg)
    print("Data loaded")


channel.basic_consume(queue="loader", auto_ack=True, on_message_callback=callback)

print(" [*] Waiting for messages.")
channel.start_consuming()
