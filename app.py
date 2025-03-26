import PySimpleGUI as sg
from login import login_interface
from main_interface import main_interface
from registro import registro_interface
from cita import cita_interface

def main():
    current_state = "login" # Estado inicial: 'login'
    window = login_interface()  # Se abre la ventana de login

    while True:
        event, values = window.read()
        
        # Si se cierra la ventana o se selecciona 'Salir', se termina la aplicación
        if event in (sg.WIN_CLOSED, "Salir"):
            break

        if current_state == "login":
            if event == "Iniciar Sesión":
                usercode = values["-USERCODE-"]
                password = values["-PASSWORD-"]
                # Validación simple
                if usercode == "admin" and password == "1234":
                    window.close()
                    current_state = "main"
                    window = main_interface()
                    
        elif current_state == "main":
            if event == "Registro Nuevo":
                window.close()
                current_state = "registro"
                window = registro_interface()
            elif event == "Registrar Cita":
                window.close()
                current_state = "cita"
                window = cita_interface()
            elif event == "Cerrar Sesión":
                window.close()
                current_state = "login"
                window = login_interface()

        elif current_state == "registro":
            if event == "Enviar":
                nombre = values["-NAME-"]
                apellido = values["-LASTNAME-"]
                sg.popup("Registro Creado", f"Nombre: {nombre}", f"Apellido: {apellido}")
            elif event == "Volver":
                window.close()
                current_state = "main"
                window = main_interface()
        
        elif current_state == "cita":
            if event == "Enviar":
                nombre = values["-NAME-"]
                apellido = values["-LASTNAME-"]
                sg.popup("Cita Registrada", f"Nombre: {nombre}", f"Apellido: {apellido}")
            elif event == "Volver":
                window.close()
                current_state = "main"
                window = main_interface()

    window.close()

if __name__ == "__main__":
    main()
