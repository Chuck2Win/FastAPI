from fastapi import FastAPI
import uvicorn
# fast api 객체 설정
app = FastAPI()

# get
@app.get('/')
def read_root():
	return dict(hello='world')

if __name__ == '__main__':
	uvicorn.run(app, host = '0.0.0.0', port = 8000)
