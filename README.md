# Restaurante App - Semana 15

## Datos del proyecto

**Asignatura:** Programación Orientada a Objetos

**Proyecto:** restaurante_app

**Semana:** 15

**Tema:** Conceptos fundamentales de manejo de eventos

---

## Descripción

El proyecto consiste en una aplicación de escritorio desarrollada en Python utilizando Tkinter.

La aplicación permite gestionar productos, consultar usuarios y registrar ventas mediante una interfaz gráfica.

En esta semana se incorporan conceptos fundamentales de manejo de eventos mediante botones y funciones callback.

---

## Funcionalidades

La aplicación permite:

- Iniciar sesión.
- Registrar productos.
- Actualizar productos.
- Eliminar productos.
- Consultar usuarios.
- Seleccionar usuarios mediante un Combobox.
- Seleccionar productos mediante un Combobox.
- Registrar ventas.
- Guardar las ventas en formato JSON.
- Consultar las ventas registradas.
- Actualizar la información de la interfaz después de registrar una venta.
- Controlar el stock disponible de los productos.

---

## Manejo de eventos

Para el registro de ventas se utiliza el atributo `command` de los botones de Tkinter.

El flujo utilizado es:

Usuario selecciona una opción
→ botón
→ evento `command`
→ función callback
→ `RestauranteServicio`
→ almacenamiento en JSON
→ actualización de la interfaz.

Por ejemplo:

```python
ttk.Button(
    ventas_frame,
    text="Registrar venta",
    command=self.registrar_venta
)