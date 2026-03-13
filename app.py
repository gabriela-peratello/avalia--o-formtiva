from flask import Flask, redirect, render_template, request
import mysql.connector
from database.conexao import conectar
from model.requisitos import cadastrar_requsito
from model.requisitos import recuperar_tarefas

app = Flask(__name__)

# Barra -> Entende que é a principal
@app.route("/")
def pag_principal():
    return render_template("index.html")

@app.route("/requi")
def pag_requisitos():
    return render_template("requisitos.html")

@app.route("/mstrequi")
def pag_requisitos():
    requisitos = recuperar_tarefas()
    return render_template("requisitos.html", requisitos = requisitos)

@app.route("/adcRequi", methods=["GET", "POST"])
def inserir_requisto():
    desc = request.form.get("descricao")
    nivel = request.form.get("nivel")
    val = request.form.get("valor")

    if cadastrar_requsito(desc, nivel, val):
        return redirect("/requi")
    else:
        return "Erro ao cadastrar"



if __name__ == "__main__":
    app.run(debug=True)
