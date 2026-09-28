class Usuario:

    def __init__(
        self,
        usuario,
        nombre,
        contraseña
    ):

        self.usuario = usuario
        self.nombre = nombre
        self.contraseña = contraseña

    def to_dict(self):

        return {
            "usuario": self.usuario,
            "nombre": self.nombre,
            "contraseña": self.contraseña
        }