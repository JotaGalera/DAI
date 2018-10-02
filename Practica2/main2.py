from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/user/<username>')
def perfilUser(username):
    return 'Usuario %s' % username

@app.errorhandler(404)
def pagenotfound(error):
    return "This page not found",404

if __name__ == "__main__":
  app.run(debug = True, host='0.0.0.0')
