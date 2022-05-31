import neo4j
from orm.query_builder import QueryBuilder

class Neo4jOOP:
    def __init__(self, uri: str, user: str, password: str) -> None:
        self.driver = neo4j.GraphDatabase.driver(uri, auth=(user, password))
        
    def close(self) -> None:
        self.driver.close()

    def execute_query(self, query):
        return self.driver.session().run(query).values()

    def parse_match_node(self, result):
        parsedResult = []
        for value in result:
            parsedNode = { "id": value[0]._id ,"label": list(value[0]._labels),"properties": value[0]._properties}
            parsedResult.append(parsedNode)
        return parsedResult

    def purge(self):
        query = ["Match (a) -[r] -> (c) delete a, r, c;"]
        return self.driver.session().run("".join(query)).values()

neo = Neo4jOOP("bolt://localhost:7687",  user="neo4j", password="pwd")
queryBuilder = QueryBuilder()
query = queryBuilder.create().node("a", "Person").build()
neo.execute_query(query)
# a = input()
# query = queryBuilder.match().node("a", "Person", ism="Mahdi").set("a", ism="med").set("a", age="thletha").to_return("a").build()

print(neo.execute_query(query))