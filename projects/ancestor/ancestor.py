import sys
sys.path.insert(0, '../graph')
from util import Queue
from graph import Graph

def build_graph(ancestors):
	graph = Graph()

	for ancestor in ancestors:
		(parent, child) = ancestor
		
		if parent not in graph.vertices:
			graph.add_vertex(parent)
		if child not in graph.vertices:
			graph.add_vertex(child)

		graph.add_edge(child, parent)

	return graph

def earliest_ancestor(ancestors, starting_node):
	graph = build_graph(ancestors)
	# breadth first approach, want to take it layer by layer
	# start at vertex
	queue = Queue()
	queue.enqueue([starting_node])
	print("--------------")
	print("Starting node:", starting_node)

	# what are we looking for? the oldest ancestor which connected to our starting node
	ancestor = -1
	max_path_length = 1

	while queue.size() > 0:
		# explore the vertex
		path = queue.dequeue()
		print("path", path)
		current = path[-1]
		print("our current", current)
		# if lengthe path is greater than max path and current is less than ancestor, make ancestor to current
		# max_path_length is a path length
		if (len(path) >= max_path_length and current < ancestor) or (len(path) > max_path_length):
			ancestor = current
			max_path_length = len(path)
		# check the neighbors, copy the list and add the neighbors to each copy
		for relative in graph.get_neighbors(current):
			print("current:", current, "relatives:", relative)
			path_copy = list(path)
			path_copy = path_copy + [relative]
			# explore the adjacent vertex
			print("enqueued", path_copy)
			queue.enqueue(path_copy)
		# check to see if our visited set is not empty, if it's not our current will become our ancestor
	print("FOUND ancestor:", ancestor)
	return ancestor