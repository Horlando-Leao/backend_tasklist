from pprint import pprint

from flask import Flask
from controllers.operations_usuarios import OperationsUsuarios
from models.models import Usuario
app = Flask(__name__)

opera_usuarios = OperationsUsuarios()

#opera_usuarios.add()
#opera_usuarios.find_nome('horlando')
#opera_usuarios.like_nome('le')

# new_var = opera_usuarios.find_email('joseleao@.com')
# pprint(new_var[0])

#opera_usuarios.delete('teste@.com')

#opera_usuarios.update_nome('leaoleao@.com', 'Horlando Leão')

