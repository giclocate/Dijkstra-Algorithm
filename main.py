import os
import matplotlib.pyplot as plt
import networkx as nx
from grafo import grafo_arquivo, dijkstra

def main():
    caminho_arquivo = 'dados\mammalia-macaque-contact-sits.edges'
   
    if not os.path.exists(caminho_arquivo):
        print(f"Arquivo {caminho_arquivo} não existe.")
        return

    grafo = grafo_arquivo(caminho_arquivo)

    nos_validos = set(grafo.nodes())
    
    while True:
        try:
            no_origem = int(input("Digite o nó de origem: "))
            if no_origem not in nos_validos:
                raise ValueError(f"Nó de origem {no_origem} não existe no grafo.")
            break
        except ValueError as e:
            print(e)
    
    while True:
        try:
            no_destino = int(input("Digite o nó de destino: "))
            if no_destino not in nos_validos:
                raise ValueError(f"Nó de destino {no_destino} não existe no grafo.")
            break
        except ValueError as e:
            print(e)
   
    distancias, caminhos = dijkstra(grafo, no_origem)
   
    if no_destino not in distancias:
        print(f"Nenhum caminho encontrado do nó {no_origem} para o nó {no_destino}.")
    else:
        distancia = distancias[no_destino]
        caminho = caminhos[no_destino]
        print(f"Menor distância do nó {no_origem} para o nó {no_destino}: {distancia}")
        print(f"Caminho: {' -> '.join(map(str, caminho))}")
       
        visualizar_grafo(grafo, caminho, no_origem, no_destino, distancia)

def visualizar_grafo(grafo, caminho, no_origem, no_destino, distancia):
    pos = nx.spring_layout(grafo, seed=12, k=3.5, iterations=100)  
    plt.figure(figsize=(14, 14))
   
    nx.draw_networkx_edges(grafo, pos, edge_color='lightgray', width=0.5)
    nx.draw_networkx_nodes(grafo, pos, node_size=500, node_color='skyblue', linewidths=0.5, edgecolors='black')
   
    nx.draw_networkx_edges(grafo, pos, edgelist=list(zip(caminho, caminho[1:])), edge_color='red', width=2.5)
    nx.draw_networkx_nodes(grafo, pos, nodelist=caminho, node_size=700, node_color='red', edgecolors='black')
   
    nx.draw_networkx_labels(grafo, pos, font_size=10, font_color='black')
   
    edge_labels = {(caminho[i], caminho[i+1]): grafo[caminho[i]][caminho[i+1]]['weight'] for i in range(len(caminho) - 1)}
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=edge_labels, font_color='black')
   
    plt.title(f'Visualização do Grafo\nMenor caminho do nó {no_origem} ao nó {no_destino}\nA menor distância: {distancia}', fontsize=15)
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()