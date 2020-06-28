from pymongo import MongoClient
conexion = MongoClient('mongodb://localhost')
db= conexion["Farmacia"]

def autenticacion(email,password):
    consulta= db["Usuarios"].find_one({"email":email})
    if consulta:
        if consulta["password"]==password:
            return True
        else: return False
    else: return False

def guardar_paciente(data):
    dbpacientes=db["Pacientes"]
    dbpacientes.insert_one(data)
    return True


def actualizardatos(cedula,edad,nivel):
    dbpacientes=db["Pacientes"]
    busqueda=dbpacientes.find_one({"cedula":cedula})
    if busqueda:
        if busqueda["cedula"]==cedula:
            dbpacientes.update_one({"cedula":cedula},{"$set":{"edad":edad}})
            dbpacientes.update_one({"cedula":cedula},{"$set":{"nivel":nivel}})
            return True
        else: return False
    else: return False

def buscarpaciente(cedula):
    dbpacientes=db["Pacientes"]
    busqueda=dbpacientes.find_one({"cedula":cedula})
    if busqueda:
        if busqueda["cedula"]==cedula:
            dbpacientes.delete_one({"cedula":cedula})
            return True
        else: return False
    else: return False


