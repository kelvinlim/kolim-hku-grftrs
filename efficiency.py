import networkx as nx

# Create a directed graph
G = nx.DiGraph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4)])

# Compute global efficiency
global_efficiency = nx.global_efficiency(G)

print(f"Global efficiency: {global_efficiency:.4f}")

