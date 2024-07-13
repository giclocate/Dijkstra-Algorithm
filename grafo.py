import networkx as nx

def grafo_arquivo(file_path):
    grafo = nx.Graph()
    with open(file_path, 'r') as file:
        for line in file:
            no_origem, no_destino, peso = line.split()
            no_origem = int(no_origem)
            no_destino = int(no_destino)
            peso = float(peso)  
            grafo.add_edge(no_origem, no_destino, weight=peso)
    return grafo
def dijkstra(graph, source):
    return nx.single_source_dijkstra(graph, source)
