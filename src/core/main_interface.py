from ui_config import sg

# Definición de la interfaz principal del sistema
def main_interface():
    layout = [
        # Primera fila con el texto y el botón de Cerrar Sesión en la parte superior derecha
        [
            sg.Text("Núcleo de Diagnóstico", font=("Helvetica", 20), justification='center', expand_x=True),
            sg.Push(),
            sg.Button("Cerrar Sesión", button_color=('white', '#FF5555'), size=(12, 1))
        ],
        # Segunda fila con el TabGroup
        [
            sg.TabGroup(
                [[
                    sg.Tab("Gestión de Pacientes", [
                        [sg.Button("Registrar Paciente", expand_x=True)],
                        [sg.Button("Editar Paciente", expand_x=True)],
                        [sg.Button("Buscar Paciente", expand_x=True)],
                        [sg.Button("Listar Pacientes", expand_x=True)],
                        [sg.Button("Historial Paciente", expand_x=True)]
                    ], expand_x=True, expand_y=True),

                    sg.Tab("Gestión de Citas", [
                        [sg.Button("Nueva Cita", expand_x=True)],
                        [sg.Button("Editar Cita", expand_x=True)],
                        [sg.Button("Buscar Citas", expand_x=True)]
                    ], expand_x=True, expand_y=True),

                    sg.Tab("Gestión de Usuarios", [
                        [sg.Button("Nuevo Usuario", expand_x=True)],
                        [sg.Button("Editar Usuario", expand_x=True)],
                        [sg.Button("Nuevo Doctor", expand_x=True)],
                        [sg.Button("Editar Doctor", expand_x=True)],
                        [sg.Button("Listar Doctores", expand_x=True)]
                    ], expand_x=True, expand_y=True),

                    sg.Tab("Sistema de Diagnóstico", [
                        #[sg.Button("Consulta", expand_x=True)],
                        [sg.Button("Revisión", expand_x=True)],
                        [sg.Button("Pruebas de Laboratorio", expand_x=True)],
                        [sg.Button("Pruebas Post Mortem", expand_x=True)]
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

    return sg.Window("Interfaz Principal", layout, size=(800, 600), resizable=True, element_justification='center', finalize=True)
