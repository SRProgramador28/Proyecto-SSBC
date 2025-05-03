from ui_config import sg
from database.singleton import DatabaseManagerSingleton

def doctores_interface():
    sg.theme("MyNewTheme")

    layout = [
        [sg.Text("Gestión de Doctores", font=("Helvetica", 20), justification='center')],

        [sg.Frame("Datos del Doctor", [
            [sg.Text("Nombre del Doctor", size=(20, 1)), sg.Input(key="-NOMBRE-", size=(30, 1))],
            [sg.Text("Especialidad", size=(20, 1)), sg.Input(key="-ESPECIALIDAD-", size=(30, 1))],
            [sg.Text("ID de Usuario Vinculado", size=(20, 1)), sg.Input(key="-ID-USUARIO-", size=(30, 1))],
        ])],

        [sg.Button("Registrar Doctor", size=(20, 1)), sg.Button("Volver", size=(20, 1))]
    ]

    window = sg.Window("Gestión de Doctores", layout, size=(600, 500), element_justification='c', finalize=True)
    db = DatabaseManagerSingleton.get_instance()

    def buscar_usuario(id_usuario):
        try:
            query = "SELECT id_usuario FROM usuarios WHERE id_usuario = %s"
            resultado = db.execute_query(query, (id_usuario,))
            if resultado:
                return resultado[0][0]
        except Exception as e:
            sg.popup(f"Error al buscar usuario: {str(e)}")

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Volver"):
            break

        elif event == "Registrar Doctor":
            nombre = values["-NOMBRE-"]
            especialidad = values["-ESPECIALIDAD-"]
            id_usuario = values["-ID-USUARIO-"]

            if not nombre or not especialidad or not id_usuario:
                sg.popup("Error", "Todos los campos son obligatorios.")
                continue

            if not buscar_usuario(id_usuario):
                sg.popup("Error", "ID de usuario no encontrado.")
                continue

            try:
                query = """
                    INSERT INTO doctores (nombre, especialidad, id_usuario)
                    VALUES (%s, %s, %s)
                """
                db.execute_query(query, (nombre, especialidad, id_usuario))
                sg.popup("Doctor registrado exitosamente", title="Éxito")

                for key in ["-NOMBRE-", "-ESPECIALIDAD-", "-ID-USUARIO-"]:
                    window[key].update("")
            except Exception as e:
                sg.popup(f"Error al registrar doctor: {e}", title="Error")

    window.close()
    db.close()
