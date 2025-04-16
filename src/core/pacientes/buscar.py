import PySimpleGUI as sg
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ui_config import sg

# Definición de la interfaz para buscar pacientes
def buscar_paciente_interface():
    sg.theme('MyNewTheme')
    layout = [
        [sg.Text("Buscar Paciente", font=("Helvetica", 20), justification='center')],
        [sg.Text("Código o Nombre del Paciente:", size=(25, 1))],
        [sg.Input(key="-BUSCAR-", size=(30, 1))],
        [sg.Button("Buscar", size=(15, 1))],
        [sg.Text("Resultado:", font=("Helvetica", 12))],
        [sg.Multiline(key="-RESULTADO-", size=(60, 10), disabled=True)],
        [sg.Button("Volver", size=(15, 1))]
    ]
    return sg.Window("Buscar Paciente", layout, size=(600, 400), element_justification='c', finalize=True)

# BLOQUE PARA PRUEBAS
""""
if __name__ == "__main__":
    window = buscar_paciente_interface()
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Salir"):
            break
    window.close()"""
# FIN DEL BLOQUE PARA PRUEBAS