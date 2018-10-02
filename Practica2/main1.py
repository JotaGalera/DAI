from flask import Flask
from flask import render_template,url_for
from flask import Response

app = Flask(__name__)

@app.route('/')
def web():
    return render_template('helloMod.html')

@app.route('/png')
def png():
    response = Response()
    response.headers.add('Content-Type' , 'image/png')
    im = open('static/img/Tux.png','rb')
    imagen = im.read()
    response.set_data(imagen)
    return response

if __name__ == "__main__":
  app.run(debug = True, host='0.0.0.0')
