from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/user/<username>')
def perfilUser(username):
    return 'Usuario %s' % username
#http://0.0.0.0:5000/user/CualquierNombre


@app.route('/user/')
def perfilUserConParametros(username=None):
    parametro1=request.args.get('variable1')
    parametro2=request.args.get('variable2')
    return parametro1 + ' ' + parametro2
#http://0.0.0.0:5000/user/?variable1=hole&variable2=adios


@app.errorhandler(404)
def pagenotfound(error):
    return "This page not found",404

if __name__ == "__main__":
  app.run(debug = True, host='0.0.0.0')
#http://0.0.0.0:5000/CualquierOtraRuta
