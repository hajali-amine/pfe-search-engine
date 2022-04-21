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
        result =  self.driver.session().run("".join(query)).values()
        return self.parse_match_node(result)

    def parse_match_node(self, result):
        parsedResult = []
        for value in result:
            parsedNode = { "id": value[0]._id ,"label": list(value[0]._labels),"properties": value[0]._properties}
            parsedResult.append(parsedNode)
        return parsedResult

    def find_by_id(self, type, id):
        query = [f"Match (a:{type}) WHERE ID(a) = {id} RETURN a AS a"]
        result = self.driver.session().run("".join(query)).values()
        return self.parse_match_node(result)[0]

    def delete_one_by_id(self, type , id):
        query = [f"Match (a:{type}) WHERE ID(a) = {id} DELETE a"]   
        result = self.driver.session().run("".join(query)).values()
        return result
    
    def delete_all(self, type, **kwargs):
        query = [f"Match (a:{type} {{"]
        for key, value in kwargs.items():
            query.append(key + ":" + f"'{value}'")
            query.append(",")
        query.pop()
        query.append("}) DELETE a")
        return self.driver.session().run("".join(query)).values()
    def count_node(self, type, **kwargs):
        query = [f"Match (a:{type} {{"]
        for key, value in kwargs.items():
                query.append(key + ":" + f"'{value}'")
                query.append(",")
        query.pop()
        query.append("}) RETURN count(a) AS nodes ")
        return self.driver.session().run("".join(query)).single()["nodes"]

neo = Neo4jOOP("bolt://localhost:7687",  user="neo4j", password="pwd")
print(neo.delete_all("person", name="hi", age="test"))

    