import tkinter as tk

from servicios.restaurante_servicio import (
    RestauranteServicio
)

from ui.login_view import (
    LoginView
)

from ui.main_view import (
    MainView
)


class RestauranteApp:

    def __init__(
        self,
        root
    ):

        self.root = root

        self.root.title(
            "Restaurante App - Semana 15"
        )

        self.root.geometry(
            "900x700"
        )

        self.root.resizable(
            False,
            False
        )

        self.restaurante_servicio = (
            RestauranteServicio()
        )

        self.mostrar_login()

    def limpiar_ventana(self):

        for widget in (
            self.root.winfo_children()
        ):

            widget.destroy()

    def mostrar_login(self):

        self.limpiar_ventana()

        LoginView(
            self.root,
            self.restaurante_servicio,
            self.mostrar_main
        )

    def mostrar_main(self):

        self.limpiar_ventana()

        MainView(
            self.root,
            self.restaurante_servicio,
            self.mostrar_login
        )


if __name__ == "__main__":

    root = tk.Tk()

    app = RestauranteApp(
        root
    )

    root.mainloop()