from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from env import environments


def session_conn():
    engine = create_engine(f'mysql+mysqlconnector://'
                           f'{environments("USUARIOBANCO")}:{environments("SENHABANCO")}@'
                           f'{environments("ENDERECOBANCO")}:{environments("PORTABANCO")}/'
                           f'{environments("BASEDADOSMYSQL")}', echo=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    return session
