from sqlalchemy import Column, Integer, String
from app.core.db import Base

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False, index=True)
    email = Column(String(180), unique=True, nullable=False, index=True)
