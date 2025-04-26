from ui_config import sg
from database.singleton import DatabaseManagerSingleton

# Definición de la interfaz para las pruebas postmortem
def pruebas_postmortem_interface():
    sg.theme('MyNewTheme')
    layout = [
        [sg.Text("Registro de Pruebas Postmortem", font=("Helvetica", 18))],
        
        [sg.Text("ID Consulta", size=(18, 1)), sg.Input(key="-ID_CONSULTA-")],
        [sg.Text("Nombre de la Prueba", size=(18, 1)), sg.Input(key="-NOMBRE_PRUEBA-")],
        [sg.Text("Fecha de Realización", size=(18, 1)), sg.Input(key="-FECHA-", size=(20, 1)), sg.CalendarButton("Seleccionar Fecha", target="-FECHA-", format="%Y-%m-%d")],
        [sg.Text("Detalles", size=(18, 1)), sg.Multiline(key="-DETALLES-", size=(45, 5))],
        [sg.Text("Prueba Realizada", size=(18, 1)), sg.Checkbox("", default=False, key="-REALIZADA-")],

        [sg.Button("Guardar Prueba", size=(20, 1)), sg.Button("Volver", size=(20, 1))]
    ]
    window = sg.Window("Pruebas Postmortem", layout, size=(600, 400), finalize=True)
    db = DatabaseManagerSingleton.get_instance()

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Volver"):
            break

        elif event == "Guardar Prueba":
            id_consulta = values["-ID_CONSULTA-"]
            nombre_prueba = values["-NOMBRE_PRUEBA-"]
            fecha_realizacion = values["-FECHA-"]
            detalles = values["-DETALLES-"]
            realizada = values["-REALIZADA-"]

            # Validar campos
            if not id_consulta or not nombre_prueba or not fecha_realizacion:
                sg.popup("Error", "Por favor, complete los campos obligatorios.")
                continue

            try:
                # Verificar consulta
                consulta_query = "SELECT 1 FROM consultas WHERE id_consulta = %s"
                if not db.execute_query(consulta_query, (id_consulta,), fetch="one"):
                    sg.popup("Error", f"No se encontró una consulta con ID {id_consulta}.")
                    continue

                # Verificar prueba 
                prueba_query = "SELECT id_prueba_postmortem FROM pruebas_postmortem WHERE nombre_prueba = %s"
                prueba_result = db.execute_query(prueba_query, (nombre_prueba,), fetch="one")
                if not prueba_result:
                    sg.popup("Error", f"No se encontró una prueba con el nombre '{nombre_prueba}'.")
                    continue
                id_prueba_postmortem = prueba_result[0]

                # Insertar
                query = """
                    INSERT INTO consulta_prueba_postmortem (id_consulta, id_prueba_postmortem, detalles, realizada, fecha_realizacion)
                    VALUES (%s, %s, %s, %s, %s)
                """
                filas_afectadas = db.execute_query(query, (id_consulta, id_prueba_postmortem, detalles, realizada, fecha_realizacion))
                if filas_afectadas:
                    sg.popup("Prueba postmortem registrada exitosamente", title="Éxito")

                    # Limpiar los campos después de guardar
                    for key in ["-ID_CONSULTA-", "-NOMBRE_PRUEBA-", "-FECHA-", "-DETALLES-", "-REALIZADA-"]:
                        window[key].update("")
                else:
                    sg.popup("Error al registrar la prueba postmortem.")

            except Exception as e:
                sg.popup(f"Error al guardar la prueba: {e}", title="Error")

    window.close()
    db.close()
