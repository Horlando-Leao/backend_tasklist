from pprint import pprint

from database.database import session_conn
from models.models import Usuario


# noinspection PyMethodMayBeStatic
class OperationsUsuarios:
    """"Classe de operações básicas de usuários"""

    def add(self, nome: str = None, email: str = None, password: str = None) -> None:
        session = session_conn()
        p1 = Usuario(nome=nome, email=email, password=password)
        session.add_all([p1])
        session.commit()

    def delete(self, value: str) -> bool:
        """"Só pode ser deletado por email
        :rtype: boolgi
        """

        session = session_conn()
        result = session.query(Usuario).filter_by(email=value).delete()
        session.commit()
        if result > 0:
            return True
        else:
            return False

    def find_nome(self, value: str) -> str:
        session = session_conn()
        return session.query(Usuario).filter(Usuario.nome == value).all()

    def like_nome(self, value: str) -> str:
        session = session_conn()
        search = "%{}%".format(value)
        return session.query(Usuario).filter(Usuario.nome.like(search)).all()

    def find_email(self, value: str) -> str:
        session = session_conn()
        return session.query(Usuario).filter_by(email=value).all()

    def like_email(self, value: str) -> str:
        session = session_conn()
        search = "%{}%".format(value)
        return session.query(Usuario).filter(Usuario.email.like(search)).all()

    def update_nome(self, email: str, new_value: str) -> bool:
        session = session_conn()
        result = session.query(Usuario).filter_by(email=email).update({'nome': new_value})
        session.commit()
        if result > 0:
            return True
        else:
            return False
        session.commit()
