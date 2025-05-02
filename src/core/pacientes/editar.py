from ui_config import sg
from database.singleton import DatabaseManagerSingleton

# Definición de la interfaz para editar información de pacientes
def editar_paciente_interface():
    sg.theme('MyNewTheme')

    layout = [
        [sg.Text("Editar Paciente", font=("Helvetica", 20))],
        [sg.Frame("Buscar", [
            [sg.Text("Código del Paciente"), sg.Input(key="-CODE-", size=(20, 1)), sg.Button("Buscar")]
        ])],
        [sg.HorizontalSeparator()],
        [sg.Frame("Detalles del Paciente", [
            [sg.Text("Nombre"), sg.Input(key="-NAME-", size=(30, 1), disabled=True)],
            [sg.Text("Apellido"), sg.Input(key="-LASTNAME-", size=(30, 1), disabled=True)],
            [sg.Text("Edad"), sg.Input(key="-AGE-", size=(10, 1), disabled=True)],
            [sg.Text("Sexo"), sg.Combo(["Masculino", "Femenino"], key="-SEX-", disabled=True)],
            [sg.Text("Peso (kg)"), sg.Input(key="-WEIGHT-", size=(10, 1), disabled=True)],
            [sg.Text("Altura (m)"), sg.Input(key="-HEIGHT-", size=(10, 1), disabled=True)],
            [sg.Text("Grupo Sanguíneo"), sg.Combo(["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"], key="-BLOOD-", disabled=True)],
            [sg.Text("Alergias"), sg.Multiline(key="-ALLERGIES-", size=(40, 3), disabled=True)],
            [sg.Text("Enfermedades Crónicas"), sg.Multiline(key="-DISEASES-", size=(40, 3), disabled=True)],
        ])],
        [sg.Button("Guardar Cambios", size=(20, 1), disabled=True), sg.Button("Volver", size=(20, 1))]
    ]
    window = sg.Window("Editar Información", layout, size=(600, 500), element_justification='c', finalize=True)
    db = DatabaseManagerSingleton.get_instance()
    codigo = None

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Volver"):
            break

        elif event == "Buscar":
            codigo = values["-CODE-"]
            if not codigo:
                sg.popup("Error", "Por favor, ingrese el código del paciente.")
                continue

            try:
                query = "SELECT * FROM pacientes WHERE id_paciente = %s"
                paciente = db.execute_query(query, params=(codigo,), fetch="one")

                if paciente:
                    window["-NAME-"].update(paciente[1], disabled=False)
                    window["-LASTNAME-"].update(paciente[2], disabled=False)
                    window["-AGE-"].update(paciente[3], disabled=False)
                    window["-SEX-"].update(paciente[4], disabled=False)
                    window["-WEIGHT-"].update(paciente[5], disabled=False)
                    window["-HEIGHT-"].update(paciente[6], disabled=False)
                    window["-BLOOD-"].update(paciente[7], disabled=False)
                    window["-ALLERGIES-"].update(paciente[8], disabled=False)
                    window["-DISEASES-"].update(paciente[9], disabled=False)
                    window["Guardar Cambios"].update(disabled=False)
                else:
                    sg.popup("Error", "No se encontró un paciente con ese código.")
            except Exception as e:
                sg.popup(f"Error al buscar paciente: {e}")

        elif event == "Guardar Cambios" and codigo:
            nombre = values["-NAME-"]
            apellido = values["-LASTNAME-"]
            edad = values["-AGE-"]
            sexo = values["-SEX-"]
            peso = values["-WEIGHT-"]
            altura = values["-HEIGHT-"]
            grupo_sanguineo = values["-BLOOD-"]
            alergias = values["-ALLERGIES-"]
            enfermedades_cronicas = values["-DISEASES-"]

            if not all([nombre, apellido, edad, sexo]):
                sg.popup("Error", "Por favor, complete todos los campos obligatorios.")
                continue

            try:
                query = """
                    UPDATE pacientes
                    SET nombre = %s, apellido = %s, edad = %s, sexo = %s, peso = %s, altura = %s,
                        grupo_sanguineo = %s, alergias = %s, enfermedades_cronicas = %s
                    WHERE id_paciente = %s
                """
                db.execute_query(query, (
                    nombre, apellido, edad, sexo, peso, altura,
                    grupo_sanguineo, alergias, enfermedades_cronicas, codigo
                ))
                sg.popup("Paciente actualizado exitosamente", title="Éxito")
            except Exception as e:
                sg.popup(f"Error al actualizar paciente: {e}", title="Error")

    window.close()
    db.close()
