from fastapi import FastAPI

app_users = FastAPI()

@app_users.get('/')
async def users_index():
    return {"msg": "users index"}


@app_users.get('/hello')
async def users_hello():
    return {"msg": "hello from users"}