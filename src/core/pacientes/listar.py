from ui_config import sg
from database.singleton import DatabaseManagerSingleton

# Definición de la interfaz para listar pacientes
def listar_paciente_interface():
    sg.theme('MyNewTheme')
    layout = [
        [sg.Text("Listado de Pacientes", font=("Helvetica", 20), justification='center')],
        [sg.Multiline(default_text="PACIENTES", size=(60, 15), disabled=True, key="-LISTADO-")],
        [sg.Button("Volver", size=(15, 1))]
    ]
    window = sg.Window("Listar Pacientes", layout, size=(800, 500), finalize=True)
    db = DatabaseManagerSingleton.get_instance()
    # Revisar si el ID existe antes de insertar
    def verificacion(tabla, campo_id, valor):
        query = f"SELECT 1 FROM {tabla} WHERE {campo_id} = %s LIMIT 1"
        resultado = db.execute_query(query, params=(valor,), fetch="one")
        return bool(resultado)

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
                # Verificación previa
                if not verificacion("pacientes", "id_paciente", id_paciente):
                    sg.popup("Error", f"No se encontró un paciente con ID {id_paciente}")
                    continue
                if not verificacion("doctores", "id_doctor", id_doctor):
                    sg.popup("Error", f"No se encontró un doctor con ID {id_doctor}")
                    continue

                query = """
                    INSERT INTO historial_consultas (
                        id_paciente, id_doctor, diagnostico, tratamiento, observaciones, estado
                    ) VALUES (%s, %s, %s, %s, %s, %s)
                """
                db.execute_query(query, (
                    id_paciente, id_doctor, diagnostico, tratamiento, observaciones, estado
                ))
                sg.popup("Consulta guardada exitosamente", title="Éxito")
                
                for key in ["-IDPACIENTE-", "-IDDOCTOR-", "-DIAGNOSTICO-", "-TRATAMIENTO-", "-OBSERVACIONES-"]:
                    window[key].update("")
                window["-ESTADO-"].update("Abierta")

            except Exception as e:
                sg.popup(f"Error al guardar consulta: {e}", title="Error")

    window.close()
    db.close()
