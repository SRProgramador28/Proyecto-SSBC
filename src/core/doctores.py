from ui_config import sg

def doctores_interface():
    layout = [
        [sg.Text("Gestión de Doctores", font=("Helvetica", 20), justification='center')],
        
        [sg.Text("Nombre del Doctor", size=(20, 1)), sg.Input(key="-NOMBRE-", size=(30, 1))],
        [sg.Text("Especialidad", size=(20, 1)), sg.Input(key="-ESPECIALIDAD-", size=(30, 1))],
        [sg.Text("ID de Usuario Vinculado", size=(20, 1)), sg.Input(key="-IDUSUARIO-", size=(30, 1))],
        
        [sg.Button("Registrar Doctor", size=(20, 1))],
        [sg.Button("Volver", size=(20, 1))]
    ]
    
    return sg.Window("Gestión de Doctores", layout, size=(600, 400), element_justification='c', finalize=True)

# BLOQUE PARA PRUEBAS
"""
if __name__ == "__main__":
    window = doctores_interface()
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Salir"):
            break
    window.close()"""
# FIN DEL BLOQUE PARA PRUEBAS