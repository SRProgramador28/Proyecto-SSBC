from ui_config import sg
from database.singleton import DatabaseManagerSingleton

# Definición de la interfaz para el formulario de consulta
def consulta_interface():
    sg.theme('MyNewTheme')
    layout = [
        [sg.Text("Formulario de Consulta", font=("Helvetica", 18))],
        [sg.Frame("Datos de la Consulta", [
            [sg.Text("ID Paciente", size=(15, 1)), sg.Input(key="-ID_PACIENTE-")],
            [sg.Text("ID Doctor", size=(15, 1)), sg.Input(key="-ID_DOCTOR-")],
            [sg.Text("Diagnóstico Provisional", size=(15, 1)), sg.Multiline(key="-DIAGNOSTICO-", size=(40, 3))],
            [sg.Text("Tratamiento Prescrito", size=(15, 1)), sg.Multiline(key="-TRATAMIENTO-", size=(40, 3))],
            [sg.Text("Observaciones", size=(15, 1)), sg.Multiline(key="-OBSERVACIONES-", size=(40, 3))],
            [sg.Text("Estado de Consulta", size=(15, 1)), sg.Combo(["Abierta", "En proceso", "Cerrada"], key="-ESTADO-", default_value="Abierta")],
        ])],
        [sg.Button("Guardar Consulta", size=(20, 1)), sg.Button("Volver", size=(20, 1))]
    ]
    window = sg.Window("Formulario de Consulta", layout, size=(600, 500), element_justification='c', finalize=True)
    db = DatabaseManagerSingleton.get_instance()

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Volver"):
            break

        elif event == "Guardar Consulta":
            id_paciente = values["-ID_PACIENTE-"]
            id_doctor = values["-ID_DOCTOR-"]
            diagnostico = values["-DIAGNOSTICO-"]
            tratamiento = values["-TRATAMIENTO-"]
            observaciones = values["-OBSERVACIONES-"]
            estado = values["-ESTADO-"]

            # Validar campos
            if not id_paciente or not id_doctor or not diagnostico or not estado:
                sg.popup("Error", "Por favor, complete los campos obligatorios.")
                continue

            try:
                # Verificar si el paciente y el doctor existen
                paciente_query = "SELECT 1 FROM pacientes WHERE id_paciente = %s"
                doctor_query = "SELECT 1 FROM doctores WHERE id_doctor = %s"
                if not db.execute_query(paciente_query, (id_paciente,), fetch="one"):
                    sg.popup("Error", f"No se encontró un paciente con ID {id_paciente}.")
                    continue
                if not db.execute_query(doctor_query, (id_doctor,), fetch="one"):
                    sg.popup("Error", f"No se encontró un doctor con ID {id_doctor}.")
                    continue

                # Insertar
                query = """
                    INSERT INTO consultas (id_paciente, id_doctor, diagnostico, tratamiento, observaciones, estado)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                db.execute_query(query, (id_paciente, id_doctor, diagnostico, tratamiento, observaciones, estado))
                sg.popup("Consulta guardada exitosamente", title="Éxito")

                # Limpiar los campos después de guardar
                for key in ["-ID_PACIENTE-", "-ID_DOCTOR-", "-DIAGNOSTICO-", "-TRATAMIENTO-", "-OBSERVACIONES-"]:
                    window[key].update("")
                window["-ESTADO-"].update("Abierta")

            except Exception as e:
                sg.popup(f"Error al guardar la consulta: {e}", title="Error")

    window.close()
    db.close()
