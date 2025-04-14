import PySimpleGUI as sg
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ui_config import sg

# Definición de la interfaz para editar citas
def editar_cita_interface():
    layout = [
        [sg.Text("Modificar Cita", font=("Helvetica", 20))],
        [sg.Text("Código de la cita", font=("Helvetica", 12))],
        [sg.Input(key="-CITA_ID-", font=("Arial", 12), size=(30, 1))],
        [sg.Button("Buscar", font=("Helvetica", 12))],
        [sg.Text("Nombre", font=("Helvetica", 12))],
        [sg.Input(key="-NAME-", font=("Arial", 12), size=(30, 1))],
        [sg.Text("Apellido", font=("Helvetica", 12))],
        [sg.Input(key="-LASTNAME-", font=("Arial", 12), size=(30, 1))],
        [sg.Text("Fecha de cita", font=("Helvetica", 12))],
        [sg.Input(key="-DATE-", font=("Arial", 12), size=(30, 1))],
        [sg.Button("Guardar Cambios", size=(20, 1)), sg.Button("Volver", size=(20, 1))]
    ]
    return sg.Window("Editar Cita", layout, size=(600, 500), element_justification='c', finalize=True)

# BLOQUE PARA PRUEBAS
"""
if __name__ == "__main__":
    window = editar_cita_interface()
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Salir"):
            break
    window.close()"""
# FIN DEL BLOQUE PARA PRUEBAS