import requests
import zipfile
import os

def download_and_extract_zip(url, extract_to='.'):
    local_zip_file = os.path.join(extract_to, 'temp.zip')
    
    # Baixar o arquivo zip
    response = requests.get(url)
    with open(local_zip_file, 'wb') as file:
        file.write(response.content)

    # Extrair o arquivo zip
    with zipfile.ZipFile(local_zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    
    # Remover o arquivo zip temporário
    os.remove(local_zip_file)

# URL do arquivo zipado
zip_url = 'https://nrvis.com/download/data/dynamic/copresence-InVS15.zip'  # Substitua pela URL real do arquivo zipado

# Diretório onde os arquivos serão extraídos
extract_dir = 'dados'

download_and_extract_zip(zip_url, extract_dir)
