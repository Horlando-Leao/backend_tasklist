from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from env import environments


def init_db():
    from sqlalchemy.ext.declarative import declarative_base
    engine = create_engine(f'mysql+mysqlconnector://'
                           f'{environments("USUARIOBANCO")}:{environments("SENHABANCO")}@'
                           f'{environments("ENDERECOBANCO")}:{environments("PORTABANCO")}/'
                           f'{environments("BASEDADOSMYSQL")}', echo=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    Base = declarative_base()

    import models.models

    Base.metadata.create_all(bind=engine)

