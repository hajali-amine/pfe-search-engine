class QueryBuilder:
    def __init__(self, queryType) -> None:
        self.queryType = queryType
        self.query = [queryType, " "]
        self.nodeNames = []
        self.relationList = []  
    def match_first_node(self, nodeName, type, **kwargs):
        self.nodeNames.append(nodeName)
        self.query.append(self.build_node(nodeName, type, **kwargs))
    def add_node(self, nodeName, type, **kwargs):
        self.nodeNames.append(nodeName)
        if len(self.relationList) == 0 :
            self.query.append(", ")
        self.query.append(self.build_node(nodeName, type, **kwargs))
    def build_node(self, nodeName, type, **kwargs):
        node = [f"({nodeName}:{type} "]
        print (len(kwargs.items()))
        if len(kwargs.items()) > 0 :
            node.append("{")
            for key, value in kwargs.items():
                node.append(key + ":" + f"'{value}'")
                node.append(",")
            node.pop()
            node.append("})")
        else: node.append(")")
        return("".join(node))
    def return_query(self):
        return "".join(self.query)
    def return_all_nodes_relations(self):
        returnedNodes = [" RETURN "]
        for nodename in self.nodeNames:
            returnedNodes.append(nodename)
            returnedNodes.append(",")
        for relation in self.relationList:
            returnedNodes.append(relation)
            returnedNodes.append(",")
        returnedNodes.pop()
        self.query.append("".join(returnedNodes))
    def add_relationship(self,relationName,  relationType,):
        self.relationList.append(relationName)
        self.query.append(f" - [{relationName}:{relationType}] -> ")