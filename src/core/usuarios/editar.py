from ui_config import sg
from database.singleton import DatabaseManagerSingleton

# Definición de la interfaz para editar un usuario
def editar_usuario_interface():
    sg.theme('MyNewTheme')

    layout = [
        [sg.Text("Editar Usuario", font=("Helvetica", 20))],

        [sg.Frame("Buscar", [
            [sg.Text("Buscar por Usuario"), sg.Input(key="-USUARIO-", size=(30, 1)), sg.Button("Buscar")],
        ])],

        [sg.HorizontalSeparator()],

        [sg.Frame("Datos del Usuario", [
            [sg.Text("Nombre"), sg.Input(key="-NOMBRE-", size=(30, 1), disabled=True)],
            [sg.Text("Apellido"), sg.Input(key="-APELLIDO-", size=(30, 1), disabled=True)],
            [sg.Text("Contraseña"), sg.Input(key="-PASSWORD-", password_char="*", size=(30, 1), disabled=True)],
            [sg.Text("Rol"), sg.Combo(["Administrador", "Usuario"], key="-ROL-", disabled=True)],
            [sg.Text("Estado"), sg.Combo(["Activo", "Inactivo"], key="-ESTADO-", disabled=True)],
            [sg.Text("Fecha de Registro"), sg.Input(key="-FECHA_REGISTRO-", size=(30, 1), disabled=True)],
        ])],

        [sg.Button("Guardar Cambios", size=(20, 1)), sg.Button("Volver", size=(20, 1))]
    ]

    window = sg.Window("Editar Usuario", layout, size=(600, 500), element_justification='c', finalize=True)
    db = DatabaseManagerSingleton.get_instance()

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Volver"):
            break

        if event == "Buscar":
            usuario = values["-USUARIO-"]
            if not usuario:
                sg.popup("Ingrese el nombre de usuario a buscar")
                continue

            try:
                query = "SELECT nombre, password, rol, estado, fecha_registro FROM usuarios WHERE usuario = %s"
                result = db.execute_query(query, (usuario,), fetch="one")
                if result:
                    nombre, password, rol, estado, fecha = result

                    window["-NOMBRE-"].update(value=nombre, disabled=False)
                    window["-PASSWORD-"].update(value=password, disabled=False)
                    window["-ROL-"].update(value=rol, disabled=False)
                    window["-ESTADO-"].update(value=estado, disabled=False)
                    window["-FECHA_REGISTRO-"].update(value=str(fecha), disabled=True)

                    window["Guardar Cambios"].update(disabled=False)
                else:
                    sg.popup("Usuario no encontrado")
            except Exception as e:
                sg.popup(f"Error al buscar usuario: {e}")

        elif event == "Guardar Cambios":
            try:
                nombre = values["-NOMBRE-"]
                password = values["-PASSWORD-"]
                rol = values["-ROL-"]
                estado = values["-ESTADO-"]
                usuario = values["-USUARIO-"]

                if not all([nombre, password, rol, estado]):
                    sg.popup("Todos los campos deben estar llenos")
                    continue

                query = """
                    UPDATE usuarios
                    SET nombre = %s, password = %s, rol = %s, estado = %s
                    WHERE usuario = %s
                """
                filas_afectadas = db.execute_query(query, (nombre, password, rol, estado, usuario))
                if filas_afectadas:
                    sg.popup("Usuario actualizado correctamente")
                else:
                    sg.popup("No se pudo actualizar el usuario")
            except Exception as e:
                sg.popup(f"Error al actualizar usuario: {e}")

    window.close()
    db.close()
