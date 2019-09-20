'''
Created on 11 lug 2019
per lancio server

D:\Eclipse\java-neon\workspace\flask-project\flask-tutorial>python waitress_server.py

@author: g.fontana
'''
from waitress import serve
import  mainapp
 
serve(mainapp.app, host='0.0.0.0', port=8080)