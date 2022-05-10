from directions_enum import Direction


class QueryBuilder:
    def __init__(self) -> None:
        self.query = []

    def create(self):
        self.query.append("CREATE ")
        return self
    
    def match(self):
        self.query.append("MATCH ")
        return self
    
    def node(self, name, type, **kwargs):
        self.query.append(f"({name}:{type} {{")
        for key, value in kwargs.items():
            self.query.append(key + ":" + f"'{value}'")
            self.query.append(",")
        self.query.pop()
        self.query.append("}) " if kwargs else ") ")
        return self

    def relation(self, name, type, direction, **kwargs):
        if direction == Direction.LEFT:
            self.query.append("<")
        self.query.append(f"-[{name}:{type} {{")
        for key, value in kwargs.items():
            self.query.append(key + ":" + f"'{value}'")
            self.query.append(",")
        self.query.pop()
        self.query.append("}]-" if kwargs else "]-")
        if direction == Direction.RIGHT:
            self.query.append("> ")
        elif direction == Direction.NONE:
            self.query.append(" ")
        return self
    
    def set(self, who, **kwargs):
        self.query.append("SET ")
        for key, value in kwargs.items():
            self.query.append(who + "." + key + "=" + f"'{value}'")
            self.query.append(",")
        self.query.pop()
        self.query.append(" ")
        return self
    
    def to_return(self, *args):
        self.query.append("RETURN ")
        for element in args:
            self.query.append(str(element))
            self.query.append(", ")
        self.query.pop()
        self.query.append(" ")
        return self
    
    def where(self, *args):
        self.query.append("WHERE ")
        self.query.extend(args)

    def build(self):
        query = "".join(self.query)
        self.query = []
        return query


        # self.nodeNames = []
        # self.relationList = []  
    # def match_first_node(self, nodeName, type, **kwargs): # Match first node?
    #     self.nodeNames.append(nodeName)
    #     self.query.append(self.build_node(nodeName, type, **kwargs))
    #     # return self
    # def add_node(self, nodeName, type, **kwargs): # ??
    #     self.nodeNames.append(nodeName)
    #     if len(self.relationList) == 0 :
    #         self.query.append(", ")
    #     self.query.append(self.build_node(nodeName, type, **kwargs))
    # def build_node(self, nodeName, type, **kwargs):
    #     node = [f"({nodeName}:{type} "]
    #     print (len(kwargs.items()))
    #     if len(kwargs.items()) > 0 :
    #         node.append("{")
    #         for key, value in kwargs.items():
    #             node.append(key + ":" + f"'{value}'")
    #             node.append(",")
    #         node.pop()
    #         node.append("})")
    #     else: node.append(")")
    #     return("".join(node))
    # def return_query(self):
    #     return "".join(self.query)
    # def return_all_nodes_relations(self):
    #     returnedNodes = [" RETURN "]
    #     for nodename in self.nodeNames:
    #         returnedNodes.append(nodename)
    #         returnedNodes.append(",")
    #     for relation in self.relationList:
    #         returnedNodes.append(relation)
    #         returnedNodes.append(",")
    #     returnedNodes.pop()
    #     self.query.append("".join(returnedNodes))
    # def add_relationship(self,relationName,  relationType,):
    #     self.relationList.append(relationName)
    #     self.query.append(f" - [{relationName}:{relationType}] -> ")