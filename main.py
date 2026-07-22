from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    name: str
    price: float


products = [
    {"id": 1, "name": "Laptop", "price": 60000},
    {"id": 2, "name": "Mouse", "price": 800}
]


@app.post("/products", status_code=201)
def create_product(product: Product):
    new_product = {
        "id": len(products) + 1,
        "name": product.name,
        "price": product.price
    }

    products.append(new_product)

    return new_product
@app.get("/products", summary="Get All Products")
def get_products():
    return products
from fastapi import HTTPException

@app.get("/products/{id}", summary="Get Product by ID")
def get_product_by_id(id: int):
    for product in products:
        if product["id"] == id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )

@app.put("/products/{id}", summary="Update Product")
def update_product(id: int, updated_product: Product):
    for product in products:
        if product["id"] == id:
            product["name"] = updated_product.name
            product["price"] = updated_product.price
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )

@app.delete("/products/{id}", summary="Delete Product", status_code=204)
def delete_product(id: int):
    for product in products:
        if product["id"] == id:
            products.remove(product)
            return

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )