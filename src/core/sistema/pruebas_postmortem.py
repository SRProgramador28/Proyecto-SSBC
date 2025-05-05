from ui_config import sg
from database.singleton import DatabaseManagerSingleton

# Definición de la interfaz para las pruebas postmortem
def pruebas_postmortem_interface():
    sg.theme('MyNewTheme')
    db = DatabaseManagerSingleton.get_instance()

    try:
        pruebas_query = "SELECT id_prueba_postmortem, nombre_prueba, descripcion FROM pruebas_postmortem ORDER BY nombre_prueba"
        pruebas_result = db.execute_query(pruebas_query)
        pruebas_lista = [r[1] for r in pruebas_result]  # Lista de nombres de pruebas
        pruebas_dict = {r[1]: r[0] for r in pruebas_result}  # Diccionario de pruebas nombre -> id
    except Exception as e:
        sg.popup(f"Error al cargar la lista de pruebas: {e}")
        pruebas_lista = []
        pruebas_dict = {}

    layout = [
        [sg.Text("Registro de Pruebas Postmortem", font=("Helvetica", 18), justification='center', expand_x=True)],

        [sg.Frame("Buscar Consulta", [
            [sg.Text("ID Consulta:", size=(15, 1)), sg.Input(key="-ID_CONSULTA-", size=(15, 1)), 
             sg.Button("Verificar", key="-VERIFICAR-", size=(10, 1))]
        ])],

        [sg.Frame("Información de la Consulta", [
            [sg.Text("Paciente:", size=(15, 1)), sg.Text("", key="-INFO_PACIENTE-", size=(30, 1))],
            [sg.Text("Doctor:", size=(15, 1)), sg.Text("", key="-INFO_DOCTOR-", size=(30, 1))],
            [sg.Text("Fecha consulta:", size=(15, 1)), sg.Text("", key="-FECHA_CONSULTA-", size=(30, 1))]
        ])],

        [sg.Frame("Datos de la Prueba", [
            [sg.Text("Tipo de Prueba:", size=(15, 1)), sg.Combo(pruebas_lista, key="-NOMBRE_PRUEBA-", size=(30, 1), 
                    enable_events=True, readonly=True)],
            [sg.Text("Descripción:", size=(15, 1)), sg.Multiline(key="-DESCRIPCION-", size=(45, 3), disabled=True)],
            [sg.Text("Fecha Realización:", size=(15, 1)), sg.Input(key="-FECHA-", size=(20, 1)), 
             sg.CalendarButton("Seleccionar", target="-FECHA-", format="%Y-%m-%d", size=(10, 1))],
            [sg.Text("Detalles:", size=(15, 1)), sg.Multiline(key="-DETALLES-", size=(45, 5))],
            [sg.Text("Prueba Realizada:", size=(15, 1)), sg.Checkbox("", default=False, key="-REALIZADA-")]
        ])],

        [sg.Button("Guardar Prueba", size=(20, 1)), sg.Button("Limpiar", key="-LIMPIAR-", size=(15, 1)), sg.Button("Volver", size=(15, 1))]
    ]

    window = sg.Window("Pruebas Postmortem", layout, size=(650, 600), element_justification='c', finalize=True)

    def limpiar_campos():
        for key in ["-NOMBRE_PRUEBA-", "-FECHA-", "-DETALLES-", "-REALIZADA-"]:
            window[key].update("")
        window["-DESCRIPCION-"].update("")
        window["-INFO_PACIENTE-"].update("")
        window["-INFO_DOCTOR-"].update("")
        window["-FECHA_CONSULTA-"].update("")
        window["-REALIZADA-"].update(False)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Volver"):
            break

        elif event == "-NOMBRE_PRUEBA-":
            # Actualizar descripción cuando se selecciona una prueba
            nombre_prueba = values["-NOMBRE_PRUEBA-"]
            if nombre_prueba and nombre_prueba in pruebas_dict:
                # Obtener descripción desde el diccionario precargado
                _, descripcion = pruebas_dict[nombre_prueba]
                window["-DESCRIPCION-"].update(descripcion or "Sin descripción disponible")
                    
        elif event == "-VERIFICAR-":
            id_consulta = values["-ID_CONSULTA-"].strip()
            if not id_consulta:
                sg.popup("Por favor, ingrese un ID de consulta válido")
                continue
                
            try:
                # Verificar si existe la consulta y obtener datos del paciente y doctor
                query = """
                SELECT c.id_paciente, CONCAT(p.nombre, ' ', p.apellido) AS nombre_paciente,
                       d.nombre AS nombre_doctor, d.especialidad, c.fecha_consulta 
                FROM consultas c
                JOIN pacientes p ON c.id_paciente = p.id_paciente
                JOIN doctores d ON c.id_doctor = d.id_doctor
                WHERE c.id_consulta = %s
                """
                result = db.execute_query(query, (id_consulta,), fetch="one")
                
                if result:
                    window["-INFO_PACIENTE-"].update(result[1])
                    window["-INFO_DOCTOR-"].update(f"{result[2]} ({result[3]})")
                    
                    # Formatear fecha
                    fecha_consulta = result[4]
                    if isinstance(fecha_consulta, str):
                        window["-FECHA_CONSULTA-"].update(fecha_consulta)
                    else:
                        window["-FECHA_CONSULTA-"].update(fecha_consulta.strftime('%Y-%m-%d'))
                else:
                    sg.popup("No se encontró la consulta especificada")
                    window["-INFO_PACIENTE-"].update("")
                    window["-INFO_DOCTOR-"].update("")
                    window["-FECHA_CONSULTA-"].update("")
            except Exception as e:
                sg.popup_error(f"Error al verificar consulta: {e}")
                
        elif event == "-LIMPIAR-":
            limpiar_campos()
            
        elif event == "Guardar Prueba":
            id_consulta = values["-ID_CONSULTA-"].strip()
            nombre_prueba = values["-NOMBRE_PRUEBA-"]
            fecha_realizacion = values["-FECHA-"].strip()
            detalles = values["-DETALLES-"].strip()
            realizada = values["-REALIZADA-"]
            
            # Validar campos
            if not id_consulta or not nombre_prueba or not fecha_realizacion:
                sg.popup("Error", "Por favor, complete los campos obligatorios (ID Consulta, Tipo de Prueba y Fecha).")
                continue
                
            # Validar si la consulta tiene información cargada
            if not window["-INFO_PACIENTE-"].get():
                sg.popup("Error", "Por favor, verifique primero el ID de consulta.")
                continue
                
            try:
                # Obtener ID de la prueba desde el diccionario
                if nombre_prueba not in pruebas_dict:
                    sg.popup("Error", "Prueba no encontrada en la base de datos.")
                    continue
                    
                id_prueba, _ = pruebas_dict[nombre_prueba]
                    
                # Verificar si ya existe esta prueba para esta consulta
                check_query = """
                SELECT 1 FROM consulta_prueba_postmortem 
                WHERE id_consulta = %s AND id_prueba_postmortem = %s
                """
                existe = db.execute_query(check_query, (id_consulta, id_prueba), fetch="one")
                
                if existe:
                    # Actualizar registro existente
                    update_query = """
                    UPDATE consulta_prueba_postmortem 
                    SET detalles = %s, realizada = %s, fecha_realizacion = %s
                    WHERE id_consulta = %s AND id_prueba_postmortem = %s
                    """
                    db.execute_query(update_query, (detalles, realizada, fecha_realizacion, 
                                                  id_consulta, id_prueba), fetch=None)
                    sg.popup("Prueba postmortem actualizada exitosamente", title="Éxito")
                else:
                    # Insertar nuevo registro
                    insert_query = """
                    INSERT INTO consulta_prueba_postmortem 
                    (id_consulta, id_prueba_postmortem, detalles, realizada, fecha_realizacion)
                    VALUES (%s, %s, %s, %s, %s)
                    """
                    db.execute_query(insert_query, (id_consulta, id_prueba, detalles, 
                                                   realizada, fecha_realizacion), fetch=None)
                    sg.popup("Prueba postmortem registrada exitosamente", title="Éxito")
                
                # Limpiar solo los campos de la prueba después de guardar
                window["-NOMBRE_PRUEBA-"].update("")
                window["-DESCRIPCION-"].update("")
                window["-FECHA-"].update("")
                window["-DETALLES-"].update("")
                window["-REALIZADA-"].update(False)
                
            except Exception as e:
                sg.popup_error(f"Error al guardar la prueba: {e}")
    
    window.close()
    db.close()
