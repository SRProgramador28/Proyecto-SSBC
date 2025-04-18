import PySimpleGUI as sg
from datetime import datetime
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ui_config import sg

# Definición de la interfaz para el registro de citas
def cita_interface():
    sg.theme('My New Theme')
    layout = [
        [sg.Text("Registrar Nueva Cita", font=("Helvetica", 20), justification='center', expand_x=True)],
        
        [sg.Text("Paciente", size=(20, 1)), sg.InputCombo(values=[], key="-PACIENTE-", size=(30, 1))],
        [sg.Text("Doctor", size=(20, 1)), sg.InputCombo(values=[], key="-DOCTOR-", size=(30, 1))],
        [sg.Text("Fecha de Consulta", size=(20, 1)), sg.Input(default_text=datetime.today().strftime('%Y-%m-%d'), key="-FECHA-")],
        [sg.Text("Diagnóstico Provisional", size=(20, 1)), sg.Multiline(key="-DIAGNOSTICO-", size=(40, 3))],
        [sg.Text("Tratamiento Prescrito", size=(20, 1)), sg.Multiline(key="-TRATAMIENTO-", size=(40, 3))],
        [sg.Text("Observaciones", size=(20, 1)), sg.Multiline(key="-OBSERVACIONES-", size=(40, 3))],
        [sg.Text("Estado", size=(20, 1)), sg.Combo(["Pendiente", "Realizada", "Cancelada"], key="-ESTADO-")],
        
        [sg.Button("Enviar", size=(20, 1)), sg.Button("Volver", size=(20, 1))]
    ]
    return sg.Window("Registro de Citas", layout, size=(650, 600), finalize=True)


# BLOQUE PARA PRUEBAS
"""
if __name__ == "__main__":
    window = cita_interface()
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Salir"):
            break
    window.close()"""
# FIN DEL BLOQUE PARA PRUEBAS
