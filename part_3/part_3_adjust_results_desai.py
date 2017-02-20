import csv

with open("part_3_social_network_data.txt", "rb") as connect:
    # connections = csv.reader(connect, delimiter="\n")
    original = connect.readlines()
    nodes = []
    for line in original:
    	node = line.split("\t")[0].replace("\r","").replace("\n","")
    	nodes.append(int(node))
        # nodes = [line[0] for line.split("\t") in original]
    nodes = sorted(nodes)
    # print nodes
# print nodes[:20]

with open("final_mr_job.txt", "rb") as results:
	lines = results.readlines()
	output = {}
	for result in lines:
		result = result.replace("\r","").replace("\n","")
		node, recommended = result.split("\t")
		# print node, "\t", recommended.replace("[","").replace("]","")
		output[int(node)] = recommended.replace("[","").replace("]","")
	# print output
		# output[]
	# for line in lines:
	# 	print line.split("\t")[0], line.split("\t")[1]
# for node in nodes:
# 	if node in output:
# 		print node, '\t', output[node]
# 	else:
# 		print node

with open("final_mrjob_output.txt", "w") as write_output:
	for node in nodes:
		if node in output:
			# print node, output[node]
			write_output.write("{}\t{}\n".format(node, output[node]))
		else:
			# print node
			write_output.write("{}\n".format(node))