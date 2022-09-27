# post - body에 정보를 넣어서 보낸다.
# get - header에만 정보를 넣어서 보냄
from fastapi import FastAPI
import uvicorn
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# pydantic으로 request body 정의
class Item(BaseModel):
    name : str
    description : Optional[str] = None
    price : float
    tax : Optional[float] = None
    
@app.post('/items/')
def create_item(item:Item):
    return item

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0',port=8000)