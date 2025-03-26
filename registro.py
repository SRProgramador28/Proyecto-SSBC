import PySimpleGUI as sg

def registro_interface():
    sg.theme('My New Theme')
    layout = [
        [sg.Text("Registro Nuevo", font=("Helvetica", 20), justification='center', background_color=sg.theme_background_color())],
        [sg.Text("Código", font=("Helvetica", 12), background_color=sg.theme_background_color())],
        [sg.Input(key="-CODE-", font=("Arial", 12), size=(30, 1))],
        [sg.Text("Nombre", font=("Helvetica", 12), background_color=sg.theme_background_color())],
        [sg.Input(key="-NAME-", font=("Arial", 12), size=(30, 1))],
        [sg.Text("Apellido", font=("Helvetica", 12), background_color=sg.theme_background_color())],
        [sg.Input(key="-LASTNAME-", font=("Arial", 12), size=(30, 1))],
        [sg.Button("Enviar", font=("Helvetica", 12), size=(20, 1))],
        [sg.Button("Volver", font=("Helvetica", 12), size=(20, 1))]
    ]
    return sg.Window("Registro", layout, size=(600, 400), element_justification='c', background_color=sg.theme_background_color(), finalize=True)

# BLOQUE PARA PRUEBAS
"""
if __name__ == "__main__":
    window = registro_interface()
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Salir"):
            break
    window.close()"""
# FIN DEL BLOQUE PARA PRUEBAS
