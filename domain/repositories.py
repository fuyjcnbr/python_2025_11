from abc import ABC, abstractmethod
from typing import List
from .models import Product, Order

class ProductRepository(ABC):
    @abstractmethod
    def add(self, product: Product) -> Product:
        pass

    @abstractmethod
    def get(self, product_id: int) -> Product:
        pass

    @abstractmethod
    def list(self) -> List[Product]:
        pass

class OrderRepository(ABC):
    @abstractmethod
    def add(self, order: Order) -> Order:
        pass

    @abstractmethod
    def get(self, order_id: int) -> Order:
        pass

    @abstractmethod
    def list(self) -> List[Order]:
        pass
