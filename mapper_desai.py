#!/usr/bin/python
import sys
#import csv
import networkx as nx

# for line in sys.stdin:
#     print line
    # edge_list = [node[0].replace("\t",",") for node in line]
    # G = nx.parse_adjlist(edge_list, delimiter=",", nodetype=int)
    # print G
input = sys.argv[0]

with open(input, "rb") as connect:
    connections = csv.reader(connect, delimiter="\n")
    edge_list = [node[0].replace("\t",",") for node in connections]
    G = nx.parse_adjlist(edge_list, delimiter=",", nodetype=int)
    # print edge_list
    for node in nx.nodes(G):
        for non_con in nx.non_neighbors(G, node):
            for result in nx.common_neighbors(G, node, non_con):
                print '{}\t{}\t{}'.format(node, non_con, 1)
