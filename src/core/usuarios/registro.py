from ui_config import sg
from database.singleton import DatabaseManagerSingleton

# Definición de la interfaz para crear un nuevo usuario
def crear_usuario_interface():
    sg.theme('MyNewTheme')
    layout = [
        [sg.Text("Registrar Nuevo Usuario", font=("Helvetica", 20))],
        [sg.Frame("Datos del Usuario", [
            [sg.Text("Nombre"), sg.Input(key="-NOMBRE-", size=(30, 1))],
            [sg.Text("Usuario"), sg.Input(key="-USUARIO-", size=(30, 1))],
            [sg.Text("Contraseña"), sg.Input(key="-PASSWORD-", password_char="*", size=(30, 1))],
            [sg.Text("Rol", size=(20, 1)), sg.Combo(["Usuario"], key="-ROL-")],
        ])],
        [sg.Button("Registrar", size=(20, 1)), sg.Button("Volver", size=(20, 1))]
    ]
    window = sg.Window("Nuevo Usuario", layout, size=(600, 500), element_justification='c', finalize=True)
    db = DatabaseManagerSingleton.get_instance()

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Volver"):
            break
        if event == "Registrar":
            try:
                query = """
                  INSERT INTO usuarios (nombre, usuario, password, rol, estado)
                  VALUES (%s, %s, %s, %s, 'Activo')
                """
                filas = db.execute_query(query, 
                                         (values["-NOMBRE-"],
                                          values["-USUARIO-"],
                                          values["-PASSWORD-"],
                                          values["-ROL-"]))
                if filas:
                    sg.popup("Usuario registrado exitosamente")
            except Exception as e:
                sg.popup(f"Error al registrar usuario: {e}")
    window.close()
    db.close()
