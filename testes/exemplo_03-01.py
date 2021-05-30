from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from pprint import pprint
from env import environments

# engine = create_engine('sqlite:///test.db', echo=True)

engine = create_engine(f'mysql+mysqlconnector://{environments("USUARIOBANCO")}:{environments("SENHABANCO")}@'
                       f'{environments("ENDERECOBANCO")}:{environments("PORTABANCO")}/'
                       f'{environments("BASEDADOSMYSQL")}', echo=True)

# mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


for x in mybases:
    print(x)

#
# class Produto(Base):
#
#     __tablename__ = 'produtos'
#     id = Column(Integer, primary_key=True)
#     nome = Column(String(100))
#     preco = Column(Float)
#     pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
#     pessoa = relationship('Pessoa')
#
#     def __repr__(self):
#         return f'Produto(id={self.id}, nome={self.nome}, preco={self.preco}, pessoa={self.pessoa_id})'
#
# print("minhas bases=> ", mybases[0])
#
#
# class Pessoa(Base):
#     __tablename__ = 'pessoas'
#     id = Column(Integer, primary_key=True)
#     nome = Column(String(100))
#     idade = Column(Integer)
#
#     produtos = relationship(Produto, backref='pessoas')
#
#     def __repr__(self):
#         return f'Pessoa(id={self.id}, nome={self.nome}, idade={self.idade})'
#
#
# Base.metadata.create_all(engine)
#
# p1 = Pessoa(nome='Carlos', idade=21)
# pd1 = Produto(nome='livro', preco=100.00, pessoa=p1)
# session.add_all([p1, pd1])
#
# p2 = Pessoa(nome='João', idade=21)
# pd2 = Produto(nome='jogo', preco=250.00, pessoa=p2)
# session.add_all([p2, pd2])
#
# p3 = Pessoa(nome='Lucas', idade=21)
# pd3 = Produto(nome='livro', preco=100.00, pessoa=p3)
# pd4 = Produto(nome='jogo', preco=250.00, pessoa=p3)
# session.add_all([p3, pd3, pd4])
#
# session.commit()
#
# pprint(session.query(Pessoa).all())
# pprint(session.query(Produto).all())
# print(session.query(Produto).filter(Pessoa.nome == 'Fausto').all())
# print(session.query(Produto).filter_by(nome='livro').filter(Pessoa.nome == 'Fausto').all())
# print(session.query(Produto).filter_by(nome='livro').filter(Pessoa.nome == 'Carlos').all())
# print(session.query(Pessoa).filter(Produto.nome == 'livro').filter_by(nome='João').all())
