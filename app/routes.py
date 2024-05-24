from flask_restful import Resource

class HelloWorld(Resource):
    def get(self):
        return {message: 'HOLA MUNDO DESDE LA API', status:200}
    
class APIRoutes:
    def init_routes(self, api):
        api.add_resource(HelloWorld, '/')