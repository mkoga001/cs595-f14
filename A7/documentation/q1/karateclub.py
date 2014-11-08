#!/usr/local/bin/python
import json

f = open("zachary.dat")
inputlines = f.readlines()
f.close()
karatejson = {"links" : [],"nodes" : []}
counter = 0
for row in inputlines[7 + 34:]:
    columns = row.split()
    node = counter + 1
    #In order draw graph in d3 we need both nodes and links so nodes are computed.
    newNode = { 'id' : str(node) }
    
    karatejson['nodes'].append( newNode )
    for col in range(len(columns)):
        #compute the links which have edges other wise skip it.
        if columns[col] != "0":
            source = node
            target = col + 1
            weight = int(columns[col])
            
            newLink = \
                { "target" : target,"source" : source,  "weight" : weight }
            
            karatejson['links'].append( newLink )
    counter += 1 
    
print(json.dumps(karatejson))
        
        
            
    
    
    
    