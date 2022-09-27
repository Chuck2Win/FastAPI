# post - body에 정보를 넣어서 보낸다.
# get - header에만 정보를 넣어서 보냄
from fastapi import FastAPI
import uvicorn
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# pydantic으로 request body 정의
class ItemIn(BaseModel):
    name : str
    description : Optional[str] = None
    price : float
    tax : Optional[float] = None

class ItemOut(BaseModel):
    name : str
    price : float
    tax : Optional[float] = None

    
@app.post('/items/', response_model = ItemOut)
def create_item(item:ItemIn):
    return item

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0',port=8000)