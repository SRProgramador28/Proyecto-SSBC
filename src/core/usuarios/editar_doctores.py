from ui_config import sg
from database.singleton import DatabaseManagerSingleton

def editar_doctor_interface():
    sg.theme("MyNewTheme")

    layout = [
        [sg.Text("Editar Doctor", font=("Helvetica", 20))],

        [sg.Frame("Buscar Doctor", [
            [sg.Text("ID o Nombre del Doctor:"), sg.Input(key="-BUSCAR-", size=(30, 1)), sg.Button("Buscar")]
        ])],

        [sg.HorizontalSeparator()],

        [sg.Frame("Datos del Doctor", [
            [sg.Text("Nombre"), sg.Input(key="-NOMBRE-", size=(30, 1), disabled=True)],
            [sg.Text("Especialidad"), sg.Input(key="-ESPECIALIDAD-", size=(30, 1), disabled=True)],
            [sg.Text("ID de Usuario Vinculado"), sg.Text("", key="-IDUSUARIO-", size=(30, 1))],
        ])],

        [sg.Button("Guardar Cambios", size=(20, 1), disabled=True), sg.Button("Volver", size=(20, 1))]
    ]

    window = sg.Window("Editar Doctor", layout, size=(600, 500), element_justification='c', finalize=True)
    db = DatabaseManagerSingleton.get_instance()

    def obtener_id_doctor(criterio):
        try:
            if criterio.isdigit():
                query = "SELECT id_doctor FROM doctores WHERE id_doctor = %s"
                resultado = db.execute_query(query, (criterio,))
                if resultado:
                    return resultado[0][0]
            # Buscar por nombre
            query = "SELECT id_doctor FROM doctores WHERE nombre LIKE %s LIMIT 1"
            resultado = db.execute_query(query, (f"%{criterio}%",))
            if resultado:
                return resultado[0][0]
        except Exception as e:
            sg.popup_error(f"Error al buscar doctor: {e}")
        return None

    def usuario_existe(id_usuario):
        query = "SELECT 1 FROM usuarios WHERE id = %s LIMIT 1"
        return bool(db.execute_query(query, (id_usuario,), fetch="one"))

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Volver"):
            break

        elif event == "Buscar":
            criterio = values["-BUSCAR-"].strip()
            if not criterio:
                sg.popup("Por favor, ingrese el ID o nombre del doctor.")
                continue

            id_doctor = obtener_id_doctor(criterio)
            if not id_doctor:
                sg.popup("No se encontró un doctor con ese criterio.")
                continue

            query = "SELECT * FROM doctores WHERE id_doctor = %s"
            doctor = db.execute_query(query, (id_doctor,), fetch="one")

            if doctor:
                window["-BUSCAR-"].update(str(doctor[0]))
                window["-NOMBRE-"].update(doctor[1], disabled=False)
                window["-ESPECIALIDAD-"].update(doctor[2], disabled=False)
                window["-IDUSUARIO-"].update(str(doctor[3]))
                window["Guardar Cambios"].update(disabled=False)
            else:
                sg.popup("Error al cargar los datos del doctor.")

        elif event == "Guardar Cambios":
            nombre = values["-NOMBRE-"]
            especialidad = values["-ESPECIALIDAD-"]
            id_usuario = values["-IDUSUARIO-"]
            id_doctor = values["-BUSCAR-"]

            if not nombre or not especialidad or not id_usuario:
                sg.popup("Todos los campos son obligatorios.")
                continue

            if not usuario_existe(id_usuario):
                sg.popup(f"No existe un usuario con ID {id_usuario}.")
                continue

            try:
                query = """
                    UPDATE doctores
                    SET nombre = %s, especialidad = %s, id_usuario = %s
                    WHERE id_doctor = %s
                """
                db.execute_query(query, (nombre, especialidad, id_usuario, id_doctor))
                sg.popup("Doctor actualizado exitosamente", title="Éxito")
                for key in ["-NOMBRE-", "-ESPECIALIDAD-", "-IDUSUARIO-"]:
                    window[key].update("", disabled=True)
                window["Guardar Cambios"].update(disabled=True)

            except Exception as e:
                sg.popup(f"Error al actualizar doctor: {e}", title="Error")

    window.close()
    db.close()
