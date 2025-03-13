from flask import Flask

app = Flask(__name__)

#route -> são os endpoints da nossa API
@app.route("/")
def pagar_pessoas():

    return "<h1>Começar a semana, pagando suas dívidas, é bom demais</h1>"

@app.route("/pix")
def mande_o_pix():

    return "<h3>Pagar as pessoas faz bem pras pessoas!!! =D</h3>"

@app.route("/comidas")
def prato_do_dia():

    return "<h1>o prato do dia é feijoada</h1>"


# se o arquivo app.py == ao arquivo principal da nossa aplicação
if __name__ == "__main__":
    app.run(debug=True)