import requests
import csv

# URL da API JSONPlaceholder
url = "https://jsonplaceholder.typicode.com/comments"

# Faz a requisição GET
response = requests.get(url)

# Verifica se a requisição deu certo (código de status 200)
if response.status_code == 200:
    # Obtém os dados em formato JSON
    comments_data = response.json()
    print(f"Quantidade de comentarios: {len(comments_data)}") #Quantidade de comentarios: 500

    # Nome do arquivo CSV para exportar os resultados
    csv_filename = "dataset_comments.csv"

    # Abre o arquivo CSV em modo de escrita (w)
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
        # Cria um objeto escritor CSV
        csv_writer = csv.writer(csv_file)

        # Escreve o cabeçalho do CSV (nomes das colunas)
        csv_writer.writerow(["postId", "id", "name", "email", "body"])

        # Itera cada comentário, escrevendo cada linha no arquivo CSV
        for comment in comments_data:
            csv_writer.writerow([comment["postId"], comment["id"], comment["name"], comment["email"], comment["body"]])

    print(f"Os dados foram exportados para o arquivo: {csv_filename}")

else:
    # Se a requisição der erro, exibe o código de status
    print(f"A requisição falhou, status erro: {response.status_code}")
