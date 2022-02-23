from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1@localhost/testdb"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()