from werkzeug.security import check_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def __init__(sel, id, nombre, correo, clave, fechaReg, perfil) -> None:
        sel.id         = id
        sel.nombre     = nombre
        sel.correo     = correo
        sel.clave      = clave
        sel.fechaReg   = fechaReg
        sel.perfil     = perfil
    @classmethod
    def ValidarClave(sel, claveCifrada, clave):
        return check_password_hash(claveCifrada, clave)