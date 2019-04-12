#!${DEV_HOME}/tools/bin/python3
#--coding:utf-8

import os, pickle
from flask          import Flask, render_template, request, redirect, url_for, session, jsonify, make_response, send_file
from app.util       import init, GetData, CommonUtil, RedisSession

app = Flask(__name__)
app.session_interface = RedisSession.RedisSessionInterface()

@app.route('/', methods = ['POST', 'GET'])
@app.route('/home', methods = ['POST', 'GET'])
def home():
    init.init_session()

    return render_template(
                '/home/index.html'
              , _port   = os.environ['APP_PORT']
            )

@app.route('/carousel', methods = ['POST', 'GET'])
def carousel():
    init.init_session()

    users = GetData.get_users()

    return render_template(
                '/carousel/index.html'
              , _port   = os.environ['APP_PORT']
              , _users  = users
            )

@app.route('/cards', methods = ['POST', 'GET'])
def cards():
    init.init_session()

    users = GetData.get_users()

    return render_template(
                '/cards/index.html'
              , _port   = os.environ['APP_PORT']
              , _users  = users
            )

@app.route('/api/test', methods = ['POST', 'GET'])
def api_test():
    if request.method == 'GET' :
        param00  = request.args.get('param00', None)
        param01  = request.args.get('param01', "No Input")
    else :
        param00  = request.form.get('param00', None)
        param01  = request.form.get('param01', "No Input")

    print("[ __init__.py ] api_test() : param00[%s] param01[%s]"%(param00, param01));

    data_0 = { 
              "key0" : "data0"
            , "key1" : param00
           }

    data_1 = { 
              "key0" : "data1"
            , "key1" : param01
           }

    return jsonify( {
          "out_0" : data_0
        , "out_1" : data_1
        } )


