import networkx as nx
import sqlite3
import numpy as np
import matplotlib.pyplot as plt

def conectar_banco(db_name):
    conn = sqlite3.connect(db_name)
    return conn

def criar_grafo_bd(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT source, target, weight FROM edges")
    rows = cursor.fetchall()

    G = nx.Graph()
    for row in rows:
        G.add_edge(row[0], row[1], weight=row[2])
    
    return G

def input_usuario():
    no_inicial = int(input("Digite o nó inicial: "))
    no_final = int(input("Digite o nó final: "))
    return no_inicial, no_final

# encontrar e exibir o caminho mínimo
def menor_caminho(G, no_inicial, no_final):
    caminho_minimo = nx.dijkstra_path(G, no_inicial, no_final)
    print(f"Caminho mínimo: {caminho_minimo}")

    arcos_caminho = [(caminho_minimo[i], caminho_minimo[i+1]) for i in range(len(caminho_minimo)-1)]
    cor_dos_arcos = []
    for arco in G.edges:
        if arco in arcos_caminho:
            cor_dos_arcos.append('r')
        else:
            cor_dos_arcos.append('b')

    posicoes_nos = nx.spring_layout(G)  
    nx.draw_networkx(G, pos=posicoes_nos, edge_color=cor_dos_arcos, with_labels=True, node_color='w', edgecolors='black', node_size=500, font_size=10, font_color='k')

    plt.show()

# função principal
def main():
    db_name = 'seu_banco_de_dados.db'  # substitua pelo nome do seu banco de dados
    conn = conectar_banco(db_name)
    G = criar_grafo_bd(conn)
    no_inicial, no_final = input_usuario()
    menor_caminho(G, no_inicial, no_final)

if __name__ == "__main__":
    main()