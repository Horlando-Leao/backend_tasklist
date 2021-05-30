from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from pprint import pprint
engine = create_engine('sqlite:///test.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Produto(Base):

    __tablename__ = 'Produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    preco = Column(Float)
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship('Pessoa')

    def __repr__(self):
        return f'Pessoa(id={self.id}, nome={self.nome}, preco={self.preco})'


class Pessoa(Base):

    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

    produtos = relationship(Produto, backref='pessoas')

    def __repr__(self):
        return f'Pessoa(id={self.id}, nome={self.nome}, idade={self.idade}, produtos={self.produtos})'


Base.metadata.create_all(engine)

"""
p1 = Pessoa(nome='Fausto', idade=21)
p2 = Pessoa(nome='Fabio', idade=22)
p3 = Pessoa(nome='Fernando', idade=26)


session.add_all([p1, p2, p3])
session.commit()
"""


pprint(session.query(Pessoa).first())

"""pprint(session.query(Pessoa).all())
pprint(session.query(Pessoa).first())
pprint(session.query(Pessoa).query(nome='Fausto'))
"""

