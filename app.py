from flask import Flask, jsonify
import requests
import csv
from io import StringIO

app = Flask(__name__)

def get_comments_data():
    # URL da API JSONPlaceholder
    url = "https://jsonplaceholder.typicode.com/comments"

    # Faz a requisição GET
    response = requests.get(url)

    # Verifica se a requisição deu certo (código de status 200)
    if response.status_code == 200:
        # Obtém os dados em formato JSON
        comments_data = response.json()
        # Retorna os dados
        return comments_data
    else:
        # Se a requisição falhou, retorna uma lista vazia
        return []

@app.route('/api/comments', methods=['GET'])
def get_comments():
    # Obtém os dados dos comentários
    comments_data = get_comments_data()

    # Retorna os dados no formato JSON
    return jsonify(comments_data)

if __name__ == '__main__':
    # Executa o aplicativo Flask
    app.run(debug=True)
    #http://127.0.0.1:5000/api/comments  <-- URL que esta rodando o servidor