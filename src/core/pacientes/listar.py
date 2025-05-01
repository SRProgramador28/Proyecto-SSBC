from ui_config import sg
from database.singleton import DatabaseManagerSingleton

# Definición de la interfaz para listar pacientes
def listar_paciente_interface():
    sg.theme('MyNewTheme')
    layout = [
        [sg.Text("Listado de Pacientes", font=("Helvetica", 20), justification='center')],
        [sg.Multiline(default_text="PACIENTES", size=(60, 15), disabled=True, key="-LISTADO-")],
        [sg.Button("Listar", size=(15, 1))],
        [sg.Button("Volver", size=(15, 1))]
    ]
    window = sg.Window("Listar Pacientes", layout, size=(800, 500), finalize=True)
    db = DatabaseManagerSingleton.get_instance()

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Volver"):
            break
        elif event == "Listar":
            # Consulta SQL
            query = "SELECT * FROM pacientes"
            resultados = db.execute_query(query)

            if resultados:
                texto_resultado = "\n".join([
                    f"\n\nID: {r[0]} \nNombre: {r[1]} \nApellido: {r[2]} \nEdad: {r[3]} \nSexo: {r[4]} \nAltura: {r[6]} \nGrupo Sanguineo: {r[7]} \nAlergias: {r[8]} \nEnfermedades Cronicas: {r[9]}"
                    for r in resultados])
            else:
                texto_resultado = "No se encontraron pacientes."
            window["-LISTADO-"].update(texto_resultado)

    window.close()
    db.close()
