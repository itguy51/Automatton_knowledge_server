from semnet import *
import re
import sys

#Create dictionary of entities and relations as, 'memory'
entities = {}
relations = { "isa": GetIsA() }

#Declare some rules to make it a bit user friendly
rules = (
    ("e\>(.*)", lambda g: addEntity(g)),
    ("r\>(.*)", lambda g: addRelation(g)),
    ("(.*)\>(.*)\>(.*)", lambda g: addFact(g)),
    ("([a-zA-Z\_\-]*)\((.*)\, (.*)\)", lambda g: isTrue(g)),
    ("objects\((.*)\, (.*)\)", lambda g: objects(g)),
    ("dump", lambda g: dump(g))
)

#Declare some functions
def dump(g):
    print entities
    print relations

def objects(g):
    print entities[g[0]].objects(relations[g[1]])

def isTrue(g):
    output = relations[g[0]](entities[g[1]], entities[g[2]])
    print 'true' if output > 0 else 'false'

def addEntity(g):
    entities[g[0]] = Entity(g[0])
    print "Entity added:", g[0]
    
def addRelation(g):
    relations[g[0]] = Relation(g[0])
    print "Relationship added:", g[0]
    
def addFact(g):
    entity1 = entities[g[0]]
    relationship = relations[g[1]]
    entity2 = entities[g[2]]
    Fact(entity1, relationship, entity2)
    print "I understand"

def action(input):
    for rule in rules:
        match = re.match(rule[0], input)
        if match:
            rule[1](match.groups())
            break

#main function
def main():
    while True:
        input = raw_input("? ")
        if input == "quit":
            sys.exit()
        action(input)
        
if __name__ == "__main__": main()