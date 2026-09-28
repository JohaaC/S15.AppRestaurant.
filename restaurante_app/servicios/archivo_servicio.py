import json


class ArchivoServicio:

    def leer_json(self, ruta):

        try:

            if not ruta.exists():

                return []

            with open(
                ruta,
                "r",
                encoding="utf-8"
            ) as archivo:

                contenido = archivo.read().strip()

                if not contenido:

                    return []

                return json.loads(contenido)

        except FileNotFoundError:

            return []

        except json.JSONDecodeError:

            return []

        except PermissionError:

            return []

        except OSError:

            return []

    def guardar_json(
        self,
        ruta,
        datos
    ):

        try:

            ruta.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            with open(
                ruta,
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )

            return True

        except PermissionError:

            return False

        except OSError:

            return False