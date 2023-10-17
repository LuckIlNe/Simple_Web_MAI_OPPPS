from sqlalchemy import (
    MetaData, Table, Column, ForeignKey, Float,
    Integer, String, Identity, Enum, Date
)

from sqlalchemy.ext.declarative import declarative_base
import enum
from sqlalchemy.dialects.postgresql import ARRAY

Base = declarative_base()
metadata = Base.metadata

class Articles(Base):

    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    title = Column(String, nullable=False, unique=True)
    source = Column(String, nullable=False, unique=True)
    text = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    capacity = Column(String, nullable=False)
    authors = Column(ARRAY(String), nullable=False)
    categories = Column(ARRAY(String), nullable=False)

    def __repr__(self):
        return "<Article id=%s >" % self.id