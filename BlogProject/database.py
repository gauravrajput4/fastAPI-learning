from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL="postgresql://apple:root123@localhost/blogdb"

engine = create_engine(DATABASE_URL)

SessionLocal=sessionmaker(bind=engine)

Base = declarative_base()
