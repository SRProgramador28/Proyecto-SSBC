import PySimpleGUI as sg

def cita_interface():
    sg.theme('My New Theme')
    layout = [
        [sg.Text("Cita Nueva", font=("Helvetica", 20), justification='center', background_color=sg.theme_background_color())],
        [sg.Text("Código", font=("Helvetica", 12), background_color=sg.theme_background_color())],
        [sg.Input(key="-CODE-", font=("Arial", 12), size=(30, 1))],
        [sg.Text("Nombre", font=("Helvetica", 12), background_color=sg.theme_background_color())],
        [sg.Input(key="-NAME-", font=("Arial", 12), size=(30, 1))],
        [sg.Text("Apellido", font=("Helvetica", 12), background_color=sg.theme_background_color())],
        [sg.Input(key="-LASTNAME-", font=("Arial", 12), size=(30, 1))],
        [sg.Text("Fecha de Cita", font=("Helvetica", 12), background_color=sg.theme_background_color())],
        [sg.Input(key="-Date-", font=("Arial", 12), size=(30, 1))],
        [sg.Button("Enviar", font=("Helvetica", 12), size=(20, 1))],
        [sg.Button("Volver", font=("Helvetica", 12), size=(20, 1))]
    ]
    return sg.Window("Cita", layout, size=(600, 400), element_justification='c', background_color=sg.theme_background_color(), finalize=True)

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
