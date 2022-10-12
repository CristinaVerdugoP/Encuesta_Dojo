from flask import Flask, render_template, request, redirect, session
from mi_app import app
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def formulario():
    return render_template("index.html")

@app.route('/process', methods = ["POST"])
def process():
    session['nombre'] = request.form['name']
    session['ciudad'] = request.form['city']
    session['lenguaje'] = request.form['language']
    session['comentarios'] = request.form['comments']
    return redirect('/resultado_formulario')

@app.route('/resultado_formulario')
def resultado_formulario():
    return render_template("datos.html", name = session['nombre'], city = session['ciudad'], lenguage = session['lenguaje'], comments = session['comentarios'])
