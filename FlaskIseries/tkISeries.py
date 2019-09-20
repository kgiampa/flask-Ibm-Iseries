'''
Created on 07 mag 2018

@author: GianpieroF
'''
import pypyodbc
from datetime import date, timedelta
 
class tkISeries():
     
    def __init__(self):
        super(tkISeries, self).__init__()
        
    def connection(self):
        #python=user profile created on iseries
        connection = pypyodbc.connect(driver='{iSeries Access ODBC Driver}',
                        system='indirizzo_ip',uid='PYTHON',pwd='PYTHON')
        self.c1 = connection.cursor()
        print ("cursor")
           
      
    def selectBolle(self,c1):
        # libreria = library iseries
        # file =table iseries
        dataric = date.today() - timedelta(5)
        data1 = dataric.strftime('%y%m%d')
        stringa=("select  (bfili concat   banno concat   bnume), bporto, "+
        "(substr(CAST(bdatab AS char(6)),5,2)" +
        "concat '/' concat substr(CAST(bdatab AS char(6)),3,2) concat '/' "+
        "concat substr(CAST(bdatab AS char(6)),1,2))  data, " +
        "bmrag, bmind, bdrag, bdind,BRIFMI, bpeso, bwolu , BCOLLI from libreria.file "+ 
                " where bdatab>= " + data1 +   " and bicdat=0  ")
        
        try:
            c1.execute(stringa) 
            row = c1.fetchall()
        except Exception as e:
            print ("error")
         
        return row
    def selectBolleDate(self,c1, dateBolle):
         
        stringa=("select  (bfili concat   banno concat   bnume), bporto," +
         "(substr(CAST(bdatab AS char(6)),5,2)" +
        "concat '/' concat substr(CAST(bdatab AS char(6)),3,2) concat '/' "+
        "concat substr(CAST(bdatab AS char(6)),1,2)) data, " +
        " bmrag, bmind, bdrag, bdind,BRIFMI, bpeso, bwolu, BCOLLI from libreria.file" + 
        " where bdatab>= " + dateBolle +   " and bicdat=0  ")
       
        try:
            c1.execute(stringa) 
            row = c1.fetchall()
        except Exception as e:
            print ("error")
         
        return row
    def updateBolle(self,c1, key):
        x = date.today()
         
         
        data_consegna=x.strftime("%y")+x.strftime("%m")+x.strftime("%d")
        
        anno=key[1] 
        nume=key[2:7]
         
        stringa=("update traspedat.bolle00f set bicdat = " + data_consegna + ","+
                 " bicaut='  1', bicgir='  1', bicnum=1 " +
                " where banno=" + anno + " and bfili=1 and   bnume = " +nume+ "")
        val= (anno, nume)
       
        c1.execute(stringa) 
        c1.commit()
          
            
                 
    