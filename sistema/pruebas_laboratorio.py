import PySimpleGUI as sg
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ui_config import sg

# Definición de la interfaz de las pruebas de laboratorio
def pruebas_laboratorio_interface():
    layout = [
        [sg.Text("Registro de Pruebas de Laboratorio", font=("Helvetica", 18))],
        
        [sg.Text("ID Consulta", size=(18, 1)), sg.Input(key="-ID_CONSULTA-")],
        [sg.Text("Nombre de la Prueba", size=(18, 1)), sg.Input(key="-NOMBRE_PRUEBA-")],
        [sg.Text("Fecha de Realización", size=(18, 1)), sg.Input(key="-FECHA-", size=(20,1)), sg.CalendarButton("Seleccionar Fecha", target="-FECHA-", format="%Y-%m-%d")],
        [sg.Text("Resultado", size=(18, 1)), sg.Multiline(key="-RESULTADO-", size=(45, 3))],
        [sg.Text("Detalles Adicionales", size=(18, 1)), sg.Multiline(key="-DETALLES-", size=(45, 3))],

        [sg.Button("Guardar Prueba", size=(20, 1)), sg.Button("Volver", size=(20, 1))]
    ]
    return sg.Window("Pruebas de Laboratorio", layout, size=(600, 450), finalize=True)

# BLOQUE PARA PRUEBAS
"""
if __name__ == "__main__":
    window = pruebas_laboratorio_interface()
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Salir"):
            break
    window.close()"""
# FIN DEL BLOQUE PARA PRUEBAS