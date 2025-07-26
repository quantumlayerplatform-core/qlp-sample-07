from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from models.user import Base

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    Base.metadata.create_all(bind=engine)

def drop_tables():
    Base.metadata.drop_all(bind=engine)

if __name__ == "__main__":
    create_tables()