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


@app.route('/about.html')
def about():
    if 'uname' in session:
        uname = session['uname']
        return render_template('about.html', uname = uname)
    else:
        return render_template('about.html')


@app.route('/rooms.html')
def rooms():
    if 'uname' in session:
        uname = session['uname']
        return render_template('rooms.html', uname = uname)
    else:
        return render_template('rooms.html')

@app.route('/dives.html')
def dives():
    if 'uname' in session:
        uname = session['uname']
        return render_template('dives.html', uname = uname)
    else:
        return render_template('dives.html')

@app.route('/foods.html')
def foods():
    if 'uname' in session:
        uname = session['uname']
        return render_template('foods.html', uname = uname)
    else:
        return render_template('foods.html')

@app.route('/news.html')
def news():
    if 'uname' in session:
        uname = session['uname']
        return render_template('news.html', uname = uname)
    else:
        return render_template('news.html')

@app.route('/contact.html')
def contact():
    if 'uname' in session:
        uname = session['uname']
        return render_template('contact.html', uname = uname)
    else:
        return render_template('contact.html')

@app.errorhandler(404)
def pagenotfound(error):
    return "This page not found",404
#http://0.0.0.0:5000/<CualquierOtraPagina>

#Ejercicio 5


if __name__ == "__main__":
  app.secret_key = os.urandom(24)
  app.run(debug = True, host='0.0.0.0')
