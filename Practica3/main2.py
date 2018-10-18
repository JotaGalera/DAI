### Ejercicio 3

from flask import Flask,render_template,url_for,redirect,session,request
from pickleshare import *
import os

app = Flask(__name__)

db = PickleShareDB('~/testpickleshare')     #Definicion de la BDD
db.clear()                                  #Aseguramos que esté limpia

db['users']=['Javier','Antonio','Sergio']   #Le damos valores previos

usuarios_registrados = db['users']          #Cargamos el valor de la BDD en un array


@app.route('/')
def web():
    if 'uname' in session:
        uname = session['uname']
        return render_template('index.html', uname = uname)
    else:
        return render_template('index.html')

@app.route('/index.html')
def webSin():
    return redirect('/')

#Función login propia flask
@app.route('/login', methods=["POST"])
def login():

    name=request.form.get('uname')
    if name in usuarios_registrados:            #Comparamos si el nombre existe
        session['uname'] = name
    return redirect('/')

#Función logout propia flask
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/menu1')
def about():
    if 'uname' in session:
        uname = session['uname']
        return render_template('menu1.html', uname = uname)
    else:
        return render_template('menu1.html')


@app.route('/menu2')
def rooms():
    if 'uname' in session:
        uname = session['uname']
        return render_template('menu2.html', uname = uname)
    else:
        return render_template('menu2.html')

@app.route('/menu3')
def dives():
    if 'uname' in session:
        uname = session['uname']
        return render_template('menu3.html', uname = uname)
    else:
        return render_template('menu3.html')

@app.route('/datos')
def dates():
    if 'uname' in session:
        uname = session['uname']
        return render_template('login.html', uname = uname)
    else:
        return redirect('/')

@app.route('/change')
def change():
    if 'uname' in session:
        uname = session['uname']
        return render_template('change.html', uname = uname)
    else:
        return redirect('/')

@app.route('/cambio')
def cambio():
    return "hola"

#uname = session['uname']

#name=request.form.get('new_uname')
#print(name)
#usuarios_registrados[usuarios_registrados.index(uname)]=name
#db['users']=usuarios_registrados

@app.errorhandler(404)
def pagenotfound(error):
    return "This page not found",404
#http://0.0.0.0:5000/<CualquierOtraPagina>

#Ejercicio 5


if __name__ == "__main__":
  app.secret_key = os.urandom(24)
  app.run(debug = True, host='0.0.0.0')
