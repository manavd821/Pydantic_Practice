from pydantic import BaseModel

class Product(BaseModel):
    id : int
    name : str
    price : float
    in_stock : bool = False


def main():
    product_data = {
        'id' : 101,
        "name" : "Manav",
        "price" : 1000.54,
        "in_stock" : True
    }
    p1 = Product(**product_data)
    print(p1)


if __name__ == "__main__":
    main()
