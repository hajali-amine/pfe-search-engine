import neo4j


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
            parsedNode = {
                "id": value[0]._id,
                "label": list(value[0]._labels),
                "properties": value[0]._properties,
            }
            parsedResult.append(parsedNode)
        return parsedResult

    def purge(self):
        query = ["Match (a) -[r] -> (c) delete a, r, c;"]
        return self.driver.session().run("".join(query)).values()
