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
    
    return sg.Window("Editar Información", layout, size=(600, 500), finalize=True)

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
