from flask import Flask, request
from flask_restplus import Resource, Api
import firebaseClient as FBC

app = Flask(__name__)
api = Api(app)
firebaseInstance=FBC.firebase_client()
@api.route('/api/<string:data_source>')
class readDatafromFB(Resource):
    def get(self,data_source):
        pass
        return firebaseInstance.getdata(data_source)


if __name__ == '__main__':
    app.run(debug=True)