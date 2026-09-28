from datetime import datetime


class Venta:

    def __init__(
        self,
        usuario,
        producto_id,
        fecha=None
    ):

        self.usuario = usuario
        self.producto_id = producto_id

        if fecha is None:

            self.fecha = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        else:

            self.fecha = fecha

    def to_dict(self):

        return {
            "usuario": self.usuario,
            "producto_id": self.producto_id,
            "fecha": self.fecha
        }