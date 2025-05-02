from ui_config import sg
from database.singleton import DatabaseManagerSingleton

# Definición de la interfaz para el registro de pacientes
def registro_interface():
    sg.theme('My New Theme')
    layout = [
        [sg.Text("Registro de Paciente", font=("Helvetica", 20), justification='center', expand_x=True)],
        [sg.Frame("Datos Personales", [
            [sg.Text("Nombre", size=(20, 1)), sg.Input(key="-NOMBRE-")],
            [sg.Text("Apellido", size=(20, 1)), sg.Input(key="-APELLIDO-")],
            [sg.Text("Edad", size=(20, 1)), sg.Input(key="-EDAD-")],
            [sg.Text("Sexo", size=(20, 1)), sg.Combo(["Masculino", "Femenino", "Otro"], key="-SEXO-")],
            [sg.Text("Peso (kg)", size=(20, 1)), sg.Input(key="-PESO-")],
            [sg.Text("Altura (m)", size=(20, 1)), sg.Input(key="-ALTURA-")],
            [sg.Text("Grupo Sanguíneo", size=(20, 1)), sg.Combo(["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"], key="-GRUPO-")],
            [sg.Text("Alergias", size=(20, 1)), sg.Multiline(key="-ALERGIAS-", size=(40, 3))],
            [sg.Text("Enfermedades Crónicas", size=(20, 1)), sg.Multiline(key="-ENFERMEDADES-", size=(40, 3))],
        ])],
        [sg.Button("Registrar", size=(20, 1)), sg.Button("Volver", size=(20, 1))]
    ]
    window = sg.Window("Registro de Pacientes", layout, size=(600, 500), element_justification='c', finalize=True)
    db = DatabaseManagerSingleton.get_instance()

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Volver"):
            break

        elif event == "Registrar":
            nombre = values["-NOMBRE-"]
            apellido = values["-APELLIDO-"]
            edad = values["-EDAD-"]
            sexo = values["-SEXO-"]
            peso = values["-PESO-"]
            altura = values["-ALTURA-"]
            grupo_sanguineo = values["-GRUPO-"]
            alergias = values["-ALERGIAS-"]
            enfermedades_cronicas = values["-ENFERMEDADES-"]

            if not all([nombre, apellido, edad, sexo]):
                sg.popup("Error", "Por favor, complete los campos obligatorios.")
                continue

            try:
                query = """
                INSERT INTO pacientes (nombre, apellido, edad, sexo, peso, altura, grupo_sanguineo, alergias, enfermedades_cronicas)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                filas = db.execute_query(query, (
                    nombre, apellido, edad, sexo, peso,
                    altura, grupo_sanguineo, alergias, enfermedades_cronicas
                ))
                if filas:
                    sg.popup("Paciente registrado exitosamente", title="Éxito")
            except Exception as e:
                sg.popup(f"Error al registrar paciente: {e}", title="Error")

    window.close()
    db.close()

