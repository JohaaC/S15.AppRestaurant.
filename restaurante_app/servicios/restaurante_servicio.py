from pathlib import Path

from servicios.archivo_servicio import (
    ArchivoServicio
)

from modelos.venta import Venta


class RestauranteServicio:

    def __init__(self):

        base_dir = Path(__file__).resolve().parent.parent

        self.ruta_productos = (
            base_dir / "datos" / "productos.json"
        )

        self.ruta_usuarios = (
            base_dir / "datos" / "usuarios.json"
        )

        self.ruta_ventas = (
            base_dir / "datos" / "ventas.json"
        )

        self.archivo_servicio = ArchivoServicio()

    # =====================================
    # USUARIOS
    # =====================================

    def obtener_usuarios(self):

        return self.archivo_servicio.leer_json(
            self.ruta_usuarios
        )

    def validar_usuario(
        self,
        usuario,
        contraseña
    ):

        usuarios = self.obtener_usuarios()

        for usuario_data in usuarios:

            if (
                usuario_data.get("usuario") == usuario
                and
                usuario_data.get("contraseña") == contraseña
            ):

                return True

        return False

    # =====================================
    # PRODUCTOS
    # =====================================

    def obtener_productos(self):

        return self.archivo_servicio.leer_json(
            self.ruta_productos
        )

    def guardar_productos(
        self,
        productos
    ):

        return self.archivo_servicio.guardar_json(
            self.ruta_productos,
            productos
        )

    def obtener_siguiente_id(self):

        productos = self.obtener_productos()

        if not productos:

            return 1

        ids = [
            producto.get("id", 0)
            for producto in productos
        ]

        return max(ids) + 1

    def registrar_producto(
        self,
        nombre,
        categoria,
        precio,
        cantidad
    ):

        productos = self.obtener_productos()

        nuevo_producto = {
            "id": self.obtener_siguiente_id(),
            "nombre": nombre,
            "categoria": categoria,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }

        productos.append(
            nuevo_producto
        )

        self.guardar_productos(
            productos
        )

        return nuevo_producto

    def actualizar_producto(
        self,
        id_producto,
        nombre,
        categoria,
        precio,
        cantidad
    ):

        productos = self.obtener_productos()

        for producto in productos:

            if producto.get("id") == id_producto:

                producto["nombre"] = nombre
                producto["categoria"] = categoria
                producto["precio"] = float(precio)
                producto["cantidad"] = int(cantidad)

                self.guardar_productos(
                    productos
                )

                return True

        return False

    def eliminar_producto(
        self,
        id_producto
    ):

        productos = self.obtener_productos()

        productos_actualizados = [
            producto
            for producto in productos
            if producto.get("id") != id_producto
        ]

        if (
            len(productos_actualizados)
            ==
            len(productos)
        ):

            return False

        self.guardar_productos(
            productos_actualizados
        )

        return True

    # =====================================
    # VENTAS
    # =====================================

    def obtener_ventas(self):

        return self.archivo_servicio.leer_json(
            self.ruta_ventas
        )

    def guardar_ventas(
        self,
        ventas
    ):

        return self.archivo_servicio.guardar_json(
            self.ruta_ventas,
            ventas
        )

    def registrar_venta(
        self,
        usuario,
        producto_id
    ):

        usuarios = self.obtener_usuarios()

        productos = self.obtener_productos()

        ventas = self.obtener_ventas()

        # ---------------------------------
        # VALIDAR USUARIO
        # ---------------------------------

        usuario_encontrado = None

        for usuario_data in usuarios:

            if (
                usuario_data.get("usuario")
                ==
                usuario
            ):

                usuario_encontrado = (
                    usuario_data
                )

                break

        if usuario_encontrado is None:

            return (
                False,
                "El usuario seleccionado no existe."
            )

        # ---------------------------------
        # VALIDAR PRODUCTO
        # ---------------------------------

        producto_encontrado = None

        for producto in productos:

            if (
                producto.get("id")
                ==
                producto_id
            ):

                producto_encontrado = producto

                break

        if producto_encontrado is None:

            return (
                False,
                "El producto seleccionado no existe."
            )

        # ---------------------------------
        # VALIDAR CANTIDAD DISPONIBLE
        # ---------------------------------

        cantidad = producto_encontrado.get(
            "cantidad",
            0
        )

        if cantidad <= 0:

            return (
                False,
                "El producto no tiene stock disponible."
            )

        # ---------------------------------
        # CREAR VENTA
        # ---------------------------------

        nueva_venta = Venta(
            usuario,
            producto_id
        )

        ventas.append(
            nueva_venta.to_dict()
        )

        # ---------------------------------
        # REDUCIR CANTIDAD
        # ---------------------------------

        producto_encontrado["cantidad"] = (
            cantidad - 1
        )

        # ---------------------------------
        # GUARDAR INFORMACIÓN
        # ---------------------------------

        ventas_guardadas = self.guardar_ventas(
            ventas
        )

        productos_guardados = self.guardar_productos(
            productos
        )

        if (
            not ventas_guardadas
            or
            not productos_guardados
        ):

            return (
                False,
                "No se pudo guardar la venta."
            )

        return (
            True,
            "Venta registrada correctamente."
        )