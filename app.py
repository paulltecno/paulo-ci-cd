from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello World Paulo Oliveira CI - CI DevOps MBA CLC 11"
