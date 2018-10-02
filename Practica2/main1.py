from flask import Flask
from flask import render_template,url_for 
app = Flask(__name__)

@app.route('/')
def web():
    return render_template('helloMod.html')

if __name__ == "__main__":
  app.run(debug = True, host='0.0.0.0')
