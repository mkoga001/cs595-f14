#!/usr/local/bin/python

import sys
import json
import networkx
from networkx.readwrite import json_graph

f = open("club.json")
inputlines = json.load(f)
f.close()

club = json_graph.node_link_graph(inputlines)

while (networkx.number_connected_components(club) < 2):
    eb = networkx.edge_betweenness_centrality(club, weight = 'weight')
    edgeRemove = sorted(eb.items(), key=lambda x:x[1], reverse=True)[0][0]
    club.remove_edge(*edgeRemove)
    
output = json_graph.node_link_data(club)

print(json.dumps(output))
    
   
    

