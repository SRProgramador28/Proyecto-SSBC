import PySimpleGUI as sg
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ui_config import sg

# Definición de la interfaz para el historial médico
def historial_interface():
    layout = [
        [sg.Text("Historial de Consulta", font=("Helvetica", 20), justification='center')],
        
        [sg.Text("ID Paciente", size=(20, 1)), sg.Input(key="-IDPACIENTE-", size=(30, 1))],
        [sg.Text("ID Doctor", size=(20, 1)), sg.Input(key="-IDDOCTOR-", size=(30, 1))],
        [sg.Text("Diagnóstico Provisional", size=(20, 1)), sg.Multiline(key="-DIAGNOSTICO-", size=(30, 3))],
        [sg.Text("Tratamiento Prescrito", size=(20, 1)), sg.Multiline(key="-TRATAMIENTO-", size=(30, 3))],
        [sg.Text("Observaciones", size=(20, 1)), sg.Multiline(key="-OBSERVACIONES-", size=(30, 3))],
        [sg.Text("Estado de Consulta", size=(20, 1)), sg.Combo(['Pendiente', 'Finalizada'], key="-ESTADO-", size=(30, 1))],
        
        [sg.Button("Guardar Consulta", size=(20, 1))],
        [sg.Button("Volver", size=(20, 1))]
    ]
    
    return sg.Window("Historial Médico", layout, size=(650, 500), element_justification='c', finalize=True)

# BLOQUE PARA PRUEBAS

if __name__ == "__main__":
    window = historial_interface()
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Salir"):
            break
    window.close() 
# FIN DEL BLOQUE PARA PRUEBAS