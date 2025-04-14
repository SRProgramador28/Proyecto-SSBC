import PySimpleGUI as sg
from login import login_interface
from main_interface import main_interface

# Módulos de pacientes
from pacientes.registro import registro_interface
from pacientes.editar import editar_paciente_interface
from pacientes.buscar import buscar_paciente_interface
from pacientes.listar import listar_paciente_interface

# Módulos de citas
from citas.cita import cita_interface
from citas.editar import editar_cita_interface
from citas.buscar import buscar_cita_interface

def main():
    current_state = "login"
    window = login_interface()

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Salir"):
            break

        if current_state == "login":
            if event == "Iniciar Sesión":
                usercode = values["-USERCODE-"]
                password = values["-PASSWORD-"]
                if usercode == "1" and password == "1":
                    window.close()
                    current_state = "main"
                    window = main_interface()

        elif current_state == "main":
            if event == "Nuevo Paciente":
                window.close()
                current_state = "registro"
                window = registro_interface()

            elif event == "Editar Paciente":
                window.close()
                current_state = "editar"
                window = editar_paciente_interface()

            elif event == "Buscar Paciente":
                window.close()
                current_state = "buscar"
                window = buscar_paciente_interface()

            elif event == "Listar Pacientes":
                window.close()
                current_state = "listar"
                window = listar_paciente_interface()

            elif event == "Nueva Cita":
                window.close()
                current_state = "cita"
                window = cita_interface()

            elif event == "Editar Cita":
                window.close()
                current_state = "editar_cita"
                window = editar_cita_interface()

            elif event == "Buscar Citas":
                window.close()
                current_state = "buscar_citas"
                window = buscar_cita_interface()

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

        elif current_state == "editar":
            result = editar_paciente_interface()
            if result == "volver":
                current_state = "main"
                window = main_interface()
        
        elif current_state == "buscar":
            if event == "Buscar":
                # Lógica de búsqueda
                pass
            elif event == "Volver":
                window.close()
                current_state = "main"
                window = main_interface()

        elif current_state == "listar":
            if event == "Volver":
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

        elif current_state == "editar_cita":
            result = editar_cita_interface()
            if result == "volver":
                current_state = "main"
                window = main_interface()

        elif current_state == "buscar_citas":
            if event == "Volver":
                window.close()
                current_state = "main"
                window = main_interface()

    window.close()

if __name__ == "__main__":
    main()

