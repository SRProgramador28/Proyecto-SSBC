from ui_config import sg
from database.singleton import DatabaseManagerSingleton

# Definición de la interfaz para el historial médico
def historial_interface():
    layout = [
        [sg.Text("Historial Médico de Pacientes", font=("Helvetica", 20), justification='center')],
        [sg.Frame("Buscar Paciente", [
            [sg.Text("ID o Nombre del Paciente:"), sg.Input(key="-BUSCAR-", size=(30, 1)),
                sg.Button("Buscar", key="-BUSCAR-BTN-")] 
        ])],

        [sg.Frame("Datos del Paciente", [
            [sg.Text("Nombre: ", size=(15, 1)), sg.Text("", size=(30, 1), key="-NOMBRE-")],
            [sg.Text("Edad: ", size=(15, 1)), sg.Text("", size=(30, 1), key="-EDAD-")],
            [sg.Text("Grupo Sanguíneo: ", size=(15, 1)), sg.Text("", size=(30, 1), key="-GRUPO-")],
            [sg.Text("Alergias: ", size=(15, 1)), sg.Text("", size=(30, 1), key="-ALERGIAS-")],
            [sg.Text("Enf. Crónicas: ", size=(15, 1)), sg.Text("", size=(30, 1), key="-CRONICAS-")]
        ])],

        [sg.Frame("Historial de Consultas", [
            [sg.Table(
                values=[],
                headings=["ID", "Fecha", "Doctor", "Especialidad", "Diagnóstico", "Estado"],
                auto_size_columns=False,
                col_widths=[5, 15, 15, 15, 25, 10],
                justification='left',
                num_rows=10,
                key="-HISTORIAL_TABLE-",
                enable_events=True
            )]
        ])],

        [sg.Button("Volver", size=(20, 1))]
    ]
    
    window = sg.Window("Historial Médico", layout, size=(850, 570), element_justification='center', finalize=True)
    db = DatabaseManagerSingleton.get_instance()

    def cargar_historial_paciente(id_paciente):
        try:
            query_paciente = """
            SELECT nombre, apellido, edad, grupo_sanguineo, alergias, enfermedades_cronicas 
            FROM pacientes 
            WHERE id_paciente = %s
            """
            paciente_info = db.execute_query(query_paciente, (id_paciente,))
            
            if paciente_info:
                paciente = paciente_info[0]
                window["-NOMBRE-"].update(f"{paciente[0]} {paciente[1]}")
                window["-EDAD-"].update(paciente[2])
                window["-GRUPO-"].update(paciente[3] if paciente[3] else "No registrado")
                window["-ALERGIAS-"].update(paciente[4] if paciente[4] else "Ninguna")
                window["-CRONICAS-"].update(paciente[5] if paciente[5] else "Ninguna")
                
                # Cargar historial usando la vista historial_paciente
                query_historial = """
                SELECT id_consulta, fecha_consulta, nombre_doctor, especialidad, diagnostico, estado
                FROM historial_paciente 
                WHERE id_paciente = %s
                ORDER BY fecha_consulta DESC
                """
                historial = db.execute_query(query_historial, (id_paciente,))
                
                # Formatear los datos para la tabla
                historial_data = []
                for consulta in historial:
                    historial_data.append([
                        consulta[0],  # ID consulta
                        consulta[1].strftime("%Y-%m-%d %H:%M") if consulta[1] else "N/A",  # Fecha formateada
                        consulta[2],  # Nombre doctor
                        consulta[3],  # Especialidad
                        consulta[4] if consulta[4] else "Sin diagnóstico",  # Diagnóstico
                        consulta[5]   # Estado
                    ])
                
                window["-HISTORIAL_TABLE-"].update(values=historial_data)
                return True
            else:
                sg.popup("Error", "Paciente no encontrado")
                return False
                
        except Exception as e:
            sg.popup_error(f"Error al cargar historial: {str(e)}")
            return False
    
    
    def buscar_paciente(busqueda):
        try:
            # Buscar primero por ID
            if busqueda.isdigit():
                query = "SELECT id_paciente FROM pacientes WHERE id_paciente = %s"
                resultado = db.execute_query(query, (busqueda,))
                if resultado:
                    return resultado[0][0]
            
            # Buscar por nombre
            query = """
            SELECT id_paciente FROM pacientes 
            WHERE CONCAT(nombre, ' ', apellido) LIKE %s 
            LIMIT 1
            """
            resultado = db.execute_query(query, (f"%{busqueda}%",))
            
            if resultado:
                return resultado[0][0]
            else:
                sg.popup("Paciente no encontrado")
                return None
                
        except Exception as e:
            sg.popup_error(f"Error al buscar paciente: {str(e)}")
            return None
    
    
    while True:
        event, values = window.read()
        
        if event in (sg.WIN_CLOSED, "Volver"):
            break
            
        elif event == "-BUSCAR-BTN-":
            if values["-BUSCAR-"].strip():
                id_paciente = buscar_paciente(values["-BUSCAR-"].strip())
                if id_paciente:
                    cargar_historial_paciente(id_paciente)
            else:
                sg.popup("Por favor ingrese un ID o nombre de paciente")
    
    window.close()
    db.close()
    return None
