from flask import Flask,request,jsonify

import sqlite3

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#route -> são os endpoints da nossa API
@app.route("/")
def Api_desafio():

    return "<h1>API que vai ser utilizada para o desafio final do modulo 2 </h1>"

def init_db():

    with sqlite3.connect("database.db") as conn:
        conn.execute(
            """
                CREATE TABLE IF NOT EXISTS LIVROS(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    categoria TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    image_url TEXT NOT NULL
                )
            """
        )

    quantidade = conn.execute("SELECT COUNT(*) FROM livros").fetchone()[0]


    if quantidade == 0:
    
        livros_padrao = [
            ("Fome de Poder", "Biografia", "Ray Krok", "https://i.pinimg.com/736x/41/eb/0a/41eb0a0dd7aef77d55684376473df884.jpg"),
            ("Quem tem Dívidas, tem Dúvidas", "Finanças", "André Luiz Manzano", "https://m.media-amazon.com/images/I/81StxOXIWqL._SL1500_.jpg"),
            ("O pequeno gatinho xadrez", "Infantil", "Maria Helena Paes", "https://www.formandocidadaos.com.br/images/capas/literaturas/capa_340.jpg"),
        ]

    
        for livro in livros_padrao:
       
            titulo, categoria, autor, image_url = livro
        
       
            conn.execute(f'''
                INSERT INTO livros (titulo, categoria, autor, image_url)
                VALUES ("{titulo}", "{categoria}", "{autor}", "{image_url}")
            ''')
        
        conn.commit()

init_db()

@app.route("/doar", methods=["POST"])
def doar():

    dados = request.get_json()

    print(f"AQUI ESTÃO OS DADOS RETORNADOS DO CLIENTE {dados}")
    
    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    image_url = dados.get("image_url")
    if not titulo or not categoria or not autor or not image_url:
        return jsonify({"erro":"Todos os campos são obrigatórios"}),400

    with sqlite3.connect("database.db") as conn:

        conn.execute(f"""
        INSERT INTO LIVROS (titulo, categoria, autor, image_url)
        VALUES ("{titulo}", "{categoria}", "{autor}", "{image_url}")
        """)

    conn.commit()

    return jsonify({"mensagem": "Livro cadastrado com sucesso"}), 201

@app.route("/livros", methods=["GET"])
def listar_livros():

    with sqlite3.connect("database.db") as conn:
       livros = conn.execute("SELECT * FROM LIVROS").fetchall()

       livros_formatados = []

       for item in livros:
           dicionario_livros = {
               "id": item[0],
               "titulo": item[1],
               "categoria": item[2],
               "autor": item[3],
               "image_url": item[4]
           }
           livros_formatados.append(dicionario_livros)
    
    return jsonify(livros_formatados)


# se o arquivo app.py == ao arquivo principal da nossa aplicação
if __name__ == "__main__":
    app.run(debug=True)