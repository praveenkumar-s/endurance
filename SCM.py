from flask import Blueprint, render_template
from flask import request
import os
import requests
import firebaseClient as FBC
firebaseInstance=FBC.firebase_client()

SCM_blueprint = Blueprint('SCM', __name__)

@SCM_blueprint.route("/<data_source>/exclude/<job_name>", methods =['GET'])
def exclude(data_source,job_name):
    try:
        token = request.args.get('token')
        if(not token==os.environ.get('SCM_token')):
            return "unauthorized =",403
        
        existing_data = firebaseInstance.getdata(data_source)   
        existing_data['exclusion']['job_names'].append(job_name)
        firebaseInstance.putvalue(child=data_source,data=existing_data)
        return "OK",200
    except:
        return "Unable to Complete transaction",500

    