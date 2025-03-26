import PySimpleGUI as sg

def login_interface():
    sg.theme('My New Theme')
    layout = [
        [sg.Text("Iniciar Sesión", font=("Helvetica", 24), justification='center', background_color=sg.theme_background_color())],
        [sg.Text("Usuario", font=("Helvetica", 16), background_color=sg.theme_background_color())],
        [sg.Input(key="-USERCODE-", font=("Arial", 12), size=(30, 1), justification='left')],
        [sg.Text("Contraseña", font=("Helvetica", 16), background_color=sg.theme_background_color())],
        [sg.Input(key="-PASSWORD-", password_char="*", font=("Arial", 12), size=(30, 1), justification='left')],
        [sg.Button("Iniciar Sesión", font=("Helvetica", 12), size=(20, 1))],
        [sg.Button("Salir", font=("Helvetica", 12), size=(20, 1))]
    ]
    return sg.Window("Login", layout, size=(400, 300), element_justification='c', background_color=sg.theme_background_color())

# BLOQUE PARA PRUEBAS

if __name__ == "__main__":
    window = login_interface()
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Salir"):
            break
    window.close() 
# FIN DEL BLOQUE PARA PRUEBAS