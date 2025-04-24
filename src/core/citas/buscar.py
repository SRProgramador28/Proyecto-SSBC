from ui_config import sg
from database.singleton import DatabaseManagerSingleton

# Definición de la interfaz para buscar citas
def buscar_cita_interface():
    layout = [
        [sg.Text("Buscar Cita", font=("Helvetica", 20))],
        [sg.Text("Código del paciente", font=("Helvetica", 12))],
        [sg.Input(key="-CODE-", font=("Arial", 12), size=(30, 1))],
        [sg.Button("Buscar", font=("Helvetica", 12)), sg.Button("Volver", font=("Helvetica", 12))],
        [sg.Text("Resultado:", font=("Helvetica", 12))],
        [sg.Multiline(key="-RESULTADO-", size=(60, 10), font=("Arial", 11), disabled=True)]
    ]
    return sg.Window("Buscar Cita", layout, size=(600, 400), element_justification='c', finalize=True)

