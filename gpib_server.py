from flask import Flask
from flask_restful import Resource, Api
from GpibRegister import GpibRegister

gpip_register = GpibRegister()

app = Flask(__name__)
api = Api(app)


class GpibRegisterApi(Resource):
    def get(self, address):
        return gpip_register.register_gpib_device(12)

api.add_resource(GpibRegisterApi, '/register/adress/<int:address>')

if __name__ == '__main__':
    app.run(debug=True)