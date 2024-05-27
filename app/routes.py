from flask_restful import Resource
#El modulo request nos permite aceptar info de un usuario
from flask import request

lista_objetos_almacen = ['Lapiz', 'Goma', 'Tijeras']

class HelloWorld(Resource):
    def get(self):
        #Regresamos un diccionario con el mensaje que queremos mostrar
        return { 'message': 'HOLA MUNDO DESDE LA API', 'status':200}
    
class Almacen(Resource):
    def get(self):
        return{ 'Objetos': lista_objetos_almacen, 'status': 200}
    
    def post(self):
        #Se crea una nueva variable para guardar la info que posteo el usuario
        data = request.get_json()

        #Agregamos la informacion a la lista del almacen
        lista_objetos_almacen.append(data)

        return{ 'received': True, 'info': data, 'status': 200}


#Creamos una clase que va a manejar todas las rutas 
class APIRoutes:
    def init_routes(self, api):
        api.add_resource(HelloWorld, '/')

        api.add_resource(Almacen, '/objetos_almacen')