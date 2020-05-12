import sys
sys.path.insert(0, '../graph')
from util import Queue
from graph import Graph

def build_graph(ancestors):
	graph = Graph()

	for ancestor in ancestors:
		(first_relative, second_relative) = ancestor
		if first_relative not in graph.vertices:
			graph.add_vertex(first_relative)
		if second_relative not in graph.vertices:
			graph.add_vertex(second_relative)

	for relationship in ancestors:
		(parent, child) = relationship
		graph.add_edge(child, parent)

	return graph

def earliest_ancestor(ancestors, starting_node):
	graph = build_graph(ancestors)
	# breadth first approach, want to take it layer by layer
	# start at vertex
	queue = Queue()
	visited = set()
	queue.enqueue(starting_node)

	# what are we looking for? the oldest ancestor which connected to our starting node
	ancestor = -1

	while queue.size() > 0:
		# explore the vertex
		current = queue.dequeue()
		print("our current", current)
		# check to make sure we have neighbors
		if len(graph.get_neighbors(current)) != 0:
			for relative in graph.get_neighbors(current):
				# if unexplored
				print("current:", current, "relatives:", relative)
				if relative not in visited:
					# explore the adjacent vertex
					print("enqueued", relative)
					queue.enqueue(relative)
		# check to see if our visited set is not empty, if it's not our current will become our ancestor
		elif visited:
			ancestor = current
		# if our current is not in our set, add it
		if current not in visited:
			visited.add(current)

	return ancestor