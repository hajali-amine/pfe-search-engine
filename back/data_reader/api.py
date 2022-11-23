import os

from api.data_reader import DataReader
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from graph_driver.neo4j_oop import Neo4jOOP

app = Flask(__name__)
CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

neo = Neo4jOOP(
    os.environ["NEO4J_URL"],
    user=os.environ["NEO4J_USERNAME"],
    password=os.environ["NEO4J_PASSWORD"],
)


@app.route("/api/<filter>/<search>", methods=["GET"])
@cross_origin()
def data(filter, search):
    result = (
        DataReader.search_by_filter(neo=neo, filter=filter, search=search)
        if filter != "skill"
        else DataReader.search_by_skill(neo=neo, search=search)
    )
    return jsonify(result)
