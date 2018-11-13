### Ejercicio 3

from flask import Flask,render_template,url_for,redirect,session,request
from pickleshare import *
import os
import urllib.request
from pymongo import MongoClient



app = Flask(__name__)

#MONGO
#client = MongoClient()
client = MongoClient('localhost',27017)

dbMongo = client['Restaurants']
collectionMongo = dbMongo['RestaurantsCollection']
####
db = PickleShareDB('~/testpickleshare')     #Definicion de la BDD
                                  #Aseguramos que esté limpia

db['Javier']={'Apellido':'Galera','DNI':'75936176','pass':'qwerty'}
db['Sergio']={'Apellido':'Martinez','DNI':'78451296','pass':'qwerty2'}   #Le damos valores previos
db['Antonio']={'Apellido':'Jimenez','DNI':'78123123','pass':'qwerty3'}
usuarios_registrados = db.keys()          #Cargamos el valor de la BDD en un array


@app.before_request
def beforeRequest():
    if 'historial' in session:
        session['historial'].append(request.url)
        print (session['historial'])
        if len(session['historial']) > 3:
            session['historial'].pop(0)




@app.route('/')
def web():
    print('USUARIOS REGISTRADOS EN INDEX')
    print(usuarios_registrados)
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
        session['historial']=[]
        if 'historial' in session:
            session['historial'].append(request.url)
            if len(session['historial']) > 3:
                session['historial'].pop(0)
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
        historial = session['historial']
        if 'historial' in session:
            session['historial'].append(request.url)
            if len(session['historial']) > 3:
                session['historial'].pop(0)
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

@app.route('/newuser')
def formnewuser():
    return render_template('newuser.html')

@app.route('/register',methods=["POST"])
def registernewuser():
    newuser=request.form.get('new_user')
    newapel=request.form.get('new_apellido')
    newdni =request.form.get('new_dni')
    newpass=request.form.get('new_password')
    db[newuser]={'Apellido':newapel,'DNI':newdni,'pass':newpass}
    usuarios_registrados=db.keys()
    print(usuarios_registrados)
    return render_template('index.html')

@app.route('/historial')
def historial():
    if 'uname' in session:
        if 'historial' in session:
            uname = session['uname']
            historial = session['historial']

            return render_template('historial.html',uname=uname, historial = historial )

@app.route('/datos')
def dates():
    if 'uname' in session:

        uname = session['uname']
        apellido = db[uname]['Apellido']
        dni = db[uname]['DNI']

        return render_template('login.html', historial=historial, uname = uname, apellido = apellido, dni = dni)
    else:
        return redirect('/')

@app.route('/change')
def change():
    if 'uname' in session:
        uname = session['uname']
        return render_template('change.html', uname = uname)
    else:
        return redirect('/')

@app.route('/cambio',methods=["POST"])
def cambio():

    uname = session['uname'] #Old name
    name=request.form.get('new_uname') #New name

    datos = db[uname]
    print (datos)
    db[name] = datos
    del db[uname]
    session['uname'] = name

    apellido = db[name]['Apellido']
    dni = db[name]['DNI']
    return render_template('login.html', uname = name, apellido = apellido, dni = dni )

@app.route('/showRestaurants', methods=["POST"])
def mostrar():
    rest_search=request.form.get('rest_search') #New name
    coleccion= collectionMongo.find_one({'name':rest_search})

    return render_template('menu1.html' , collection = coleccion)

@app.route('/modifyRestaurants', methods=["POST"])
def modificarRestaurant():
    old_name=request.form.get('old_name') #Old name
    new_name=request.form.get('new_name') #New name

    #myquery ={'name':old_name}
    print (collectionMongo.update( {'name':old_name} , {"$set": {'name':new_name}} ))

    coleccion= collectionMongo.find_one({'name':new_name})

    return render_template('menu1.html' , collection = coleccion)

@app.errorhandler(404)
def pagenotfound(error):
    return "This page not found",404
#http://0.0.0.0:5000/<CualquierOtraPagina>

#Ejercicio 5


if __name__ == "__main__":
  app.secret_key = os.urandom(24)
  app.run(debug = True, host='0.0.0.0')
