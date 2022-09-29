from fastapi import FastAPI, APIRouter
import uvicorn

user_router = APIRouter(prefix='/users')
order_router = APIRouter(prefix='/orders')

@user_router.get('/',tags=['users'])
def read_users():
    return [dict(user_name='Rick'), dict(user_name='Morty')]


@user_router.get('/me', tags=['users'])
def read_user_me():
    return dict(user_name='ok chang won')

@order_router.get('/', tags=['orders'])
def read_orders():
    return [dict(order='face'), dict(order='burrito')]
    
@order_router.get('./me', tags=['orders'])
def read_order_me():
    return dict(my_order='taco')

@order_router.get('/{order_id}', tags=['orders'])
def read_order_id(order_id:str):
    return dict(order_id=order_id)

app = FastAPI()

if __name__ == '__main__':
    app.include_router(user_router)
    app.include_router(order_router)
    uvicorn.run(app, host='0.0.0.0', port=8000)