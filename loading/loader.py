import csv
from py2neo import Graph, Node, Relationship

def check_node_if_exists(g: Graph, type: str, data: str):
    c = Node(type, name=data)
    exists = g.exists(c)
    c = g.match(c).first() if exists else c
    return c, exists

def update_or_create(tx, node_checked):
    if not node_checked[1]:
        tx.create(node_checked[0])

if __name__ == "__main__":
    print("here")
    g = Graph("http://://localhost:7474/db/data/",  user="neo4j", password="pwd")
    tx = g.begin()

    ifile = open('output/clean.csv', "r")
    reader = csv.reader(ifile)

    IN = "IN"
    AT = "AT"
    REQUIRING = "REQUIRING"
    
    for row in reader:
        print(row)
        title = row[0]
        company = row[1]
        location = row[2]
        position = row[3]
        skills = row[4].split(sep="-")

        title_node = check_node_if_exists(g, "Title", title)
        update_or_create(tx, title_node)
        company_node = check_node_if_exists(g, "Company", company)
        update_or_create(tx, company_node)
        location_node = check_node_if_exists(g, "Location", location)
        update_or_create(tx, location_node)
        position_node = check_node_if_exists(g, "Position", position)
        update_or_create(tx, position_node)

        tc = Relationship(title_node[0], AT, company_node[0])
        tl = Relationship(title_node[0], AT, location_node[0])
        cl = Relationship(location_node[0], AT, company_node[0])
        pt = Relationship(title_node[0], AT, position_node[0])

        tx.create(tc)
        tx.create(tl)
        tx.create(cl)
        tx.create(pt)


        for skill in skills:
            skill_node = check_node_if_exists(g, "Skill", skill)
            update_or_create(tx, skill_node)
            st = Relationship(skill_node[0], REQUIRING, title_node[0])
            tx.create(st)        

    tx.commit()

    ifile.close()
