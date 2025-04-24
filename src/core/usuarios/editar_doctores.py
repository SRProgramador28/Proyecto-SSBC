from ui_config import sg
from database.singleton import DatabaseManagerSingleton

def editar_doctor_interface():
    sg.theme("MyNewTheme")

    layout = [
        [sg.Text("Editar Doctor", font=("Helvetica", 20))],
        [sg.Text("ID del Doctor"), sg.Input(key="-ID-", size=(20, 1)), sg.Button("Buscar")],
        [sg.HorizontalSeparator()],
        [sg.Text("Nombre"), sg.Input(key="-NOMBRE-", size=(30, 1), disabled=True)],
        [sg.Text("Especialidad"), sg.Input(key="-ESPECIALIDAD-", size=(30, 1), disabled=True)],
        [sg.Text("ID de Usuario Vinculado"), sg.Input(key="-IDUSUARIO-", size=(30, 1), disabled=True)],
        [sg.Button("Guardar Cambios", size=(20, 1), disabled=True), sg.Button("Volver", size=(20, 1))]
    ]

    window = sg.Window("Editar Doctor", layout, size=(500, 400), finalize=True)
    db = DatabaseManagerSingleton.get_instance()

    def usuario_existe(id_usuario):
        query = "SELECT 1 FROM usuarios WHERE id = %s LIMIT 1"
        return bool(db.execute_query(query, (id_usuario,), fetch="one"))

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Volver"):
            break

        elif event == "Buscar":
            doctor_id = values["-ID-"]
            if not doctor_id:
                sg.popup("Error", "Por favor, ingrese el ID del doctor.")
                continue

            query = "SELECT * FROM doctores WHERE id_doctor = %s"
            doctor = db.execute_query(query, (doctor_id,), fetch="one")

            if doctor:
                window["-NOMBRE-"].update(doctor[1], disabled=False)
                window["-ESPECIALIDAD-"].update(doctor[2], disabled=False)
                window["-IDUSUARIO-"].update(doctor[3], disabled=False)
                window["Guardar Cambios"].update(disabled=False)
            else:
                sg.popup("Error", "No se encontró un doctor con ese ID.")

        elif event == "Guardar Cambios":
            nombre = values["-NOMBRE-"]
            especialidad = values["-ESPECIALIDAD-"]
            id_usuario = values["-IDUSUARIO-"]
            doctor_id = values["-ID-"]

            if not nombre or not especialidad or not id_usuario:
                sg.popup("Error", "Todos los campos son obligatorios.")
                continue

            if not usuario_existe(id_usuario):
                sg.popup("Error", f"No existe un usuario con ID {id_usuario}.")
                continue

            try:
                query = """
                    UPDATE doctores
                    SET nombre = %s, especialidad = %s, id_usuario = %s
                    WHERE id_doctor = %s
                """
                db.execute_query(query, (nombre, especialidad, id_usuario, doctor_id))
                sg.popup("Doctor actualizado exitosamente", title="Éxito")
                for key in ["-NOMBRE-", "-ESPECIALIDAD-", "-IDUSUARIO-"]:
                    window[key].update("", disabled=True)
                window["Guardar Cambios"].update(disabled=True)

            except Exception as e:
                sg.popup(f"Error al actualizar doctor: {e}", title="Error")

    window.close()
    db.close()
