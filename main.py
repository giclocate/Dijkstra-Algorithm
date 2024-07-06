import networkx as nx
import sqlite3
import matplotlib.pyplot as plt

def conectar_banco(db_name):
    conn = sqlite3.connect(db_name)
    return conn

def criar_grafo_bd(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT source, target, weight FROM edges")
    rows = cursor.fetchall()

    G = nx.DiGraph()  # Usando um grafo direcionado
    for row in rows:
        G.add_edge(row[0], row[1], weight=row[2])
    
    return G

def input_usuario():
    no_inicial = int(input("Digite o nó inicial: "))
    no_final = int(input("Digite o nó final: "))
    return no_inicial, no_final

def menor_caminho(G, no_inicial, no_final):
    try:
        if not G.has_node(no_inicial) or not G.has_node(no_final):
            raise nx.NodeNotFound("Nó inicial ou final não encontrado no grafo.")

        caminho_minimo = nx.dijkstra_path(G, no_inicial, no_final)
        print(f"Caminho mínimo: {caminho_minimo}")

        # Cores dos arcos
        arcos_caminho = [(caminho_minimo[i], caminho_minimo[i+1]) for i in range(len(caminho_minimo)-1)]
        cor_dos_arcos = ['r' if arco in arcos_caminho else 'b' for arco in G.edges]

        # Posições dos nós
        posicoes_nos = nx.spring_layout(G)  
        
        # Desenho do grafo
        nx.draw_networkx(G, pos=posicoes_nos, edge_color=cor_dos_arcos, with_labels=True,
                         node_color='w', edgecolors='black', node_size=500, font_size=10, font_color='k')

        plt.show()

    except nx.NetworkXNoPath:
        print(f"Não há caminho de {no_inicial} para {no_final}")
    except nx.NodeNotFound as e:
        print(f"Erro: {e}")

def main():
    db_name = 'grafo.db'  # Substitua pelo nome do seu banco de dados
    conn = conectar_banco(db_name)
    G = criar_grafo_bd(conn)
    no_inicial, no_final = input_usuario()
    menor_caminho(G, no_inicial, no_final)

if __name__ == "__main__":
    main()
