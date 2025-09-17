from unittest.mock import Mock
import pytest

from domain.services import WarehouseService
# from infrastructure.repositories import SqlAlchemyProductRepository, SqlAlchemyOrderRepository
from domain.repositories import ProductRepository, OrderRepository
from domain.models import Product, Order


product_examples = [
    Product(id=None, name="test_product1", quantity=1, price=100),
    Product(id=None, name="test_product2", quantity=2, price=100),
    Product(id=1, name="test_product3", quantity=1, price=300),
]

order_examples = [
    Order(id=None, products=[
        Product(id=None, name="test_product1", quantity=1, price=100),
        Product(id=None, name="test_product2", quantity=2, price=100),
    ]),
    Order(id=None, products=[
        Product(id=None, name="test_product2", quantity=2, price=100),
        Product(id=1, name="test_product3", quantity=1, price=300),
    ]),
]

@pytest.mark.parametrize(
    "product_in, product_out",
    [(x, x) for x in product_examples]
)

def test_product(product_in, product_out):
    mock_product_repository = Mock(ProductRepository)
    mock_product_repository.add.return_value = Product(
        id=1,
        name=product_in.name,
        quantity=product_in.quantity,
        price=product_in.price,
    )
    mock_product_repository.get.return_value = product_in
    mock_product_repository.list.return_value = [product_in]

    product_repo = mock_product_repository
    order_repo = None
    warehouse_service = WarehouseService(product_repo, order_repo)
    p = warehouse_service.create_product(
        name=product_in.name,
        quantity=product_in.quantity,
        price=product_in.price,
    )
    assert p.name == product_out.name
    assert p.quantity == product_out.quantity
    assert p.price == product_out.price


@pytest.mark.parametrize(
    "order_in, order_out",
    [(x, x) for x in order_examples]
)

def test_order(order_in, order_out):
    mock_order_repository = Mock(OrderRepository)
    mock_order_repository.add.return_value = Order(
        id=1,
        products=order_in.products,
    )
    mock_order_repository.get.return_value = order_in
    mock_order_repository.list.return_value = [order_in]

    product_repo = None
    order_repo = mock_order_repository
    warehouse_service = WarehouseService(product_repo, order_repo)
    o = warehouse_service.create_order(products=order_in.products)
    assert o.products == order_out.products
