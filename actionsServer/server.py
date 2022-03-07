
import config as DBConnection
from fastapi import FastAPI,HTTPException
import requests
from datetime import datetime
app = FastAPI()

@app.post("/systemAction")
def newAction(iduser,action):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    isUser = requests.get('http://192.168.1.73:3001/isUser?idUser='+iduser)

    if isUser.status_code!=200:
        raise HTTPException(status_code=404, detail="User not found")
    con=DBConnection.initConectionActions()
    cur = con.cursor()
    cur.execute('''INSERT INTO public.actions("idAction", actiondescription, date, "idUser") VALUES (default,%s,%s,%s) RETURNING *''',
                (action,dt_string,iduser,))
    rows = cur.fetchall()
    con.commit()
    con.close()
    if len(rows)>0:
        return rows
    
    raise HTTPException(status_code=500, detail="SERVER Error")    
