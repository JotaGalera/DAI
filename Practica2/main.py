from flask import Flask
from flask import render_template,url_for
from flask import Response
import random

app = Flask(__name__)

#Ejercicio 2

@app.route('/')
def web():
    return '''<!DOCTYPE html>
    <html lang="es">
      <head>
        <title>Practica 2</title>
        <link rel="stylesheet" type="text/css" href="static/css/style.css">
      </head>
      <body>
        <h1>Cargando estilos estaticos:</h1>
        <div>
          <p>Gracias a render_template podemos retornar nuestro html.
             Y gracias a url_for el css.
          </p>
          <img src="static/img/Tux.png" alt="Smiley face" height="42" width="42">
        </div
      </body>
    </html>'''

#Otra opcion:
#<link rel="stylesheet" type="text/css" href="{{url_for('static',filename='static/css/style.css' )}}">
#return render_template('helloMod.html')

@app.route('/png')
def png():
    response = Response()
    response.headers.add('Content-Type' , 'image/png')
    im = open('static/img/Tux.png','rb')
    imagen = im.read()
    response.set_data(imagen)
    return response

#Ejercicio 3

@app.route('/user/<username>')
def perfilUser(username):
    return 'Usuario %s' % username
#http://0.0.0.0:5000/user/<CualquierNombre>


@app.route('/user/')
def perfilUserConParametros(username=None):
    parametro1=request.args.get('variable1')
    parametro2=request.args.get('variable2')
    return parametro1 + ' ' + parametro2
#http://0.0.0.0:5000/user/?variable1=hole&variable2=adios

@app.errorhandler(404)
def pagenotfound(error):
    return "This page not found",404
#http://0.0.0.0:5000/<CualquierOtraPagina>

#Ejercicio 5

@app.route('/dynamic')
def dynamic():
    random_n = random.randint(1,5)
    if random_n == 1:
        return '''
                <svg width="100" height="100">
                    <circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" />
                </svg>
                '''
    elif random_n == 2:
        return '''
                <svg width="400" height="110">
                    <rect width="300" height="100" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
                    Sorry, your browser does not support inline SVG.
                </svg>
                '''
    elif random_n == 3:
        return '''
                 <svg height="210" width="500">
                    <polygon points="200,10 250,190 160,210" style="fill:lime;stroke:purple;stroke-width:1" />
                </svg>
                '''
    elif random_n == 4:
        return '''
                 <svg height="200" width="500">
                    <polyline points="20,20 40,25 60,40 80,120 120,140 200,180"
                    style="fill:none;stroke:black;stroke-width:3" />
                </svg>
                '''
    elif random_n == 5:
        return '''
                 <svg height="150" width="400">
                    <defs>
                        <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
                        <stop offset="0%" style="stop-color:rgb(255,255,0);stop-opacity:1" />
                        <stop offset="100%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
                        </linearGradient>
                    </defs>
                    <ellipse cx="200" cy="70" rx="85" ry="55" fill="url(#grad1)" />
                </svg>
                '''


if __name__ == "__main__":
  app.run(debug = True, host='0.0.0.0')
