from sqlalchemy.orm.session import Session

from domain.unit_of_work import UnitOfWork
from domain.exceptions import DomainException

class SqlAlchemyUnitOfWork(UnitOfWork):

    def __init__(self, session: Session):
        self.session = session

    def __enter__(self):
        self.session.begin()

    def __exit__(self, exception_type, exception_value, traceback):
        if exception_type == DomainException:
            print(f"""exception: type={exception_type};
                value={exception_value},
                traceback={traceback}
            """)

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
