import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path
from PIL import Image, ImageTk


class MainView:

    def __init__(self, root, restaurante_servicio, mostrar_login):

        self.root = root
        self.servicio = restaurante_servicio
        self.mostrar_login = mostrar_login

        # =====================================
        # COLORES DE LA INTERFAZ
        # =====================================

        self.ROJO = "#8B1E1E"
        self.ROJO_OSCURO = "#651414"
        self.MOSTAZA = "#D4A017"
        self.MOSTAZA_CLARO = "#E8C547"
        self.CREMA = "#FFF8E7"
        self.BLANCO = "#FFFFFF"
        self.TEXTO = "#3B1F1F"

        # =====================================
        # CARGAR ICONOS
        # =====================================

        self.icono_producto = self.cargar_icono("producto.png")
        self.icono_usuario = self.cargar_icono("usuario.png")
        self.icono_venta = self.cargar_icono("venta.png")
        self.icono_salir = self.cargar_icono("salir.png")

        self.crear_interfaz()
        self.cargar_productos()
        self.cargar_usuarios_venta()
        self.cargar_ventas()

    # =====================================
    # CARGAR ICONOS
    # =====================================

    def cargar_icono(self, nombre, tamaño=(24, 24)):

        base_dir = Path(__file__).resolve().parent.parent
        ruta = base_dir / "assets" / nombre

        imagen = Image.open(ruta)
        imagen = imagen.resize(tamaño)

        return ImageTk.PhotoImage(imagen)

    # =====================================
    # INTERFAZ
    # =====================================

    def crear_interfaz(self):

        self.root.configure(
            bg=self.CREMA
        )

        # =====================================
        # ESTILOS
        # =====================================

        estilo = ttk.Style()

        estilo.theme_use("clam")

        # -------------------------------------
        # ETIQUETAS
        # -------------------------------------

        estilo.configure(
            "TLabel",
            font=("Segoe UI", 10),
            background=self.CREMA,
            foreground=self.TEXTO
        )

        # -------------------------------------
        # BOTONES
        # -------------------------------------

        estilo.configure(
            "TButton",
            font=("Segoe UI", 10, "bold"),
            padding=7,
            background=self.MOSTAZA,
            foreground=self.ROJO_OSCURO,
            borderwidth=0
        )

        estilo.map(
            "TButton",
            background=[
                ("active", self.MOSTAZA_CLARO),
                ("pressed", self.ROJO)
            ],
            foreground=[
                ("pressed", self.BLANCO)
            ]
        )

        # -------------------------------------
        # LABELFRAME
        # -------------------------------------

        estilo.configure(
            "TLabelframe",
            background=self.CREMA,
            bordercolor=self.ROJO,
            relief="solid"
        )

        estilo.configure(
            "TLabelframe.Label",
            font=("Georgia", 11, "bold"),
            background=self.CREMA,
            foreground=self.ROJO
        )

        # -------------------------------------
        # TABLAS
        # -------------------------------------

        estilo.configure(
            "Treeview",
            font=("Segoe UI", 10),
            rowheight=28,
            background=self.BLANCO,
            fieldbackground=self.BLANCO,
            foreground=self.TEXTO
        )

        estilo.configure(
            "Treeview.Heading",
            font=("Segoe UI", 10, "bold"),
            background=self.ROJO,
            foreground=self.BLANCO
        )

        estilo.map(
            "Treeview",
            background=[
                ("selected", self.MOSTAZA)
            ],
            foreground=[
                ("selected", self.ROJO_OSCURO)
            ]
        )

        # -------------------------------------
        # COMBOBOX
        # -------------------------------------

        estilo.configure(
            "TCombobox",
            font=("Segoe UI", 10),
            fieldbackground=self.BLANCO,
            background=self.MOSTAZA,
            foreground=self.TEXTO
        )

        # =====================================
        # CONTENEDOR PRINCIPAL
        # =====================================

        contenedor = ttk.Frame(
            self.root,
            padding=15
        )

        contenedor.pack(
            fill="both",
            expand=True
        )

        # =====================================
        # ENCABEZADO
        # =====================================

        encabezado = ttk.Frame(
            contenedor
        )

        encabezado.pack(
            fill="x",
            pady=(0, 10)
        )

        ttk.Label(
            encabezado,
            text="GESTIÓN DE RESTAURANTE",
            font=("Georgia", 18, "bold"),
            foreground=self.ROJO,
            background=self.CREMA
        ).pack(
            side="left"
        )

        ttk.Button(
            encabezado,
            text="Cerrar sesión",
            image=self.icono_salir,
            compound="left",
            command=self.mostrar_login
        ).pack(
            side="right"
        )

        # =====================================
        # FORMULARIO DE PRODUCTOS
        # =====================================

        formulario = ttk.LabelFrame(
            contenedor,
            text="Información del producto",
            padding=10
        )

        formulario.pack(
            fill="x",
            pady=(0, 5)
        )

        ttk.Label(
            formulario,
            text="Nombre:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        self.nombre_entry = ttk.Entry(
            formulario,
            width=20
        )

        self.nombre_entry.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Label(
            formulario,
            text="Categoría:"
        ).grid(
            row=0,
            column=2,
            padx=5,
            pady=5
        )

        self.categoria_entry = ttk.Entry(
            formulario,
            width=20
        )

        self.categoria_entry.grid(
            row=0,
            column=3,
            padx=5,
            pady=5
        )

        ttk.Label(
            formulario,
            text="Precio:"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )

        self.precio_entry = ttk.Entry(
            formulario,
            width=20
        )

        self.precio_entry.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Label(
            formulario,
            text="Cantidad:"
        ).grid(
            row=1,
            column=2,
            padx=5,
            pady=5
        )

        self.cantidad_entry = ttk.Entry(
            formulario,
            width=20
        )

        self.cantidad_entry.grid(
            row=1,
            column=3,
            padx=5,
            pady=5
        )

        # =====================================
        # BOTONES DE PRODUCTOS
        # =====================================

        botones = ttk.Frame(
            contenedor
        )

        botones.pack(
            fill="x",
            pady=5
        )

        ttk.Button(
            botones,
            text="Registrar",
            image=self.icono_producto,
            compound="left",
            command=self.registrar_producto
        ).pack(
            side="left",
            padx=3
        )

        ttk.Button(
            botones,
            text="Actualizar",
            image=self.icono_producto,
            compound="left",
            command=self.actualizar_producto
        ).pack(
            side="left",
            padx=3
        )

        ttk.Button(
            botones,
            text="Eliminar",
            image=self.icono_producto,
            compound="left",
            command=self.eliminar_producto
        ).pack(
            side="left",
            padx=3
        )

        ttk.Button(
            botones,
            text="Limpiar",
            command=self.limpiar_formulario
        ).pack(
            side="left",
            padx=3
        )

        ttk.Button(
            botones,
            text="Consultar usuarios",
            image=self.icono_usuario,
            compound="left",
            command=self.mostrar_usuarios
        ).pack(
            side="right",
            padx=3
        )

        # =====================================
        # TABLA DE PRODUCTOS
        # =====================================

        tabla_frame = ttk.LabelFrame(
            contenedor,
            text="Productos registrados",
            padding=5
        )

        tabla_frame.pack(
            fill="both",
            expand=True,
            pady=5
        )

        columnas = (
            "id",
            "nombre",
            "categoria",
            "precio",
            "cantidad"
        )

        self.tabla = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings",
            height=6
        )

        encabezados = {
            "id": "ID",
            "nombre": "Nombre",
            "categoria": "Categoría",
            "precio": "Precio",
            "cantidad": "Cantidad"
        }

        anchos = {
            "id": 40,
            "nombre": 130,
            "categoria": 130,
            "precio": 80,
            "cantidad": 80
        }

        for columna in columnas:

            self.tabla.heading(
                columna,
                text=encabezados[columna]
            )

            self.tabla.column(
                columna,
                width=anchos[columna]
            )

        self.tabla.pack(
            fill="both",
            expand=True
        )

        self.tabla.bind(
            "<ButtonRelease-1>",
            self.seleccionar_producto
        )

        # =====================================
        # REGISTRAR VENTA
        # =====================================

        ventas_frame = ttk.LabelFrame(
            contenedor,
            text="Registrar venta",
            padding=8
        )

        ventas_frame.pack(
            fill="x",
            pady=5
        )

        ttk.Label(
            ventas_frame,
            text="Usuario:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        self.usuario_combo = ttk.Combobox(
            ventas_frame,
            state="readonly",
            width=25
        )

        self.usuario_combo.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Label(
            ventas_frame,
            text="Producto:"
        ).grid(
            row=0,
            column=2,
            padx=5,
            pady=5
        )

        self.producto_combo = ttk.Combobox(
            ventas_frame,
            state="readonly",
            width=25
        )

        self.producto_combo.grid(
            row=0,
            column=3,
            padx=5,
            pady=5
        )

        ttk.Button(
            ventas_frame,
            text="Registrar venta",
            image=self.icono_venta,
            compound="left",
            command=self.registrar_venta
        ).grid(
            row=0,
            column=4,
            padx=10,
            pady=5
        )

        # =====================================
        # TABLA DE VENTAS
        # =====================================

        ventas_tabla_frame = ttk.LabelFrame(
            contenedor,
            text="Ventas registradas",
            padding=5
        )

        ventas_tabla_frame.pack(
            fill="both",
            expand=True,
            pady=5
        )

        columnas_ventas = (
            "usuario",
            "producto",
            "fecha"
        )

        self.tabla_ventas = ttk.Treeview(
            ventas_tabla_frame,
            columns=columnas_ventas,
            show="headings",
            height=5
        )

        encabezados_ventas = {
            "usuario": "Usuario",
            "producto": "Producto",
            "fecha": "Fecha"
        }

        anchos_ventas = {
            "usuario": 150,
            "producto": 180,
            "fecha": 180
        }

        for columna in columnas_ventas:

            self.tabla_ventas.heading(
                columna,
                text=encabezados_ventas[columna]
            )

            self.tabla_ventas.column(
                columna,
                width=anchos_ventas[columna]
            )

        self.tabla_ventas.pack(
            fill="both",
            expand=True
        )

    # =====================================
    # PRODUCTOS
    # =====================================

    def cargar_productos(self):

        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        productos = self.servicio.obtener_productos()
        opciones = []

        for producto in productos:

            self.tabla.insert(
                "",
                "end",
                values=(
                    producto.get("id"),
                    producto.get("nombre"),
                    producto.get("categoria"),
                    f"{producto.get('precio', 0):.2f}",
                    producto.get("cantidad")
                )
            )

            opciones.append(
                f"{producto.get('id')} - {producto.get('nombre')}"
            )

        if hasattr(self, "producto_combo"):
            self.producto_combo["values"] = opciones

    def obtener_datos_formulario(self):

        nombre = self.nombre_entry.get().strip()
        categoria = self.categoria_entry.get().strip()
        precio_texto = self.precio_entry.get().strip()
        cantidad_texto = self.cantidad_entry.get().strip()

        if (
            not nombre
            or not categoria
            or not precio_texto
            or not cantidad_texto
        ):

            messagebox.showwarning(
                "Datos incompletos",
                "Complete todos los campos."
            )

            return None

        try:

            precio = float(precio_texto)
            cantidad = int(cantidad_texto)

            if precio < 0 or cantidad < 0:
                raise ValueError

        except ValueError:

            messagebox.showerror(
                "Datos incorrectos",
                "El precio debe ser decimal y la cantidad entera."
            )

            return None

        return nombre, categoria, precio, cantidad

    def registrar_producto(self):

        datos = self.obtener_datos_formulario()

        if datos is None:
            return

        nombre, categoria, precio, cantidad = datos

        self.servicio.registrar_producto(
            nombre,
            categoria,
            precio,
            cantidad
        )

        messagebox.showinfo(
            "Registro exitoso",
            "El producto fue registrado correctamente."
        )

        self.cargar_productos()
        self.limpiar_formulario()

    def seleccionar_producto(self, event=None):

        seleccion = self.tabla.selection()

        if not seleccion:
            return

        item = self.tabla.item(
            seleccion[0]
        )

        valores = item.get(
            "values"
        )

        if not valores:
            return

        self.limpiar_formulario()

        self.id_seleccionado = int(
            valores[0]
        )

        self.nombre_entry.insert(
            0,
            valores[1]
        )

        self.categoria_entry.insert(
            0,
            valores[2]
        )

        self.precio_entry.insert(
            0,
            valores[3]
        )

        self.cantidad_entry.insert(
            0,
            valores[4]
        )

    def actualizar_producto(self):

        if not hasattr(
            self,
            "id_seleccionado"
        ):

            messagebox.showwarning(
                "Selección requerida",
                "Seleccione un producto de la tabla."
            )

            return

        datos = self.obtener_datos_formulario()

        if datos is None:
            return

        nombre, categoria, precio, cantidad = datos

        actualizado = self.servicio.actualizar_producto(
            self.id_seleccionado,
            nombre,
            categoria,
            precio,
            cantidad
        )

        if actualizado:

            messagebox.showinfo(
                "Actualización exitosa",
                "El producto fue actualizado."
            )

            self.cargar_productos()
            self.limpiar_formulario()

        else:

            messagebox.showerror(
                "Error",
                "No se encontró el producto."
            )

    def eliminar_producto(self):

        if not hasattr(
            self,
            "id_seleccionado"
        ):

            messagebox.showwarning(
                "Selección requerida",
                "Seleccione un producto de la tabla."
            )

            return

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            "¿Desea eliminar el producto seleccionado?"
        )

        if not confirmar:
            return

        eliminado = self.servicio.eliminar_producto(
            self.id_seleccionado
        )

        if eliminado:

            messagebox.showinfo(
                "Eliminación exitosa",
                "El producto fue eliminado."
            )

            self.cargar_productos()
            self.limpiar_formulario()

        else:

            messagebox.showerror(
                "Error",
                "No se encontró el producto."
            )

    def limpiar_formulario(self):

        self.nombre_entry.delete(
            0,
            tk.END
        )

        self.categoria_entry.delete(
            0,
            tk.END
        )

        self.precio_entry.delete(
            0,
            tk.END
        )

        self.cantidad_entry.delete(
            0,
            tk.END
        )

        if hasattr(
            self,
            "id_seleccionado"
        ):
            del self.id_seleccionado

        for item in self.tabla.selection():

            self.tabla.selection_remove(
                item
            )

    # =====================================
    # USUARIOS
    # =====================================

    def cargar_usuarios_venta(self):

        usuarios = self.servicio.obtener_usuarios()
        opciones = []

        for usuario in usuarios:

            opciones.append(
                f"{usuario.get('usuario')} - {usuario.get('nombre')}"
            )

        self.usuario_combo["values"] = opciones

    def mostrar_usuarios(self):

        ventana = tk.Toplevel(
            self.root
        )

        ventana.title(
            "Usuarios registrados"
        )

        ventana.geometry(
            "500x300"
        )

        ventana.resizable(
            False,
            False
        )

        frame = ttk.Frame(
            ventana,
            padding=15
        )

        frame.pack(
            fill="both",
            expand=True
        )

        columnas = (
            "usuario",
            "nombre"
        )

        tabla_usuarios = ttk.Treeview(
            frame,
            columns=columnas,
            show="headings"
        )

        tabla_usuarios.heading(
            "usuario",
            text="Usuario"
        )

        tabla_usuarios.heading(
            "nombre",
            text="Nombre"
        )

        tabla_usuarios.column(
            "usuario",
            width=180
        )

        tabla_usuarios.column(
            "nombre",
            width=180
        )

        tabla_usuarios.pack(
            fill="both",
            expand=True
        )

        usuarios = self.servicio.obtener_usuarios()

        for usuario in usuarios:

            tabla_usuarios.insert(
                "",
                "end",
                values=(
                    usuario.get("usuario"),
                    usuario.get("nombre")
                )
            )

    # =====================================
    # VENTAS
    # =====================================

    def registrar_venta(self):

        usuario_seleccionado = self.usuario_combo.get()
        producto_seleccionado = self.producto_combo.get()

        if not usuario_seleccionado:

            messagebox.showwarning(
                "Usuario requerido",
                "Seleccione un usuario."
            )

            return

        if not producto_seleccionado:

            messagebox.showwarning(
                "Producto requerido",
                "Seleccione un producto."
            )

            return

        usuario = usuario_seleccionado.split(
            " - "
        )[0]

        producto_id = int(
            producto_seleccionado.split(
                " - "
            )[0]
        )

        exito, mensaje = self.servicio.registrar_venta(
            usuario,
            producto_id
        )

        if exito:

            messagebox.showinfo(
                "Venta registrada",
                mensaje
            )

            self.cargar_productos()
            self.cargar_ventas()

            self.producto_combo.set("")

        else:

            messagebox.showerror(
                "No se pudo registrar",
                mensaje
            )

    def cargar_ventas(self):

        if not hasattr(
            self,
            "tabla_ventas"
        ):
            return

        for fila in self.tabla_ventas.get_children():
            self.tabla_ventas.delete(fila)

        ventas = self.servicio.obtener_ventas()
        usuarios = self.servicio.obtener_usuarios()
        productos = self.servicio.obtener_productos()

        nombres_usuarios = {
            usuario.get("usuario"): usuario.get("nombre")
            for usuario in usuarios
        }

        nombres_productos = {
            producto.get("id"): producto.get("nombre")
            for producto in productos
        }

        for venta in ventas:

            usuario = venta.get(
                "usuario",
                ""
            )

            producto_id = venta.get(
                "producto_id"
            )

            nombre_usuario = nombres_usuarios.get(
                usuario,
                usuario
            )

            nombre_producto = nombres_productos.get(
                producto_id,
                "Producto eliminado"
            )

            self.tabla_ventas.insert(
                "",
                "end",
                values=(
                    nombre_usuario,
                    nombre_producto,
                    venta.get("fecha")
                )
            )