# post - body에 정보를 넣어서 보낸다.
# get - header에만 정보를 넣어서 보냄
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates # front end 구성
import uvicorn
from typing import Optional


app = FastAPI()
templates = Jinja2Templates(directory='./')

@app.get('/login/') # 이 부분은 get인지라.. 안된다. # 순서가 localhost:8000/login -> html 띄우고. -> Request로 채워서 -> submit을 누르면 login 함수가 실행됨.-> post
def get_login_form(request:Request):
    return templates.TemplateResponse('login_form.html', context={'request':request}) # 해당 html로 data를 보냄.
    
@app.post('/login/') # 이 부분은 get인지라.. 안된다.
def login(user_name:str = Form(...), password:str = Form(...)):
    return dict(user_name=user_name)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0',port=8000)