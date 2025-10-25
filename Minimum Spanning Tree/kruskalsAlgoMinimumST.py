import networkx as nx
import matplotlib.pyplot as plt

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        rank[x] += 1

def kruskals_mst(edges, num_nodes):
    edges = sorted(edges, key=lambda x: x[2])  # Sort by weight
    parent = list(range(num_nodes))
    rank = [0] * num_nodes
    mst = []
    steps = []
    for u, v, w in edges:
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            mst.append((u, v, w))
            union(parent, rank, x, y)
            steps.append((u, v, w))
            print(f"Step: Added edge ({u},{v}) weight {w}")
    return mst, steps

def draw_graph(edges, mst_edges=None, title="Graph"):
    G = nx.Graph()
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    if mst_edges:
        nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='r', width=2)
    plt.title(title)
    plt.show()

# Graph 1: 7 nodes, 11 edges
graph1_edges = [(0,1,1), (0,2,4), (1,2,2), (1,3,6), (2,3,3), (2,4,3), (3,4,8), (3,5,7), (4,5,4), (4,6,5), (5,6,2)]
mst1, steps1 = kruskals_mst(graph1_edges, 7)
draw_graph(graph1_edges, [(e[0], e[1]) for e in mst1], "Graph 1 with MST")

# Graph 2: 5 nodes, 8 edges
graph2_edges = [(0,1,3), (0,2,5), (1,2,1), (1,3,4), (2,3,2), (2,4,6), (3,4,7), (0,4,8)]
mst2, steps2 = kruskals_mst(graph2_edges, 5)
draw_graph(graph2_edges, [(e[0], e[1]) for e in mst2], "Graph 2 with MST")

# Graph 3: 6 nodes, 9 edges
graph3_edges = [(0,1,2), (0,2,3), (1,2,4), (1,3,1), (2,4,5), (3,4,6), (3,5,7), (4,5,8), (0,5,9)]
mst3, steps3 = kruskals_mst(graph3_edges, 6)
draw_graph(graph3_edges, [(e[0], e[1]) for e in mst3], "Graph 3 with MST")
