import os
import uuid

from datareader.data_reader import DataReader
from datareader.logger import logging
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from graph_driver.neo4j_oop import Neo4jOOP
from opentelemetry import trace
from prometheus_client import Counter
from prometheus_flask_exporter import PrometheusMetrics


SEARCH_COUNTER = Counter("nb_searches", "Request counter")
tracer = trace.get_tracer(__name__)

app = Flask(__name__)
CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

neo = Neo4jOOP(
    os.environ["NEO4J_URL"],
    user=os.environ["NEO4J_USERNAME"],
    password=os.environ["NEO4J_PASSWORD"],
)

metrics = PrometheusMetrics(app=app, path="/metrics")


@app.route("/api/<filter>/<search>", methods=["GET"])
@cross_origin()
@logging(function_name="data_reader.api.data")
def data(filter, search):
    SEARCH_COUNTER.inc()
    with tracer.start_as_current_span("data_reader") as span:
        span.set_attribute("request_id", uuid.uuid1())
        result = (
            DataReader.search_by_filter(neo=neo, filter=filter, search=search)
            if filter != "skill"
            else DataReader.search_by_skill(neo=neo, search=search)
        )
        return jsonify(result)
