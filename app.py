from flask import Flask, redirect, render_template, request
import mysql.connector
from database.conexao import conectar
from model.requisitos import cadastrar_requsito

app = Flask(__name__)

# Barra -> Entende que é a principal
@app.route("/")
def pag_principal():
    return render_template("index.html")

@app.route("/requi")
def pag_requisitos():
    return render_template("requisitos.html")

@app.route("/adcRequi", methods=["GET", "POST"])
def cad_requisto():
    desc = request.form.get("desc")
    nivel = request.form.get("nivel")
    val = request.form.get("val")

    if cadastrar_requsito(desc, nivel, val):
        return redirect("/requi")
    else:
        return "Erro ao cadastrar"



if __name__ == "__main__":
    app.run(debug=True)
