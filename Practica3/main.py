### Ejercicio 2

from flask import Flask,render_template,url_for,redirect,session,request
import os

app = Flask(__name__)


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


@app.errorhandler(404)
def pagenotfound(error):
    return "This page not found",404



if __name__ == "__main__":
  app.secret_key = os.urandom(24)
  app.run(debug = True, host='0.0.0.0')
