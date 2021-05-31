from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), unique=False)
    email = Column(String(120), unique=True)
    password = Column(String(120), unique=False)

    def __repr__(self):
        return f'User(id={self.id}, nome={self.nome}, email={self.email}, password={self.password})'
