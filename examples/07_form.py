# post - body에 정보를 넣어서 보낸다.
# get - header에만 정보를 넣어서 보냄
from fastapi import FastAPI, Form
import uvicorn
from typing import Optional


app = FastAPI()

@app.post('/login/') # 이 부분은 get인지라.. 안된다.
def login(user_name:str = Form(...), password:str = Form(...)):
    return dict(user_name=user_name)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0',port=8000)