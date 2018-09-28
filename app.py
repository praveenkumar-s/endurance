from flask import Flask, request, abort
from flask_restplus import Resource, Api
import firebaseClient as FBC
from functools import wraps
import os


app = Flask(__name__)
api = Api(app)
firebaseInstance=FBC.firebase_client()
API_KEY=os.environ.get('API_KEY')

def require_appkey(view_function):
    @wraps(view_function)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        key=API_KEY
        #if request.args.get('key') and request.args.get('key') == key:
        if request.headers.get('x-api-key') and request.headers.get('x-api-key') == key:
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function


@api.route('/api/data_store/<string:data_source>')

class readDatafromFB(Resource):

    @require_appkey
    def post(self,data_source):
        payload=api.payload
        try:
            firebaseInstance.putvalue(child=data_source,data=payload)
        except:
            abort(500)
        return payload,201


    @require_appkey
    def get(self,data_source):
        return firebaseInstance.getdata(data_source)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')