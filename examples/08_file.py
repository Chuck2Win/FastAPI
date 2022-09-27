from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import HTMLResponse
import uvicorn
from typing import List, Optional

app = FastAPI()

@app.post('/files/') # 이 부분은 get인지라.. 안된다.
def create_files(files: List[bytes] = File(...)): # File이 복수도 되나 봄.
    return dict(file_sizes=[len(file) for file in files])

@app.post('/uploadfiles/')
def create_upload_files(files: List[UploadFile]=File(...)):
    return dict(filenames=[file.filename for file in files])

@app.get('/')
def main():
    content='''
    <body>
    <form action='/files/' enctype='multipart/form-data' method='post'>
    <input name='files' type='file' multiple>
    <input type ='submit'>
    </form>
    <form action='/uploadfiles/' enctype='multipart/form-data' method='post'>
    <input name='files' type='file' multiple>
    <input type='submit'>
    </form>
    </body>
    '''
    return HTMLResponse(content=content)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0',port=8000)