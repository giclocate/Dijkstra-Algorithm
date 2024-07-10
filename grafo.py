import networkx as nx

def load_graph_from_file(file_path):
    G = nx.Graph()
    with open(file_path, 'r') as f:
        for line in f:
            node1, node2, weight = map(int, line.split())
            G.add_edge(node1, node2, weight=weight)
    return G

def dijkstra(graph, source):
    return nx.single_source_dijkstra(graph, source)
