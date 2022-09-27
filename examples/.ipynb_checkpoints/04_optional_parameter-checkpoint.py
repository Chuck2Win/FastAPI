from fastapi import FastAPI
import uvicorn
from typing import Optional

app = FastAPI()

fake_items_db = [dict(item_name='Foo'),dict(item_name='bar'), dict(item_name='Baz')]

@app.get('/items/{item_id}')
def read_item(item_id:str, q:Optional[str]=None):
    if q:
        return dict(item_id=item_id, q=q)
    return dict(item_id=item_id)
@app.get('/items')
def read_item2(item_id:str, q:Optional[str]=None):
    if q:
        return dict(item_id=item_id, q=q)
    return dict(item_id=item_id)


if __name__ == '__main__':
	uvicorn.run(app, host='0.0.0.0', port = 8000)
