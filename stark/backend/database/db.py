from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./stark.db'
# SQLALCHEMY_DATABASE_URL = 'postgresql://user:password@postgresserver/db'

engine = create_engine(
    # connect_args parameter is used only for sqlite
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
