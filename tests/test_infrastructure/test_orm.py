from sqlalchemy import Integer, String, Float

from infrastructure.orm import ProductORM, OrderORM, order_product_associations


def test_product_orm():
    assert ProductORM.__tablename__ == 'products'
    assert ProductORM.__table__.columns.keys() == ["id", "name", "quantity", "price"]

    assert isinstance(ProductORM.__table__.columns["id"].type, Integer)
    assert ProductORM.__table__.columns["id"].primary_key is True
    assert ProductORM.__table__.columns["id"].nullable is False

    assert isinstance(ProductORM.__table__.columns["name"].type, String)

    assert isinstance(ProductORM.__table__.columns["quantity"].type, Integer)

    assert isinstance(ProductORM.__table__.columns["price"].type, Float)


def test_order_orm():
    assert OrderORM.__tablename__ == 'orders'
    assert OrderORM.__table__.columns.keys() == ["id"]

    assert isinstance(OrderORM.__table__.columns["id"].type, Integer)
    assert OrderORM.__table__.columns["id"].primary_key is True
    assert OrderORM.__table__.columns["id"].nullable is False


def test_order_product_associations():
    assert order_product_associations.name == 'order_product_associations'
    assert order_product_associations.columns.keys() == ["order_id", "product_id"]

    assert isinstance(order_product_associations.columns["product_id"].type, Integer)
    assert len(order_product_associations.columns["product_id"].foreign_keys) == 1
    fk = list(order_product_associations.columns["product_id"].foreign_keys)[0]
    assert fk._get_colspec() == "products.id" # pylint: disable=W0212

    assert isinstance(order_product_associations.columns["order_id"].type, Integer)
    assert len(order_product_associations.columns["order_id"].foreign_keys) == 1
    fk = list(order_product_associations.columns["order_id"].foreign_keys)[0]
    assert fk._get_colspec() == "orders.id" # pylint: disable=W0212
