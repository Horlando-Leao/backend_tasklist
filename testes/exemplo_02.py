from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pprint import pprint
engine = create_engine('sqlite:///test.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Pessoa(Base):

    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

    def __repr__(self):
        return f'Pessoa(id={self.id}, nome={self.nome}, idade={self.idade})'


Base.metadata.create_all(engine)


p1 = Pessoa(nome='Fausto', idade=21)
p2 = Pessoa(nome='Fabio', idade=22)
p3 = Pessoa(nome='Fernando', idade=26)

session.add_all([p1, p2, p3])
session.commit()

pprint(session.query(Pessoa).all())
pprint(session.query(Pessoa).first())
pprint(session.query(Pessoa).query(nome='Fausto'))

