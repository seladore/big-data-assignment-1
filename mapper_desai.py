#!/usr/bin/env python
import sys
import zipimport
#import csv
#import networkx as nx

importer = zipimport.zipimporter("networkx.mod")
nx = importer.load_module("networkx")

# for line in sys.stdin:
#     print line
    # edge_list = [node[0].replace("\t",",") for node in line]
    # G = nx.parse_adjlist(edge_list, delimiter=",", nodetype=int)
    # print G
#input = sys.argv[0]

#with open(input, "rb") as connect:
 #   connections = csv.reader(connect, delimiter="\n")
#for line in sys.stdin:
    #line = line.strip()
#	print line
#	edge_list = [node[0].replace("\t",",") for node in line]
#	G = nx.parse_adjlist(edge_list, delimiter=",", nodetype=int)
    # print edge_list
#	for node in nx.nodes(G):
#		for non_con in nx.non_neighbors(G, node):
#	    		for result in nx.common_neighbors(G, node, non_con):
#				print '{}\t{}\t{}'.format(node, non_con, 1)

#!/usr/bin/env python

#import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        print '%s\t%s' % (word, 1)
