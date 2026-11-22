from pydantic import BaseModel

class ProductDTO(BaseModel):
    sno : int
    name : str
    price : int = 0