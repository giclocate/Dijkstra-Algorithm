# Projeto de Cálculo de Menor Caminho em Grafos com Algoritmo de Dijkstra

## Descrição
Este projeto tem como objetivo calcular o menor caminho entre dois pontos quaisquer em um grafo utilizando o algoritmo de Dijkstra. Os dados para montar o grafo são obtidos a partir de um arquivo contendo informações sobre interações entre animais. O projeto inclui uma visualização do grafo, destacando o menor caminho encontrado.

## Funcionalidades
- Leitura de dados de interações a partir de um arquivo.
- Construção de um grafo não direcionado e ponderado.
- Cálculo do menor caminho entre dois nós escolhidos pelo usuário utilizando o algoritmo de Dijkstra.
- Visualização do grafo com destaque para o menor caminho encontrado.

## Linguagem e Bibliotecas Utilizadas
### Linguagem
- Python 3.8+

### Bibliotecas
- `os`: Para operações de sistema de arquivos.
- `matplotlib`: Para visualização do grafo.
- `networkx`: Para criação e manipulação do grafo.

### Instalação das Bibliotecas
Para instalar as bibliotecas necessárias, execute:
```bash
pip install matplotlib networkx
```

## Estrutura do Projeto
- `main.py`: Contém a função principal que coordena a execução do programa.
- `grafo.py`: Contém as funções `grafo_arquivo` e `dijkstra` para construir o grafo e calcular o menor caminho.
- `dados/mammalia-macaque-contact-sits.edges`: Arquivo de dados utilizado para construir o grafo.

## Como Executar
1. Certifique-se de que todas as bibliotecas necessárias estão instaladas.
2. Coloque o arquivo de dados `mammalia-macaque-contact-sits.edges` no diretório `dados`.
3. Execute o script `main.py`:
   ```bash
   python main.py
   ```
4. Insira os nós de origem e destino quando solicitado.

## Contribuidores
- **Giovanna Clócate**: Responsável pelo desenvolvimento do código principal e visualização.
- **Amós Kinsley**: Responsável pela integração do banco de dados no código principal.
- **Lucas dos Santos**: Auxílio na implementação do algoritmo de Dijkstra e testes.

## Imagens
![WhatsApp Image 2024-07-15 at 17 27 09](https://github.com/user-attachments/assets/88e8adee-5a66-47d5-b4c5-3896e45bbc09)

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Referências
- Dados de interações animais: [Animal Networks - Bansal Lab](https://bansallab.github.io/asnr/data.html)
