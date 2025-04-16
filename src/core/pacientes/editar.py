import PySimpleGUI as sg
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ui_config import sg

# Definición de la interfaz para editar información de pacientes
def editar_paciente_interface():
    sg.theme('MyNewTheme')
    
    layout = [
        [sg.Text("Editar Paciente", font=("Helvetica", 20))],
        [sg.Text("Código del Paciente"), sg.Input(key="-CODE-", size=(20, 1)), sg.Button("Buscar")],
        [sg.HorizontalSeparator()],
        [sg.Text("Nombre"), sg.Input(key="-NAME-", size=(30, 1), disabled=True)],
        [sg.Text("Apellido"), sg.Input(key="-LASTNAME-", size=(30, 1), disabled=True)],
        [sg.Button("Guardar Cambios", size=(20, 1)), sg.Button("Volver", size=(20, 1))]
    ]

    window = sg.Window("Editar Paciente", layout, size=(500, 350), finalize=True)

# Lógica para editar la información del paciente
    pacientes = {
        "P001": {"nombre": "Juan", "apellido": "Pérez"},
        "P002": {"nombre": "Ana", "apellido": "García"},
    }

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Volver"):
            window.close()
            return "volver"

        if event == "Buscar":
            code = values["-CODE-"].strip()
            if code in pacientes:
                window["-NAME-"].update(pacientes[code]["nombre"], disabled=False)
                window["-LASTNAME-"].update(pacientes[code]["apellido"], disabled=False)
                window["Guardar Cambios"].update(disabled=False)
            else:
                sg.popup("Paciente no encontrado", f"No se encontró el código: {code}")

        if event == "Guardar Cambios":
            nuevo_nombre = values["-NAME-"]
            nuevo_apellido = values["-LASTNAME-"]
            sg.popup("Cambios guardados",
                     f"Nombre actualizado: {nuevo_nombre}",
                     f"Apellido actualizado: {nuevo_apellido}")

    window.close()
    return None

# BLOQUE PARA PRUEBAS
"""
if __name__ == "__main__":
    window = editar_paciente_interface()
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Salir"):
            break
    window.close()"""
# FIN DEL BLOQUE PARA PRUEBAS
