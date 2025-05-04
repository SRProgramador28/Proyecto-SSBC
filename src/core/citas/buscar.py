from ui_config import sg
from database.singleton import DatabaseManagerSingleton

# Definición de la interfaz para buscar citas
def buscar_cita_interface():
    sg.theme('MyNewTheme')
    layout = [
        [sg.Text("Buscar Cita", font=("Helvetica", 20), justification='center', expand_x=True)],
        
        [sg.Frame("Buscar Paciente", [
            [sg.Text("ID o Nombre del Paciente:", size=(20, 1)), sg.Input(key="-BUSCAR-", size=(30, 1))],
            [sg.Button("Buscar", key="-BUSCAR-BTN-", size=(15,1))]
        ])],

        [sg.Frame("Resultados", [
            [sg.Multiline(key="-RESULTADO-", size=(80, 18), disabled=True)]
        ])],

        [sg.Button("Volver", size=(20, 1))]
    ]

    window = sg.Window("Buscar Cita", layout, size=(600, 500), element_justification='c', finalize=True)
    db = DatabaseManagerSingleton.get_instance()

    def obtener_paciente(criterio):
        try:
            if criterio.isdigit():
                query = "SELECT id_paciente FROM pacientes WHERE id_paciente = %s"
                resultado = db.execute_query(query, (criterio,))
                if resultado:
                    return resultado[0][0]
                
            # Buscar por nombre
            query = """
            SELECT id_paciente FROM pacientes
            WHERE CONCAT(nombre, ' ', apellido) LIKE %s
            LIMIT 1
            """
            resultado = db.execute_query(query, (f"%{criterio}%",))
                resultado = db.execute_query(query, (criterio,), fetch="one")
            else:
                # Buscar por nombre
                query = """
                SELECT id_paciente FROM pacientes 
                WHERE CONCAT(nombre, ' ', apellido) LIKE %s 
                LIMIT 1
                """
                resultado = db.execute_query(query, (f"%{criterio}%",), fetch="one")

            if resultado:
                return resultado[0][0]  
                    return resultado[0]
            return None
        except Exception as e:
            sg.popup(f"Error al obtener ID del paciente: {e}")
        return None

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Volver"):
            break
        elif event == "-BUSCAR-BTN-":
            criterio = values["-BUSCAR-"].strip()
            if not criterio:
                sg.popup("Error", "Por favor, ingrese el nombre o ID del paciente.")
                continue

            id_paciente = obtener_paciente(criterio)

            if not id_paciente:
                sg.popup("Error", "No se encontró un paciente con ese ID o nombre.")
                window["-RESULTADO-"].update("")
                continue

            try:
                query = """
                    SELECT id_cita, nombre_completo_paciente, nombre_doctor, especialidad, fecha_hora, motivo, estado
                    FROM vista_citas
                    WHERE id_paciente = %s
                    ORDER BY fecha_hora DESC
                """
                resultados = db.execute_query(query, (id_paciente,))

                if resultados:
                    texto_resultado = ""
                    for r in resultados:
                        texto_resultado += (f"ID Cita: {r[0]}\n"
                                            f"Paciente: {r[1]}\n"
                                            f"Doctor: {r[2]} ({r[3]})\n"
                                            f"Fecha: {r[4]}\n"
                                            f"Motivo: {r[5]}\n"
                                            f"Estado: {r[6]}\n"
                                            f"{'-'*60}\n")
                else:
                    texto_resultado = "No se encontraron citas para este paciente."

                window["-RESULTADO-"].update(texto_resultado)

            except Exception as e:
                sg.popup_error(f"Error al buscar: {e}")

    window.close()
    db.close()
