from ui_config import sg
from database.singleton import DatabaseManagerSingleton

# Definición de la interfaz para buscar citas
def buscar_cita_interface():
    sg.theme('MyNewTheme')
    layout = [
        [sg.Text("Buscar Cita", font=("Helvetica", 20), justification='center', expand_x=True)],
        [sg.Text("Código del Paciente:", size=(20, 1)), sg.Input(key="-BUSCAR-", size=(30, 1))],
        [sg.Button("Buscar", size=(15, 1)), sg.Button("Volver", size=(15, 1))],
        [sg.Text("Resultados:", font=("Helvetica", 12))],
        [sg.Multiline(key="-RESULTADO-", size=(70, 15), disabled=True)]
    ]

    window = sg.Window("Buscar Cita", layout, size=(700, 500), element_justification='c', finalize=True)
    db = DatabaseManagerSingleton.get_instance()

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Volver"):
            break

        elif event == "Buscar":
            criterio = values["-BUSCAR-"]
            if not criterio:
                sg.popup("Error", "Por favor, ingrese el código del paciente.")
                continue

            try:
                query = """
                    SELECT c.id_cita, p.nombre, p.apellido, d.nombre AS doctor, c.fecha_hora, c.motivo, c.estado
                    FROM citas c
                    INNER JOIN pacientes p ON c.id_paciente = p.id_paciente
                    INNER JOIN doctores d ON c.id_doctor = d.id_doctor
                    WHERE p.id_paciente = %s
                    ORDER BY c.fecha_hora DESC
                """
                resultados = db.fetch_all(query, (criterio,))

                if resultados:
                    texto_resultado = ""
                    for r in resultados:
                        texto_resultado += (f"ID Cita: {r['id_cita']}\n"
                                            f"Paciente: {r['nombre']} {r['apellido']}\n"
                                            f"Doctor: {r['doctor']}\n"
                                            f"Fecha: {r['fecha_hora']}\n"
                                            f"Motivo: {r['motivo']}\n"
                                            f"Estado: {r['estado']}\n"
                                            f"{'-'*50}\n")
                else:
                    texto_resultado = "No se encontraron citas para ese paciente."

                window["-RESULTADO-"].update(texto_resultado)

            except Exception as e:
                sg.popup_error(f"Error al buscar: {e}")

    window.close()
    db.close()


