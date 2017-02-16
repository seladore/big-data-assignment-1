#!/usr/bin/python

# Big Data Spring 2017
# Assignment 1
# MSBA GROUP 11

#_______________________________________________
## DIRECTORY
## | 1 | Import Packages
## | 2 | Input File and Create Graph Object
## | 3 | Map and Reduce by Mutual Edges
## | 4 | Output File

#_______________________________________________
## | 1 | Import Packages
import csv
import networkx as nx
# import re
import time

#_______________________________________________
## | 2 | Input File and Create Graph Object
start = time.time()
with open("part_3_testing_data.txt", "rb") as connect:
    connections = csv.reader(connect, delimiter="\n")
    edge_list = [node[0].replace("\t",",") for node in connections]
    G = nx.parse_adjlist(edge_list, delimiter=",", nodetype=int)

#_______________________________________________
## | 3 | Map and Reduce by Mutual Edges
counter = 0
results = {}
#for node in range(0,500):
for node in nx.nodes(G):
    mutuals = {}
    for non_con in nx.non_neighbors(G, node):
        num_mutuals = len(sorted(nx.common_neighbors(G, node, non_con)))
        if num_mutuals > 1:
            mutuals[non_con] = num_mutuals
    mutuals = sorted(mutuals.items(), key=lambda x: (x[1], x), reverse=True)[:10]
    results[node] = [x[0] for x in mutuals]
    counter = counter+1


#_______________________________________________
## | 4 | Output File
with open("social_network_recommendations.txt", "w") as output:
    for key, value in results.items():
        output.write("{}\t{}\n".format(key,value))
end = time.time()
print end-start
