import PySimpleGUI as sg
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ui_config import sg

# Definición de la interfaz para el formulario de consulta
def consulta_interface():
    sg.theme('MyNewTheme')
    layout = [
        [sg.Text("Formulario de Consulta", font=("Helvetica", 18))],

        [sg.Text("ID Paciente", size=(15, 1)), sg.Input(key="-ID_PACIENTE-")],
        [sg.Text("ID Doctor", size=(15, 1)), sg.Input(key="-ID_DOCTOR-")],
        [sg.Text("Diagnóstico Provisional", size=(15, 1)), sg.Multiline(key="-DIAGNOSTICO-", size=(40, 3))],
        [sg.Text("Tratamiento Prescrito", size=(15, 1)), sg.Multiline(key="-TRATAMIENTO-", size=(40, 3))],
        [sg.Text("Observaciones", size=(15, 1)), sg.Multiline(key="-OBSERVACIONES-", size=(40, 3))],
        [sg.Text("Estado de Consulta", size=(15, 1)), sg.Combo(["Abierta", "En proceso", "Cerrada"], key="-ESTADO-", default_value="Abierta")],
        
        [sg.Button("Guardar Consulta", size=(20, 1)), sg.Button("Volver", size=(20, 1))]
    ]
    return sg.Window("Formulario de Consulta", layout, size=(600, 500), finalize=True)

# BLOQUE PARA PRUEBAS
#"""
if __name__ == "__main__":
    window = consulta_interface()
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Salir"):
            break
    window.close()#"""
# FIN DEL BLOQUE PARA PRUEBAS