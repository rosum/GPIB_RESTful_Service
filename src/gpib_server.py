from flask import Flask, request
from flask_restplus import Resource, Api
from GpibService import GpibService

gpip_service = GpibService()

app = Flask(__name__)
api = Api(app)


class GpibRegisterApi(Resource):

    def post(self, adress):
        return gpip_service.register_gpib_device(adress)

    def delete(self, adress):
        return gpip_service.purge_gpib_device(adress)



class GpibQueryApi(Resource):

    def get(self, adress):
        return gpip_service.read_gpib(adress)

    def post(self, adress):
        query = request.args.get('q')
        return gpip_service.gpib_write_read(adress, query)

    def put(self, adress):
        query = request.args.get('q')
        return gpip_service.write_gpib(adress, query)



api.add_resource(GpibRegisterApi, '/instrument/register/adress/<int:adress>')
api.add_resource(GpibQueryApi, '/instrument/adress/<int:adress>')

if __name__ == '__main__':
    app.run(debug=True)