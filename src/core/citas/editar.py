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

        [sg.Frame("Información de la Cita", [
                [sg.Text("Paciente", size=(20, 1)), sg.Text(key="-INFO_PACIENTE-", size=(30, 1))],
                [sg.Text("Doctor", size=(20, 1)), sg.Text(key="-INFO_DOCTOR-", size=(30, 1))],
        ])],

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
            cita_id = values["-CITA_ID-"].strip()
            if not cita_id:
                sg.popup("Ingrese el código de la cita para buscar.")
                continue

            try:
                query = """
                SELECT id_cita, fecha_hora, motivo, observaciones, estado, nombre_completo_paciente, nombre_doctor, especialidad
                FROM vista_citas
                WHERE id_cita = %s
                """
                resultado = db.execute_query(query, (cita_id,),  fetch="one")

                if resultado:
                    cita_actual = resultado[0]

                    fecha_hora = resultado[1]
                    if isinstance(fecha_hora, str):
                        window["-FECHA-"].update(value=fecha_hora)
                    else:
                        window["-FECHA-"].update(value=fecha_hora.strftime("%Y-%m-%d %H:%M"))

                    window["-MOTIVO-"].update(value=resultado[2] or "")
                    window["-OBSERVACIONES-"].update(value=resultado[3] or "")
                    window["-ESTADO-"].update(value=resultado[4])

                    window["-INFO_PACIENTE-"].update(value=resultado[5])
                    window["-INFO_DOCTOR-"].update(value=f"{resultado[6]} ({resultado[7]})")
                else:
                    sg.popup("Cita no encontrada.")
                    
                    for key in ["-FECHA-", "-MOTIVO-", "-OBSERVACIONES-", "-ESTADO-", "-INFO_PACIENTE-", "-INFO_DOCTOR-"]:
                        window[key].update(value="")
                    cita_actual = None

            except Exception as e:
                sg.popup_error(f"Error al buscar la cita: {e}")
                
        elif event == "Guardar Cambios":
            if not cita_actual:
                sg.popup("No hay cita seleccionada para modificar.")
                continue

            nueva_fecha = values["-FECHA-"].strip()
            nuevo_motivo = values["-MOTIVO-"].strip()
            nuevas_observaciones = values["-OBSERVACIONES-"].strip()
            nuevo_estado = values["-ESTADO-"]

            if not nueva_fecha or not nuevo_estado:
                sg.popup("Por favor, complete todos los campos obligatorios.")
                continue

            try:
                update_query = """
                UPDATE citas
                SET fecha_hora = %s, motivo = %s, observaciones = %s, estado = %s
                WHERE id_cita = %s
                """
                db.execute_query(update_query, (
                    nueva_fecha,
                    nuevo_motivo,
                    nuevas_observaciones,
                    nuevo_estado,
                    cita_actual
                ), fetch="none")

                sg.popup("Cita modificada exitosamente.", title="Éxito")

                for key in ["-FECHA-", "-MOTIVO-", "-OBSERVACIONES-", "-ESTADO-", "-INFO_PACIENTE-", "-INFO_DOCTOR-"]:
                    window[key].update("")
                cita_actual = None

            except Exception as e:
                sg.popup_error(f"Error al actualizar la cita: {e}")


    window.close()
    db.close()
