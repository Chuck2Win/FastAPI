from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/items/{item_id}')
def create_item(item_id:str):
    return dict(item=item_id)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0',port=8000)