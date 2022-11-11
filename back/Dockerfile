FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY graph_driver graph_driver

COPY graph_query_builder graph_query_builder

COPY api api

ENV FLASK_APP=api.api

ENV NEO4J_USERNAME=neo4j

ENV NEO4J_PASSWORD=pwd

ENV NEO4J_URL=bolt://localhost:7687

EXPOSE 5000

CMD flask run --host=0.0.0.0
