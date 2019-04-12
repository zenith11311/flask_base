import os, sys, random, pickle, datetime
from flask import session

def init_session() :

    if 'cards' not in session :
        session['cards'] = pickle.dumps(list())

    if 'status' not in session :
        status = dict()
        status['logon'] = False
        session['status'] = pickle.dumps(status)
        

