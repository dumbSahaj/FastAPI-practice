from fastapi import FastAPI
import products

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
        if pro.get('id')==product_id:
            return {
                    product_id:pro
                }
    return {
        product_id:"not found"
    }