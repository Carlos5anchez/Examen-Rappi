
import config as DBConnection
from fastapi import FastAPI,HTTPException
import requests
from datetime import datetime
app = FastAPI()

@app.post("/buro")
def buro(iduser):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    isUser = requests.get('http://192.168.1.73:3001/isUser?idUser='+iduser)

    if isUser.status_code!=200:
        raise HTTPException(status_code=404, detail="User not found")
    con=DBConnection.initConectionBuro()
    cur = con.cursor()
    query='''SELECT idburo, iduser, puntualidad, deudaspagadas, deudasvencidas, retiroefectivo, reportes, puntaje
	        FROM public.buro WHERE puntualidad=True AND deudaspagadas>deudasvencidas AND retiroefectivo::decimal>10000 AND reportes=0 AND puntaje>50 AND iduser = {} '''.format(iduser)
    cur.execute(query)
    rows = cur.fetchall()
    con.commit()
    con.close()
    if len(rows)>0:
        return True
    
    raise HTTPException(status_code=500, detail="SERVER Error")    
