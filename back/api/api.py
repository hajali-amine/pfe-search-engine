import os
from urllib import request
import dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin


from api.data_loader import DataLoader
from api.data_reader import DataReader
from graph_driver.neo4j_oop import Neo4jOOP

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

neo = Neo4jOOP(os.environ["NEO4J_URL"],  user=os.environ["NEO4J_USERNAME"], password=os.environ["NEO4J_PASSWORD"])

@app.route("/api", methods=["POST"])
@cross_origin()
def get_data_to_insert():
    data = request.get_json()
    print(data)
    DataLoader.load(neo=neo, data=data)
    return "jawwek behi"
    
@app.route("/api/<filter>/<search>", methods=["GET"])
@cross_origin()
def data(filter, search):
    result = DataReader.search_by_filter(neo=neo, filter=filter, search=search) if filter != "skill" else DataReader.search_by_skill(neo=neo, search=search)
    return jsonify(result)

