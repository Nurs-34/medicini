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

@app.route("/list")
def lst():
    return render_template("list.html")