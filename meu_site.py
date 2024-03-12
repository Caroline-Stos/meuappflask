from flask import Flask, render_template, url_for

app = Flask(__name__)

app.static_folder = 'static'

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/usuario/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

if __name__ == '__main__':
    app.run(debug=True)

