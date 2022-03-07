
import config as DBConnection
from fastapi import FastAPI,HTTPException
app = FastAPI()

@app.get("/getCustomers")
def getCustomers():
    con=DBConnection.initConection()
    cur = con.cursor()
    cur.execute('''SELECT * FROM public."userInfo";''')
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows


@app.get("/isUser")
def isUser(idUser):
    con=DBConnection.initConection()
    cur = con.cursor()
    query='''SELECT * FROM public."userInfo" WHERE "idUsuario" = {} '''.format(idUser)
    cur.execute(query)
    rows = cur.fetchall()
    print(len(rows))
    con.commit()
    con.close()
    if len(rows)>0:
        return rows
    raise HTTPException(status_code=404, detail="User not found")    
    

