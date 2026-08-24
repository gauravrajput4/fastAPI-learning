from sqlalchemy import Column,Text, Integer, String, DateTime, Boolean, ForeignKey
from database import Base

# Blog Table
class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(Text)