from flask import Flask, render_template
from flask import request
 
from datetime import date, timedelta
#from flask_bootstrap import Bootstrap
from tkISeries import tkISeries 
 
app = Flask(__name__)

 

@app.route('/')
def hello():
    return render_template('/azienda.html')

@app.route('/base', methods=('GET', 'POST'))
def bolle():
    if request.method == 'POST':
        data = request.form 
        #print ("request")
        #print (data) 
        print (request.form.to_dict())
        
        print (type(request.form.to_dict())) 
        data =request.form.to_dict()
        iseries=tkISeries()
        iseries.connection()
        for key, value in data.items():
            if value=='on':
                
                iseries.updateBolle(iseries.c1,key)
                print (value)
                print (key)
            #if key=='date' and value:
                #print ("dateeeee")
                #print (value)
                #if not value:
                #     
                #    value = date.today().strftime('%y%m%d')
                #print (value)
                #data=value
                #dataupd=data[-2:]+data[2:-2]+data[:2]
                #dataupd=dataupd+data[3:4] 
                #print (dataupd)
                 
                #rows=iseries.selectBolleDate(iseries.c1, dataupd)
                 
    if request.method != 'POST':
        iseries=tkISeries()
        iseries.connection()
        #iseries.c1.execute("{CALL GRK80OBJ.PCCLA1}") 
        rows=iseries.selectBolle(iseries.c1)
    if request.method == 'POST':
        data =request.form.to_dict()
        iseries=tkISeries()
        iseries.connection()
        dataric = date.today() - timedelta(5)
        
        dataupd = dataric.strftime('%y%m%d')
        
        for key, value in data.items():
            if key=='date' and value:
                print (value)
                print (key)
                data=value
                dataupd=data[-2:]+data[2:-2]+data[:2]
        rows=iseries.selectBolleDate(iseries.c1, dataupd)
    
    return render_template('/base.html', len = len(rows), lenr = len(rows[0]), rows=rows)

@app.route('/dati', methods=('GET', 'POST'))
 
def parse_request():
    if request.method == 'GET':
        data = request.data  
        print ("request")
        print (data)
        
 