from flask import Flask, request,jsonify
from pymongo import MongoClient
from bdfarmacia import *
from bson.json_util import dumps

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def login():
    if request.method=="POST":
        email= request.form["email"]
        password= request.form["password"]
        retorno=loginvalidate(email,password)
        if retorno:
            return "Usuario valido, ir a la ventana principal"
        else:
            return "Usuario incorrecto, vuelva a ingresar los datos"
    return "PAGINA PRINCIPAL: Login"

def loginvalidate(email,password):
    return autenticacion(email,password)

@app.route("/lista-pacientes", methods=["GET","POST"])
def listadopacientes():
    if request.method=="GET":
        dbpacientes=db["Pacientes"]
        listado=dumps(dbpacientes.find())
    return jsonify(listado)

@app.route("/lista-pacientes/agregar", methods=["GET","POST"])
def crearpaciente(): 
    if request.method=="POST":
        cedula= request.form["cedula"]
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        edad = request.form["edad"]
        nivel = request.form["nivel"]
        data= {"cedula":cedula,"nombre":nombre,"apellido":apellido,"edad":edad,"nivel":nivel}
        guardar=guardar_paciente(data)
        if guardar:
            return"El paciente ha sido agregado de manera correcta" 
    return "PAGINA PACIENTES: Añadir pacientes"

@app.route("/lista-pacientes/actualizar", methods=["GET","PUT"])
def actualizarpaciente():
    if request.method=="PUT":
        cedula=request.form["cedula"]
        edad=request.form["edad"]
        nivel=request.form["nivel"]
        actualizar = actualizardatos(cedula,edad,nivel)
        if actualizar:
            return "El paciente ha sido actualizado"
        else:
            return "El paciente no existe."
    return "PAGINA PACIENTES: Actualizar pacientes"

@app.route("/lista-pacientes/eliminar", methods=["GET","DELETE"])
def eliminarpaciente():
    if request.method=="DELETE":
        cedula=request.form["cedula"]
        eliminar= buscarpaciente(cedula)
        if eliminar:
            return "El paciente ha sido eliminado exitosamente."
        else:
            return "El paciente no existe."
    return "PAGINA PACIENTES: Eliminar pacientes"

@app.route("/lista-medicamentos", methods=["GET"])
def listadomedicamentos():
    if request.method=="GET":
        dbmedicamentos=db["Medicamentos"]
        listado=dumps(dbmedicamentos.find())
    return jsonify(listado)

if __name__ == "__main__":
    app.run(debug=True,port=4300)
