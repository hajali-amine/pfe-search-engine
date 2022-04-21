import neo4j
from typing import List, NoReturn

class Neo4jOOP:
    def __init__(self, uri: str, user: str, password: str) -> None:
        self.driver = neo4j.GraphDatabase.driver(uri, auth=(user, password))

    def close(self) -> None:
        self.driver.close()

    def add_node(self, type, **kwargs): # (*list) (a, b, c, d)
        query = [f"CREATE (:{type} {{"]
        for key, value in kwargs.items():
            query.append(key + ":" + f"'{value}'")
            query.append(",")
        query.pop()
        query.append("})")
        self.driver.session().run("".join(query))
    
    def match_node(self, type, **kwargs):
        query = [f"Match (a:{type} {{"]
        for key, value in kwargs.items():
            query.append(key + ":" + f"'{value}'")
            query.append(",")
        query.pop()
        query.append("}) RETURN a AS a")
        return self.driver.session().run("".join(query)).values()


neo = Neo4jOOP("bolt://localhost:7687",  user="neo4j", password="pwd")
neo.add_node("person", name="hi", age="test")
print(neo.match_node("person", name="hi", age="test"))
    