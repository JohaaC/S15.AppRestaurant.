import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path
from PIL import Image, ImageTk


class LoginView:

    def __init__(
        self,
        root,
        restaurante_servicio,
        mostrar_main
    ):

        self.root = root

        self.servicio = (
            restaurante_servicio
        )

        self.mostrar_main = (
            mostrar_main
        )

        self.crear_interfaz()

    def crear_interfaz(self):

        self.root.configure(
            bg="#f2f4f7"
        )

        contenedor = ttk.Frame(
            self.root,
            padding=30
        )

        contenedor.pack(
            expand=True
        )

        # =========================
        # LOGO
        # =========================

        base_dir = Path(__file__).resolve().parent.parent

        ruta_logo = (
            base_dir
            / "assets"
            / "logo.png"
        )

        imagen = Image.open(ruta_logo)

        imagen = imagen.resize(
            (150, 150)
        )

        self.logo = ImageTk.PhotoImage(
            imagen
        )

        ttk.Label(
            contenedor,
            image=self.logo
        ).pack(
            pady=10
        )

        # =========================
        # TÍTULO
        # =========================

        ttk.Label(
            contenedor,
            text="RESTAURANTE APP",
            font=("Arial", 22, "bold")
        ).pack(
            pady=20
        )

        ttk.Label(
            contenedor,
            text="Inicio de sesión",
            font=("Arial", 13)
        ).pack(
            pady=10
        )

        # =========================
        # USUARIO
        # =========================

        ttk.Label(
            contenedor,
            text="Usuario:"
        ).pack(
            pady=(10, 2)
        )

        self.usuario_entry = ttk.Entry(
            contenedor,
            width=30
        )

        self.usuario_entry.pack()

        # =========================
        # CONTRASEÑA
        # =========================

        ttk.Label(
            contenedor,
            text="Contraseña:"
        ).pack(
            pady=(10, 2)
        )

        self.contraseña_entry = ttk.Entry(
            contenedor,
            width=30,
            show="*"
        )

        self.contraseña_entry.pack()

        # =========================
        # BOTÓN INICIAR SESIÓN
        # =========================

        ttk.Button(
            contenedor,
            text="Iniciar sesión",
            command=self.iniciar_sesion
        ).pack(
            pady=20
        )

    def iniciar_sesion(self):

        usuario = (
            self.usuario_entry
            .get()
            .strip()
        )

        contraseña = (
            self.contraseña_entry
            .get()
            .strip()
        )

        if not usuario or not contraseña:

            messagebox.showwarning(
                "Datos incompletos",
                "Ingrese usuario y contraseña."
            )

            return

        valido = self.servicio.validar_usuario(
            usuario,
            contraseña
        )

        if valido:

            self.mostrar_main()

        else:

            messagebox.showerror(
                "Acceso denegado",
                "Usuario o contraseña incorrectos."
            )