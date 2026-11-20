from fastapi import FastAPI
import products

app = FastAPI()


@app.get("/")
def home():
    return {'hello':"world"}

@app.get("/products")
def printproducts():
    return products.products