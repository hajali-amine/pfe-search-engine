from orm.directions_enum import Direction


class QueryBuilder:
    def __init__(self) -> None:
        self.query = []

    def create(self):
        self.query.append("CREATE ")
        return self
    
    def match(self):
        self.query.append("MATCH ")
        return self
    
    def merge(self):
        self.query.append("MERGE ")
        return self
    
    def on_create(self):
        self.query.append("ON CREATE ")
        return self
    
    def on_match(self):
        self.query.append("ON MATCH ")
        return self

    def node(self, var_name, type, **kwargs):
        self.query.append(f"({var_name}")
        if type != "":
            self.query.append(f":{type}")
        self.query.append("{")
        for key, value in kwargs.items():
            self.query.append(key + ":" + f"'{value}'")
            self.query.append(",")
        self.query.pop()
        self.query.append("}) " if kwargs else ") ")
        return self

    def relation(self, var_name, type, direction, **kwargs):
        if direction == Direction.LEFT:
            self.query.append("<")
        self.query.append(f"-[{var_name} ")
        if type != "":
            self.query.append(f":{type}")
        self.query.append("{")
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
    
    def where(self, condition):
        self.query.append("WHERE ")
        self.query.append(condition)
        self.query.append(" ")
        return self

    def build(self):
        query = "".join(self.query)
        self.query = []
        return query
