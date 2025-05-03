from ui_config import sg
from database.singleton import DatabaseManagerSingleton

# Definición de la interfaz para editar citas
def editar_cita_interface():
    sg.theme('My New Theme')
    db = DatabaseManagerSingleton.get_instance()

    layout = [
        [sg.Text("Modificar Cita", font=("Helvetica", 20), justification="center", expand_x=True)],
        [sg.Frame("Buscar", [
             [sg.Text("Código de la Cita", size=(20, 1)), sg.Input(key="-CITA_ID-", size=(30, 1)), sg.Button("Buscar", size=(10,1))],
        ])],
        [sg.HorizontalSeparator()],
        [sg.Frame("Modificar Datos", [
             [sg.Text("Fecha de Cita", size=(20, 1)), sg.Input(key="-FECHA-", size=(30, 1))],
             [sg.Text("Motivo de la Cita", size=(20, 1)), sg.Multiline(key="-MOTIVO-", size=(40, 3))],
             [sg.Text("Observaciones", size=(20, 1)), sg.Multiline(key="-OBSERVACIONES-", size=(40, 3))],
             [sg.Text("Estado", size=(20, 1)), sg.Combo(["Pendiente", "Confirmada", "Cancelada", "Reprogramada", "Completada"], key="-ESTADO-", size=(30,1))],
        ])],
        [sg.Button("Guardar Cambios", size=(20, 1)), sg.Button("Volver", size=(20, 1))]
    ]

    window = sg.Window("Editar Cita", layout, size=(600, 500), element_justification='c', finalize=True)

    cita_actual = None

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Volver"):
            break

        elif event == "Buscar":
            cita_id = values["-CITA_ID-"]
            if not cita_id:
                sg.popup("Ingrese el código de la cita para buscar.")
                continue

            try:
                query = "SELECT * FROM citas WHERE id_cita = %s"
                result = db.fetch_one(query, (cita_id,))
                if result:
                    cita_actual = result
                    window["-FECHA-"].update(value=result['fecha_hora'].strftime('%Y-%m-%d %H:%M:%S'))
                    window["-MOTIVO-"].update(value=result['motivo'] or "")
                    window["-OBSERVACIONES-"].update(value=result['observaciones'] or "")
                    window["-ESTADO-"].update(value=result['estado'])
                else:
                    sg.popup("No se encontró una cita con ese código.")
            except Exception as e:
                sg.popup_error(f"Error al buscar la cita: {e}")

        elif event == "Guardar Cambios":
            if not cita_actual:
                sg.popup("Primero busque una cita para modificar.")
                continue

            nueva_fecha = values["-FECHA-"]
            nuevo_motivo = values["-MOTIVO-"]
            nuevas_observaciones = values["-OBSERVACIONES-"]
            nuevo_estado = values["-ESTADO-"]

            if not all([nueva_fecha, nuevo_estado]):
                sg.popup("Debe llenar los campos obligatorios (Fecha y Estado).")
                continue

            try:
                update_query = """
                UPDATE citas
                SET fecha_hora = %s, motivo = %s, observaciones = %s, estado = %s
                WHERE id_cita = %s
                """
                filas = db.execute_query(update_query, (
                    nueva_fecha, nuevo_motivo, nuevas_observaciones, nuevo_estado, cita_actual['id_cita']
                ))
                if filas:
                    sg.popup("Cita actualizada exitosamente.", title="Éxito")
                    # Limpiar formulario después de guardar
                    for key in ("-CITA_ID-", "-FECHA-", "-MOTIVO-", "-OBSERVACIONES-", "-ESTADO-"):
                        window[key].update("")
                    cita_actual = None
            except Exception as e:
                sg.popup_error(f"Error al actualizar la cita: {e}")

    window.close()
    db.close()
