import sqlite3
import os

def create_and_populate_db(db_name, data_dir):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Criar a tabela 'edges'
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS edges (
        source INTEGER,
        target INTEGER,
        weight REAL
    )
    ''')

    # Ler arquivos de dados e inserir no banco de dados
    for file_name in os.listdir(data_dir):
        if file_name.endswith('.txt'):
            file_path = os.path.join(data_dir, file_name)
            with open(file_path, 'r') as file:
                for line in file:
                    parts = line.strip().split()
                    if len(parts) == 2:
                        source, target = map(int, parts)
                        weight = 1.0  # Supondo peso 1 para arestas não ponderadas
                        cursor.execute('INSERT INTO edges (source, target, weight) VALUES (?, ?, ?)', (source, target, weight))
                    elif len(parts) == 3:
                        source, target, weight = int(parts[0]), int(parts[1]), float(parts[2])
                        cursor.execute('INSERT INTO edges (source, target, weight) VALUES (?, ?, ?)', (source, target, weight))

    conn.commit()
    conn.close()

# Nome do banco de dados
db_name = 'grafo.db'

# Diretório onde os arquivos de dados foram extraídos
data_dir = 'dados'

create_and_populate_db(db_name, data_dir)
