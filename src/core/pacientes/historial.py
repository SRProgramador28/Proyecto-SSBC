from ui_config import sg
from database.singleton import DatabaseManagerSingleton

# Definición de la interfaz para el historial médico
def historial_interface():
    layout = [
        [sg.Text("Historial de Consulta", font=("Helvetica", 20), justification='center')],
        
        [sg.Text("ID Paciente", size=(20, 1)), sg.Input(key="-IDPACIENTE-", size=(30, 1))],
        [sg.Text("ID Doctor", size=(20, 1)), sg.Input(key="-IDDOCTOR-", size=(30, 1))],
        [sg.Text("Diagnóstico Provisional", size=(20, 1)), sg.Multiline(key="-DIAGNOSTICO-", size=(30, 3))],
        [sg.Text("Tratamiento Prescrito", size=(20, 1)), sg.Multiline(key="-TRATAMIENTO-", size=(30, 3))],
        [sg.Text("Observaciones", size=(20, 1)), sg.Multiline(key="-OBSERVACIONES-", size=(30, 3))],
        [sg.Text("Estado de Consulta", size=(20, 1)), sg.Combo(['Pendiente', 'Finalizada'], key="-ESTADO-", size=(30, 1))],
        
        [sg.Button("Guardar Consulta", size=(20, 1))],
        [sg.Button("Volver", size=(20, 1))]
    ]
    
    window = sg.Window("Historial Médico", layout, size=(650, 500), element_justification='center', finalize=True)
    db = DatabaseManagerSingleton.get_instance()

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Volver"):
            break

        elif event == "Guardar Consulta":
            id_paciente = values["-IDPACIENTE-"]
            id_doctor = values["-IDDOCTOR-"]
            diagnostico = values["-DIAGNOSTICO-"]
            tratamiento = values["-TRATAMIENTO-"]
            observaciones = values["-OBSERVACIONES-"]
            estado = values["-ESTADO-"]

            if not id_paciente or not id_doctor or not diagnostico or not estado:
                sg.popup("Error", "Los campos ID Paciente, ID Doctor, Diagnóstico y Estado son obligatorios.")
                continue

            try:
                query = """
                    INSERT INTO historial_consultas (
                        id_paciente, id_doctor, diagnostico, tratamiento, observaciones, estado
                    ) VALUES (%s, %s, %s, %s, %s, %s)
                """
                db.execute_query(query, (
                    id_paciente, id_doctor, diagnostico, tratamiento, observaciones, estado
                ))
                sg.popup("Consulta guardada exitosamente", title="Éxito")
                # Limpiar campos después del guardado
                for key in ["-IDPACIENTE-", "-IDDOCTOR-", "-DIAGNOSTICO-", "-TRATAMIENTO-", "-OBSERVACIONES-"]:
                    window[key].update("")
                window["-ESTADO-"].update("Abierta")
            except Exception as e:
                sg.popup(f"Error al guardar consulta: {e}", title="Error")

    window.close()
    db.close()
