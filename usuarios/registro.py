import PySimpleGUI as sg
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ui_config import sg

# Definición de la interfaz para crear un nuevo usuario
def crear_usuario_interface():
    sg.theme('MyNewTheme')
    layout = [
        [sg.Text("Registrar Nuevo Usuario", font=("Helvetica", 20))],

        [sg.Text("Nombre"), sg.Input(key="-NOMBRE-", size=(30, 1))],
        [sg.Text("Apellido"), sg.Input(key="-APELLIDO-", size=(30, 1))],
        [sg.Text("Usuario"), sg.Input(key="-USUARIO-", size=(30, 1))],
        [sg.Text("Contraseña"), sg.Input(key="-PASSWORD-", password_char="*", size=(30, 1))],
        
        [sg.Button("Registrar", size=(20, 1)), sg.Button("Volver", size=(20, 1))]
    ]
    return sg.Window("Nuevo Usuario", layout, size=(500, 350), finalize=True)

# BLOQUE PARA PRUEBAS
"""
if __name__ == "__main__":
    window = crear_usuario_interface()
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Salir"):
            break
    window.close()"""
# FIN DEL BLOQUE PARA PRUEBAS