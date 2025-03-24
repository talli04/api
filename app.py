from flask import Flask,request,jsonify

import sqlite3

app = Flask(__name__)

#route -> são os endpoints da nossa API
@app.route("/")
def Api_desafio():

    return "<h1>API que vai ser utilizada para o desafio 2 </h1>"

def init_db():

    with sqlite3.connect("database.db") as conn:
        conn.execute(
            """
                CREATE TABLE IF NOT EXISTS LIVROS(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    categoria TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    imagem_url TEXT NOT NULL
                )
            """
        )

init_db()

@app.route("/doar", methods=["POST"])
def doar():

    dados = request.get_json()

    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    imagem_url = dados.get("imagem_url")

    if not titulo or not categoria or not autor or not imagem_url:
        return jsonify({"erro":"Todos os campos são obrigatórios"}),400

# se o arquivo app.py == ao arquivo principal da nossa aplicação
if __name__ == "__main__":
    app.run(debug=True)