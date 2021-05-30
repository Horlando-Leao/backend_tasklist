from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///test.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Pessoa(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String)


Base.metadata.create_all(engine)


p1 = Pessoa(nome='Fausto')
p2 = Pessoa(nome='Fabio')
p3 = Pessoa(nome='Fernando')
p4 = Pessoa(nome='Osvaldo')

session.add_all([p1, p2, p3])
session.commit()

session.add(p4)
session.flush() #limpar a sessão
