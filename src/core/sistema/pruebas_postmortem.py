import PySimpleGUI as sg
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ui_config import sg

# Definición de la interfaz para las pruebas post mortem
def pruebas_postmortem_interface():
    layout = [
        [sg.Text("Registro de Pruebas Postmortem", font=("Helvetica", 18))],
        
        [sg.Text("ID Consulta", size=(18, 1)), sg.Input(key="-ID_CONSULTA-")],
        [sg.Text("Fecha de Realización", size=(18, 1)), sg.Input(key="-FECHA-", size=(20,1)), sg.CalendarButton("Seleccionar Fecha", target="-FECHA-", format="%Y-%m-%d")],
        [sg.Text("Detalles", size=(18, 1)), sg.Multiline(key="-DETALLES-", size=(45, 5))],

        [sg.Button("Guardar Prueba", size=(20, 1)), sg.Button("Volver", size=(20, 1))]
    ]
    return sg.Window("Pruebas Postmortem", layout, size=(600, 400), finalize=True)

# BLOQUE PARA PRUEBAS
"""
if __name__ == "__main__":
    window = pruebas_postmortem_interface()
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Salir"):
            break
    window.close()"""
# FIN DEL BLOQUE PARA PRUEBAS