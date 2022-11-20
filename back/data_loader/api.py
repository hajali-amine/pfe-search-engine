import os
from urllib import request
from flask import Flask, request


from data_loader.data_loader import DataLoader
from graph_driver.neo4j_oop import Neo4jOOP


app = Flask(__name__)
neo = Neo4jOOP(
    os.environ["NEO4J_URL"],
    user=os.environ["NEO4J_USERNAME"],
    password=os.environ["NEO4J_PASSWORD"],
)


@app.route("/api", methods=["POST"])
def get_data_to_insert():
    data = request.get_json()
    print(data)
    DataLoader.load(neo=neo, data=data)
    return "jawwek behi"
