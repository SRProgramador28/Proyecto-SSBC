import PySimpleGUI as sg
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ui_config import sg

# Definición de la interfaz para editar un usuario
def editar_usuario_interface():
    sg.theme('MyNewTheme')
    
    layout = [
        [sg.Text("Editar Usuario", font=("Helvetica", 20))],

        [sg.Text("Buscar por Usuario"), sg.Input(key="-USUARIO-", size=(30, 1)), sg.Button("Buscar")],
        [sg.HorizontalSeparator()],
        [sg.Text("Nombre"), sg.Input(key="-NOMBRE-", size=(30, 1), disabled=True)],
        [sg.Text("Apellido"), sg.Input(key="-APELLIDO-", size=(30, 1), disabled=True)],
        [sg.Text("Contraseña"), sg.Input(key="-PASSWORD-", password_char="*", size=(30, 1), disabled=True)],
        [sg.Text("Rol"), sg.Combo(["Administrador", "Usuario"], key="-ROL-", disabled=True)],
        [sg.Text("Estado"), sg.Combo(["Activo", "Inactivo"], key="-ESTADO-", disabled=True)],
        [sg.Text("Fecha de Registro"), sg.Input(key="-FECHA_REGISTRO-", size=(30, 1), disabled=True)],
        
        [sg.Button("Guardar Cambios", size=(20, 1)), sg.Button("Volver", size=(20, 1))]
    ]
    return sg.Window("Editar Usuario", layout, size=(500, 400), finalize=True)

# BLOQUE PARA PRUEBAS
"""
if __name__ == "__main__":
    window = editar_usuario_interface()
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Salir"):
            break
    window.close()"""
# FIN DEL BLOQUE PARA PRUEBAS