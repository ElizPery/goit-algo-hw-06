from collections import deque
import networkx as nx

G = nx.Graph()

# Add nodes and edges
G.add_nodes_from(["James", "Heuston", "Museum", "Smithfield", "Jervis", "Abbey_Street", "Busarast", "George", "Connell", "GPO", "Westmoreland", "Marlborough", "Arran", "Four", "Custom"])
G.add_edges_from([("Heuston", "Arran"), ("Smithfield", "Four"), ("Abbey_Street", "GPO"), ("Abbey_Street", "Marlborough"), ("Busarast", "Custom"), ("James", "Heuston"), ("Heuston", "Museum"), ("Museum", "Smithfield"), ("Smithfield", "Jervis"), ("Jervis", "Abbey_Street"), ("Abbey_Street", "Busarast"), ("Busarast", "George"), ("Connell", "GPO"), ("GPO", "Westmoreland"), ("Connell", "Marlborough"), ("Arran", "Four"), ("Four", "Custom")])

graph = {node: list(G.neighbors(node)) for node in G.nodes()}

def dfs_recursive(graph, vertex, visited=None, path=None, parent=None):
    if visited is None:
        visited = set()
        path = []

    # Add the vertex to visited
    visited.add(vertex)
    if parent is not None:
        path.append((parent, vertex))
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, path, vertex)
    return path


def bfs_iterative(graph, start):
    # Initializing an empty set to store visited vertices
    # Initializing an array with a start vertex
    visited, queue  = {start}, [start]
    path = []

    while queue:  # Until the queue is empty, we continue to bypass
        # Remove the first vertex from the queue
        vertex = queue.pop(0)
        
        for neighbor in graph[vertex]:
            # Check if it has been visited before
            if neighbor not in visited:
                # Add a vertex to the set of visited vertices
                visited.add(neighbor)
                # Add all untrusted vertex neighbors to the end of the queue
                queue.append(neighbor)
                path.append((vertex, neighbor))
    # Return the set of pathes after completing the walk
    return path


print(dfs_recursive(graph, "James"))
print(bfs_iterative(graph, "James"))