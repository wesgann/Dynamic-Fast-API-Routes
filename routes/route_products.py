from fastapi import FastAPI

app_products = FastAPI()

@app_products.get('/')
async def products_index():
    return {"msg": "products index"}


@app_products.get('/hi')
async def products_hello():
    return {"msg": "hi from products"}