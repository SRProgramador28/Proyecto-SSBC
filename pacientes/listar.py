import PySimpleGUI as sg
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ui_config import sg

# Definición de la interfaz para listar pacientes
def listar_paciente_interface():
    sg.theme('MyNewTheme')
    layout = [
        [sg.Text("Listado de Pacientes", font=("Helvetica", 20), justification='center')],
        #[sg.Multiline(default_text=pacientes, size=(60, 15), disabled=True, key="-LISTADO-")],
        [sg.Button("Volver", size=(15, 1))]
    ]
    return sg.Window("Listar Pacientes", layout, size=(600, 400), element_justification='c', finalize=True)

# BLOQUE PARA PRUEBAS
"""
if __name__ == "__main__":
    window = listar_paciente_interface()
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Salir"):
            break
    window.close()"""
# FIN DEL BLOQUE PARA PRUEBAS