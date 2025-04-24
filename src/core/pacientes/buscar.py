import PySimpleGUI as sg
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ui_config import sg
from database.singleton import DatabaseManagerSingleton

# Definición de la interfaz para buscar pacientes
def buscar_paciente_interface():
    db_manager = DatabaseManagerSingleton.get_instance()  # Instancia única del Singleton
    sg.theme('MyNewTheme')
    layout = [
        [sg.Text("Buscar", font=("Helvetica", 20), justification='center')],
        [sg.Text("Nombre del Paciente:", size=(25, 1))],
        [sg.Input(key="-BUSCAR-", size=(30, 1))],
        [sg.Button("Buscar", size=(15, 1))],
        [sg.Text("Resultado:", font=("Helvetica", 12))],
        [sg.Multiline(key="-RESULTADO-", size=(60, 10), disabled=True)],
        [sg.Button("Volver", size=(15, 1))]
    ]
    window = sg.Window("Buscar Paciente", layout, size=(600, 400), element_justification='c', finalize=True)
    
    db_manager = DatabaseManagerSingleton.get_instance()
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Volver"):
            break
        elif event == "Buscar":
            criterio = values["-BUSCAR-"]
            if not criterio:
                sg.popup("Error", "Por favor, ingrese el nombre del paciente.")
                continue

            # Consulta SQL
            query = "SELECT * FROM pacientes WHERE nombre LIKE %s"
            resultados = db_manager.execute_query(query, params=(f"%{criterio}%",))

            if resultados:
                texto_resultado = "\n".join([f"ID: {r[0]}, Nombre: {r[1]}, Apellido: {r[2]}" for r in resultados])
            else:
                texto_resultado = "No se encontraron pacientes con ese nombre."
            window["-RESULTADO-"].update(texto_resultado)

    window.close()
