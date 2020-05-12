"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Invalid vertices")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        raise IndexError("Invalid vertex")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        visited = set()

        queue.enqueue(starting_vertex)

        while queue.size() > 0:
            v = queue.dequeue()
            if v not in visited:
                print(v)
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    queue.enqueue(next_vert)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()

        stack.push(starting_vertex)

        while stack.size() > 0:
            v = stack.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    stack.push(next_vert)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()

        def dft(vertex, visited):
            visited.add(vertex)
            print(vertex)
            for neighbor in self.get_neighbors(vertex):
                if neighbor not in visited:
                    dft(neighbor, visited)

        return dft(starting_vertex, visited)
        
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        # Put the starting point in that
        q.enqueue([starting_vertex])
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the queue/stack
        while q.size() > 0:
            path = q.dequeue()
            vertex = path[-1]
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                # For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                    # Copy path to avoid pass by reference
                    new_path = list(path)
                    new_path.append(next_vert)
                    #print(path, new_path)
                    q.enqueue(new_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        # Put the starting point in that
        s.push([starting_vertex])
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the queue/stack
        while s.size() > 0:
            path = s.pop()
            vertex = path[-1]
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                # For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                    # Copy path to avoid pass by reference bug
                    new_path = list(path)
                    new_path.append(next_vert)
                    #print(path, new_path)
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited = set()
        path = []

        def traverse(current, destination, visited, path):

            visited.add(current)
            path = path + [current]

            if current == destination_vertex:
                return path

            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    new_path = traverse(neighbor, destination_vertex, visited, path)
                    if new_path:
                        return new_path
            return None

        return traverse(starting_vertex, destination_vertex, visited, path)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
