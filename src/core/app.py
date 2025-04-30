import PySimpleGUI as sg
from login import login_interface
from main_interface import main_interface
from database.singleton import DatabaseManagerSingleton

# Módulos de pacientes
from pacientes.registro import registro_interface
from pacientes.editar import editar_paciente_interface
from pacientes.buscar import buscar_paciente_interface
from pacientes.listar import listar_paciente_interface

# Módulos de citas
from citas.cita import cita_interface
from citas.editar import editar_cita_interface
from citas.buscar import buscar_cita_interface

# Módulo de usuarios
from usuarios.registro import crear_usuario_interface
from usuarios.editar import editar_usuario_interface
from usuarios.doctores import doctores_interface
from usuarios.editar_doctores import editar_doctor_interface

# Módulos de sistema de diagnóstico
from sistema.consulta import consulta_interface
from sistema.pruebas_laboratorio import pruebas_laboratorio_interface
from sistema.pruebas_postmortem import pruebas_postmortem_interface

def handle_login(window):
    # Maneja la lógica de la ventana de login
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Salir"):
        return None, None
    if event == "Iniciar Sesión":
        usercode = values["-USERCODE-"]
        password = values["-PASSWORD-"]
        if usercode == "1" and password == "1":
            return "main", main_interface()
        
        if not all([usercode, password]):
            sg.popup("Error", "Por favor, complete los campos obligatorios.")
        try:
            # Consulta a la base de datos para verificar el usuario y la contraseña
            query = """
            SELECT * FROM usuarios WHERE usuario = %s AND password = %s
            """
            db = DatabaseManagerSingleton.get_instance()
            filas = db.execute_query(query, (usercode, password))
            # Aquí iría la lógica de autenticación real
            if usercode == "admin" and password == "admin":
                sg.popup("Bienvenido Admistrador")
                return "main", main_interface()
            elif filas:
                sg.popup(f"Bienvenido Doctor {usercode}!")
                return "main", main_interface()
            else:
                sg.popup("Error", "Usuario o contraseña incorrectos.")
        except Exception as e:
            sg.popup(f"Error al iniciar sesión: {e}", title="Error")
    return "login", window


def handle_main(window):
    # Maneja la lógica de la ventana principal
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Cerrar Sesión"):
        return "login", login_interface()  # Cierra sesión y regresa al login

    # Diccionario de transiciones desde la ventana principal
    transitions = {
        "Registrar Paciente": ("registro", registro_interface),
        "Editar Paciente": ("editar_paciente", editar_paciente_interface),
        "Buscar Paciente": ("buscar", buscar_paciente_interface),
        "Listar Pacientes": ("listar", listar_paciente_interface),
        "Nueva Cita": ("cita", cita_interface),
        "Editar Cita": ("editar_cita", editar_cita_interface),
        "Buscar Citas": ("buscar_citas", buscar_cita_interface),
        "Nuevo Usuario": ("crear_usuario", crear_usuario_interface),
        "Editar Usuario": ("editar_usuario", editar_usuario_interface),
        "Nuevo Doctor": ("registrar_doctor", doctores_interface),
        "Editar Doctor": ("editar_doctor", editar_doctor_interface),
        "Consulta": ("consulta", consulta_interface),
        "Pruebas de Laboratorio": ("pruebas_laboratorio", pruebas_laboratorio_interface),
        "Pruebas Post Mortem": ("pruebas_postmortem", pruebas_postmortem_interface),
    }

    if event in transitions:
        next_state, next_window_func = transitions[event]
        return next_state, next_window_func()  

    return "main", window  

# Manejador de ventanas genéricas con el botón 'Volver'
def handle_generic(window, return_state="main"):
    if window is None: 
        return return_state, main_interface()

    event, _ = window.read()
    if event in (sg.WIN_CLOSED, "Volver"):
        window.close()
        return return_state, main_interface()
    return return_state, window

def main():
    # Diccionario de estados y sus manejadores
    state_handlers = {
        "login": handle_login,
        "main": handle_main,
        "registro": lambda w: handle_generic(w, "main"),
        "editar_paciente": lambda w: handle_generic(w, "main"),
        "buscar": lambda w: handle_generic(w, "main"),
        "listar": lambda w: handle_generic(w, "main"),
        "cita": lambda w: handle_generic(w, "main"),
        "editar_cita": lambda w: handle_generic(w, "main"),
        "buscar_citas": lambda w: handle_generic(w, "main"),
        "crear_usuario": lambda w: handle_generic(w, "main"),
        "editar_usuario": lambda w: handle_generic(w, "main"),
        "registrar_doctor": lambda w: handle_generic(w, "main"),
        "editar_doctor": lambda w: handle_generic(w, "main"),
        "consulta": lambda w: handle_generic(w, "main"),
        "pruebas_laboratorio": lambda w: handle_generic(w, "main"),
        "pruebas_postmortem": lambda w: handle_generic(w, "main"),
    }

    # Estado inicial
    current_state = "login"
    window = login_interface()

    # Bucle principal
    while current_state:
        handler = state_handlers.get(current_state)
        if handler:
            next_state, next_window = handler(window)
            if window:  # Verificar si la ventana actual no es None antes de cerrarla
                window.close()
            window = next_window
            current_state = next_state
        else:
            print(f"Estado desconocido: {current_state}")
            break

    if window:  # Verificar si la ventana final no es None antes de cerrarla
        window.close()


if __name__ == "__main__":
    main()
