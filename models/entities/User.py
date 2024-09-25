from werkzeug.security import check_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, nombre, correo, clave, fechareg, perfil) -> None:
        self.id             = id
        self.nombre         = nombre
        self.correo         = correo
        self.clave          = clave
        self.fechareg       =fechareg
        self.perfil         =perfil
    @classmethod
    def ValidarClave(self, ClaveCifrada, clave):
        return check_password_hash(ClaveCifrada, clave)