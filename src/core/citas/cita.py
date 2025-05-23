from ui_config import sg
from database.singleton import DatabaseManagerSingleton
from datetime import datetime

# Definición de la interfaz para el registro de citas
def cita_interface():
    sg.theme('My New Theme')
    db = DatabaseManagerSingleton.get_instance()

    # Listar pacientes y doctores
    try:
        queryP = "SELECT id_paciente, nombre, apellido from pacientes"
        pacientes_result = db.execute_query(queryP)

        queryD = "SELECT id_doctor, nombre, especialidad FROM doctores"
        doctores_result = db.execute_query(queryD)

        pacientes = {f"{r[1]} {r[2]}": r[0] for r in pacientes_result}
        doctores = {f"{r[1]} - {r[2]}": r[0] for r in doctores_result}
    except Exception as e:
        sg.popup_error(f"Error al cargar datos: {e}")
        return

    layout = [
        [sg.Text("Registrar Nueva Cita", font=("Helvetica", 20), justification='center', expand_x=True)],

        [sg.Frame("Detalles", [
            [sg.Text("Paciente", size=(20, 1)), sg.Combo(list(pacientes.keys()), key="-PACIENTE-", size=(40, 1))],
            [sg.Text("Doctor", size=(20, 1)), sg.Combo(list(doctores.keys()), key="-DOCTOR-", size=(40, 1))],
            [sg.Text("Fecha de Cita", size=(20, 1)), sg.Input(default_text=datetime.today().strftime('%Y-%m-%d %H:%M:%S'), key="-FECHA-", size=(40, 1))],
            [sg.Text("Motivo de la Cita", size=(20, 1)), sg.Multiline(key="-MOTIVO-", size=(40, 3))],
            [sg.Text("Observaciones", size=(20, 1)), sg.Multiline(key="-OBSERVACIONES-", size=(40, 3))],
            [sg.Text("Estado", size=(20, 1)), sg.Combo(["Pendiente", "Confirmada", "Cancelada", "Reprogramada", "Completada"], key="-ESTADO-", default_value="Pendiente")], 
        ])],

        [sg.Button("Registrar", size=(20, 1)), sg.Button("Volver", size=(20, 1))]
    ]
    
    window = sg.Window("Registro de Citas", layout, size=(600, 500), element_justification='c', finalize=True)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Volver"):
            break

        elif event == "Registrar":
            paciente = values["-PACIENTE-"]
            doctor = values["-DOCTOR-"]
            fecha_cita = values["-FECHA-"]
            motivo = values["-MOTIVO-"]
            observaciones = values["-OBSERVACIONES-"]
            estado = values["-ESTADO-"]

            if not all([paciente, doctor, fecha_cita, estado]):
                sg.popup("Error", "Por favor, complete todos los campos obligatorios.")
                continue

            try:
                id_paciente = pacientes[paciente]
                id_doctor = doctores[doctor]

                query = """
                INSERT INTO citas (id_paciente, id_doctor, fecha_hora, motivo, estado, observaciones)
                VALUES (%s, %s, %s, %s, %s, %s)
                """
                parametros = (id_paciente, id_doctor, fecha_cita, motivo, estado, observaciones)
                filas = db.execute_query(query, parametros)

                if filas:
                    sg.popup("Cita registrada exitosamente", title="Éxito")
            except Exception as e:
                sg.popup(f"Error al registrar la cita: {e}", title="Error")

    window.close()
    db.close()
