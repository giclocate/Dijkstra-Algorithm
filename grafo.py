import networkx as nx

def load_graph_from_file(file_path):
    graph = nx.Graph()
    with open(file_path, 'r') as file:
        for line in file:
            node1, node2, weight = line.split()
            node1 = int(node1)
            node2 = int(node2)
            weight = float(weight)  
            graph.add_edge(node1, node2, weight=weight)
    return graph
def dijkstra(graph, source):
    return nx.single_source_dijkstra(graph, source)
