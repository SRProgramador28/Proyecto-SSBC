from ui_config import sg
from database.singleton import DatabaseManagerSingleton

# Definición de la interfaz para la revisión
def revision_interface():
    layout = [
        # Primera fila con el texto y el botón de Cerrar Sesión en la parte superior derecha
        [
            sg.Text("Sistema de Revisión", font=("Helvetica", 20), justification='center', expand_x=True),
            sg.Push(),
            sg.Button("Cerrar Sesión", button_color=('white', '#FF5555'), size=(12, 1))
        ],
        # Segunda fila con el TabGroup
        [
            sg.TabGroup(
                [[
                    sg.Tab("Revisión de Pacientes", [
                        [sg.Button("Registrar Revisión", expand_x=True)],
                        [sg.Button("Editar Revisión", expand_x=True)],
                        [sg.Button("Buscar Revisión", expand_x=True)],
                        [sg.Button("Listar Revisiones", expand_x=True)]
                    ], expand_x=True, expand_y=True)
                ]],
                expand_x=True,
                expand_y=True,
                tab_location='top',
                title_color='black',
                selected_title_color='black',
                border_width=2
            )
        ]
    ]

    return sg.Window("Interfaz de Revisión", layout, size=(800, 600), resizable=True, element_justification='center', finalize=True)