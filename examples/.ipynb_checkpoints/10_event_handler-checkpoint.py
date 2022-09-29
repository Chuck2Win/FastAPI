from fastapi import FastAPI
import uvicorn
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_hander = logging.StreamHandler()    
logger.addHandler(stream_hander)

app = FastAPI()

items = {}

@app.on_event('startup')
def startup_event():
    logger.info('startup event')
    items['foo']=dict(name='fighters')
    items['bar']=dict(name='tenders')
@app.on_event('shutdown')
def shudown_event():
    logger.info('shutdown event')
    
@app.get('/items/{item_id}')
def read_items(item_id:str):
    return items[item_id]

if __name__=='__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)