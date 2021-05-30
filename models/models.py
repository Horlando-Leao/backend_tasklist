from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import relationship

Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), unique=False)
    email = Column(String(120), unique=True)
    password = Column(String(120), unique=False)

    def __repr__(self):
        return f'User(nome = {self.name})'
