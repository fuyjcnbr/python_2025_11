from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from domain.services import WarehouseService
from infrastructure.orm import Base
from infrastructure.repositories import SqlAlchemyProductRepository, SqlAlchemyOrderRepository
from infrastructure.unit_of_work import SqlAlchemyUnitOfWork
from infrastructure.database import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionFactory=sessionmaker(bind=engine)
Base.metadata.create_all(engine)

def main():
    session = SessionFactory()
    product_repo = SqlAlchemyProductRepository(session)
    order_repo = SqlAlchemyOrderRepository(session)

    uow = SqlAlchemyUnitOfWork(session)

    warehouse_service = WarehouseService(product_repo, order_repo)
    with uow:
        new_product1 = warehouse_service.create_product(name="test_product1", quantity=1, price=100)
        new_product2 = warehouse_service.create_product(name="test_product2", quantity=1, price=200)
        # uow.commit()
        print(f"created product: {new_product1}")
        print(f"created product: {new_product2}")
        new_order1 = warehouse_service.create_order(products=[new_product1, new_product2])
        # uow.commit()
        print(f"created order: {new_order1}")

if __name__ == "__main__":
    main()
