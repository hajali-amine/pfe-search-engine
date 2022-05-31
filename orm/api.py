from crypt import methods
import json
from urllib import request
from flask import Flask, request, jsonify

from orm.data_loader import DataLoader
from orm.data_reader import DataReader
from orm.neo4j_oop import Neo4jOOP

app = Flask(__name__)

neo = Neo4jOOP("bolt://localhost:7687",  user="neo4j", password="pwd")

@app.route("/api", methods=["POST"])
def get_data_to_insert():
    data = request.get_json()
    DataLoader.load(neo, data)
    return "jawwek behi"
    
@app.route("/api/<filter>/<search>", methods=["GET"])
def data(filter, search):
    result = DataReader.search_by_filter(neo,filter, search) if filter != "skill" else DataReader.search_by_skill(neo, search)
    return jsonify(result)

