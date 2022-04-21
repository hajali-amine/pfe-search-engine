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

    def find_one_by_id(self, type, id):
        query = [f"Match (a:{type}) WHERE ID(a) = {id} RETURN a AS a"]
        result = self.driver.session().run("".join(query)).values()
        return self.parse_match_node(result)[0]

    def delete_one_by_id(self, type , id):
        query = [f"Match (a:{type}) WHERE ID(a) = {id} DELETE a"]   
        result = self.driver.session().run("".join(query)).values()
        return result
    
    def delete_all_nodes(self, type, **kwargs):
        query = [f"Match (a:{type} {{"]
        for key, value in kwargs.items():
            query.append(key + ":" + f"'{value}'")
            query.append(",")
        query.pop()
        query.append("}) DELETE a")
        return self.driver.session().run("".join(query)).values()
    def purge(self):
        query = ["Match (a) -[r] -> (c) delete a, r, c;"]
        return self.driver.session().run("".join(query)).values()
    def count_node(self, type, **kwargs):
        query = [f"Match (a:{type} {{"]
        for key, value in kwargs.items():
                query.append(key + ":" + f"'{value}'")
                query.append(",")
        query.pop()
        query.append("}) RETURN count(a) AS nodes ")
        return self.driver.session().run("".join(query)).single()["nodes"]
    def get_node_id(self, type, **kwargs):
       return  self.match_node(type, **kwargs)[0]["id"]
    def update_node_by_id(self, type, id, **kwargs):
        query = [f"Match (a:{type}) WHERE ID(a) = {id} SET "] 
        for key, value in kwargs.items():
            query.append("a."+key + "=" + f"'{value}'")
            query.append(",")
        query.pop()
        query.append(" RETURN a")
        return self.driver.session().run("".join(query)).values()
    def add_relationship(self, types, matchNode1, matchNode2, relationName, **kwargs):
        query = [f"Match (fnode:{types[0]} {{"]
        for matchItem in matchNode1:
                query.append(matchItem['key'] + ":" + f"'{matchItem['value']}'")
                query.append(",")
        query.pop()
        query.append("})")
        query.append(f" , (snode:{types[1]} {{")
        print("query here", query)
        for matchItem in matchNode2:
                query.append(matchItem['key'] + ":" + f"'{matchItem['value']}'")
                query.append(",")
        query.pop()
        query.append("})")
        query.append(f" CREATE (fnode) - [:{relationName}] -> (snode)")
        self.driver.session().run("".join(query))
neo = Neo4jOOP("bolt://localhost:7687",  user="neo4j", password="pwd")
# neo.add_node("Project", projectName="Matching App" , length="3 Months")
# neo.add_node("Location", country="France")
# print(neo.add_relationship(["Project", "Location"], [{"key": "projectName", "value":"Matching App"}, {"key": "length", "value":"3 Months"}], [{"key": "country", "value":"France"}] , "IN"))
franceNode=neo.get_node_id("Location",country="France")
print( neo.update_node_by_id("Location", franceNode, town="Paris", postalCode="7500"))