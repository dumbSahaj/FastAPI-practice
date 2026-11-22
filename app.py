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
    dictbody = body.model_dump()
    products.products.append(dictbody)
    return {"message":"new product created succesfully","new data":products.products}

## put method used to update 
@app.put("/update_product/{which_id}")
def updatestuff(body: ProductDTO, which_id: int):
    new_product_details = body.model_dump()
    for i,product in enumerate(products.products):
        if product.get("sno") == which_id:
            products.products[i] = new_product_details
            return {"message":"product updated success","products":products.products}
    return {"message":"gadbad"}

## delete a product
@app.delete("/delete/{which_id}")
def deletepro(which_id:int):
    for i,product in enumerate(products.products):
        if product.get("sno") == which_id:
            products.products.pop(i)
            return {"message":"product deleted","products":products.products}
    return {"message":"gadbad"}

## crud operations done