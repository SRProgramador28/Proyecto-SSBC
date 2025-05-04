from ui_config import sg
from database.singleton import DatabaseManagerSingleton

# Definición de la interfaz para listar doctores
def listar_doctor_interface():
    sg.theme('MyNewTheme')
    layout = [
        [sg.Text("Listado de Doctores", font=("Helvetica", 20), justification='center')],

        [sg.Frame("Resultados", [
            [sg.Multiline(key="-DOCTORES-", size=(80, 18), disabled=True)]
        ])],

        [sg.Button("Listar", size=(15, 1)), sg.Button("Volver", size=(15, 1))]
    ]
    window = sg.Window("Listar Doctores", layout, size=(600, 500), element_justification='c', finalize=True)
    db = DatabaseManagerSingleton.get_instance()

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Volver"):
            break
        elif event == "Listar":
            # Consulta SQL
            query = "SELECT * FROM doctores"
            resultados = db.execute_query(query)

            if resultados:
                texto_resultado = "\n".join([
                    f"\nID: {r[0]} \nNombre: {r[1]} \nEspecialidad: {r[2]}"
                    for r in resultados])
            else:
                texto_resultado = "No se encontraron doctores."
            window["-DOCTORES-"].update(texto_resultado)

    window.close()
    db.close()
