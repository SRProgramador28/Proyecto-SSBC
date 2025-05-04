from ui_config import sg
from database.singleton import DatabaseManagerSingleton

# Definición de la interfaz para buscar pacientes
def buscar_paciente_interface():
    sg.theme('MyNewTheme')
    
    layout = [
        [sg.Text("Buscar Paciente", font=("Helvetica", 20), justification='center')],

        [sg.Frame("Buscar", [
            [sg.Text("ID o Nombre del Paciente"), sg.Input(key="-BUSCAR-", size=(30, 1)), sg.Button("Buscar", key="-BUSCAR-BTN-")]
        ])],

        [sg.HorizontalSeparator()],

        [sg.Frame("Detalles del Paciente", [
            [sg.Text("Nombre"), sg.Input(key="-NAME-", size=(30, 1), disabled=True)],
            [sg.Text("Apellido"), sg.Input(key="-LASTNAME-", size=(30, 1), disabled=True)],
            [sg.Text("Edad"), sg.Input(key="-AGE-", size=(10, 1), disabled=True)],
            [sg.Text("Sexo"), sg.Input(key="-SEX-", size=(10, 1), disabled=True)],
            [sg.Text("Altura (m)"), sg.Input(key="-HEIGHT-", size=(10, 1), disabled=True)],
            [sg.Text("Grupo Sanguíneo"), sg.Input(key="-BLOOD-", size=(10, 1), disabled=True)],
            [sg.Text("Alergias"), sg.Multiline(key="-ALLERGIES-", size=(40, 3), disabled=True)],
            [sg.Text("Enfermedades Crónicas"), sg.Multiline(key="-DISEASES-", size=(40, 3), disabled=True)],
        ])],
        
        [sg.Button("Volver", size=(20, 1))]
    ]

    window = sg.Window("Buscar Paciente", layout, size=(600, 500), element_justification='c', finalize=True)
    db = DatabaseManagerSingleton.get_instance()

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Volver"):
            break
        elif event == "-BUSCAR-BTN-":
            criterio = values["-BUSCAR-"].strip()
            if not criterio:
                sg.popup("Error", "Por favor, ingrese el ID o Nombre del paciente.")
                continue

            if criterio.isdigit():
                query = """
                SELECT id_paciente, nombre, apellido, edad, sexo, direccion, altura, grupo_sanguineo, alergias, enfermedades_cronicas
                FROM pacientes WHERE id_paciente = %s
                """
                resultado = db.execute_query(query, (criterio,), fetch="one")
            else:
                query = """
                SELECT id_paciente, nombre, apellido, edad, sexo, direccion, altura, grupo_sanguineo, alergias, enfermedades_cronicas 
                FROM pacientes 
                WHERE CONCAT(nombre, ' ', apellido) LIKE %s 
                LIMIT 1
                """
                resultado = db.execute_query(query, (f"%{criterio}%",), fetch="one")

            if resultado:
                r = resultado
                window["-NAME-"].update(r[1])
                window["-LASTNAME-"].update(r[2])
                window["-AGE-"].update(str(r[3]))
                window["-SEX-"].update(r[4])
                window["-HEIGHT-"].update(str(r[6]) if r[6] else "")
                window["-BLOOD-"].update(r[7] if r[7] else "")
                window["-ALLERGIES-"].update(r[8] if r[8] else "")
                window["-DISEASES-"].update(r[9] if r[9] else "")
            else:
                sg.popup("Paciente no encontrado.")
                for key in ("-NAME-", "-LASTNAME-", "-AGE-", "-SEX-", "-HEIGHT-", "-BLOOD-", "-ALLERGIES-", "-DISEASES-"):
                    window[key].update("")

    window.close()
    db.close()
