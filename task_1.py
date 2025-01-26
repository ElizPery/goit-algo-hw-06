import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Add nodes and edges
G.add_nodes_from(["James", "Heuston", "Museum", "Smithfield", "Jervis", "Abbey Street", "Busarast", "George", "Connell", "GPO", "Westmoreland", "Marlborough", "Arran", "Four", "Custom"])
G.add_edges_from([("Heuston", "Arran"), ("Smithfield", "Four"), ("Abbey Street", "GPO"), ("Abbey Street", "Marlborough"), ("Busarast", "Custom"), ("James", "Heuston"), ("Heuston", "Museum"), ("Museum", "Smithfield"), ("Smithfield", "Jervis"), ("Jervis", "Abbey Street"), ("Abbey Street", "Busarast"), ("Busarast", "George"), ("Connell", "GPO"), ("GPO", "Westmoreland"), ("Connell", "Marlborough"), ("Arran", "Four"), ("Four", "Custom")])

# Draw the graph
options = {
    "node_color": "blue",
    "edge_color": "lightblue",
    "node_size": 1000,
    "width": 2,
    "with_labels": True
}
nx.draw(G, **options)
plt.show()

# Calculate number of nodes
num_nodes = G.number_of_nodes()

# Calculate number of edges
num_edges = G.number_of_edges()

# Check if graph is connected
is_connected = nx.is_connected(G)

# Find neighbors of the nodes
nodes_neighbors_arr = [f"\nNode {node} has the next neighbors: {list(G.neighbors(node))}" for node in G.nodes()]
nodes_neighbors_str = "".join(nodes_neighbors_arr)

# Find degree of the nodes
nodes_degree_arr = [f"\nDegree of the node {node}: {len(list(G.neighbors(node)))}" for node in G.nodes()]
nodes_degree_str = "".join(nodes_degree_arr)

print(f"Number of nodes: {num_nodes}\nNumber of edges: {num_edges}\nGraph is connected: {is_connected}")
print(nodes_neighbors_str)
print(nodes_degree_str)