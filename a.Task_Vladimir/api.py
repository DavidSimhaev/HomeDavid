#authbind --deep python3 main.py
from multiprocessing import freeze_support
from pprint import pprint
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status, Response
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from dbhelp import DataHelp
import uvicorn

app = FastAPI()
security = HTTPBasic()


@app.get("/users/me")
async def read_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)],response: Response):
    response.headers["content-type"] = 'application/json; charset=utf-8'
    print(credentials.username,credentials.password)
    base = DataHelp(host='xxxxxxxx', user='xxx', password='xxxx', database='APIElsen', datatable='`ОтчетПоПродажамElsen`')
    return {base.datatable: base.read_all_data()}

if __name__ == '__main__': 
    freeze_support()
    uvicorn.run("main:app", port=80, host='0.0.0.0', reload = True)
    #uvicorn.run("main:app", port=443, host='0.0.0.0', reload = True,  ssl_keyfile="key.pem", ssl_certfile="cert.pem")