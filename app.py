from fastapi import FastAPI,Request
import products
from dtos import ProductDTO

app = FastAPI()


@app.get("/")
def home():
    return {'hello':"world"}

@app.get("/products")
def printproducts():
    return products.products

## path parameter
@app.get("/product/{product_id}")
def single_product(product_id:int):
    for pro in products.products:
        if pro.get('sno')==product_id:
            return {
                    product_id:pro
                }
    return {
        product_id:"not found"
    }

## query params without request
@app.get("/query")
def questionans(name:str, age:int):
    return f"hi {age} ur age is {name}"

## query params with request 
@app.get("/greet")
def greetuser(request:Request):
    requested_dict = dict(request.query_params)
    return f"hi {requested_dict.get('age')} fuck off {requested_dict.get('name')} "
## usefull only we start models

## post method
@app.post("/createaproduct")
def new_product(body:ProductDTO):
    print(body)
    return {"message":"new product created succesfully"}