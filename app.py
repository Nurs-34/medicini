from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recomendation")
def recomendation():
    return render_template("recomendation.html")

@app.route("/recforchild")
def recforchild():
    return render_template("recforchild.html")

@app.route("/lst")
def lst():
    return render_template("lst.html")

app.route("/proverka")
def proverka():
    return render_template("proverka.html")
    # не могу сделать наследование для проверки.хтмл

@app.route("/ManorChild/<name>")
def ManorChild(name):
    return render_template("manorchild.html", name=name)