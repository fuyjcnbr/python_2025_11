from dataclasses import dataclass, field
from typing import List

@dataclass
class Product:
    id: int or None
    name: str
    quantity: int
    price: float

@dataclass
class Order:
    id: int or None
    products: List[Product] = field(default_factory=list)

    def add_product(self, product: Product):
        self.products.append(product)
