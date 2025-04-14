from ui_config import sg

# Definición de la interfaz para el registro de pacientes
def registro_interface():
    sg.theme('My New Theme')
    layout = [
        [sg.Text("Registro de Paciente", font=("Helvetica", 20), justification='center', expand_x=True)],
        
        [sg.Text("Nombre", size=(20, 1)), sg.Input(key="-NOMBRE-")],
        [sg.Text("Edad", size=(20, 1)), sg.Input(key="-EDAD-")],
        [sg.Text("Sexo", size=(20, 1)), sg.Combo(["Masculino", "Femenino", "Otro"], key="-SEXO-")],
        [sg.Text("Peso (kg)", size=(20, 1)), sg.Input(key="-PESO-")],
        [sg.Text("Altura (m)", size=(20, 1)), sg.Input(key="-ALTURA-")],
        [sg.Text("Grupo Sanguíneo", size=(20, 1)), sg.Combo(["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"], key="-GRUPO-")],
        [sg.Text("Alergias", size=(20, 1)), sg.Multiline(key="-ALERGIAS-", size=(40, 3))],
        [sg.Text("Enfermedades Crónicas", size=(20, 1)), sg.Multiline(key="-ENFERMEDADES-", size=(40, 3))],
        
        [sg.Button("Enviar", size=(20, 1)), sg.Button("Volver", size=(20, 1))]
    ]
    return sg.Window("Registro de Pacientes", layout, size=(600, 500), finalize=True)

# BLOQUE PARA PRUEBAS
"""
if __name__ == "__main__":
    window = registro_interface()
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Salir"):
            break
    window.close()"""
# FIN DEL BLOQUE PARA PRUEBAS
