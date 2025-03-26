import PySimpleGUI as sg

my_new_theme = {
    'BACKGROUND': '#EFF6FF',   # Base-100: un fondo claro con un sutil tinte azulado
    'TEXT': '#1F2937',         # Base-content: texto en un tono oscuro para buen contraste
    'INPUT': '#E2E8F0',        # Base-200: fondo de los campos de entrada, un gris azulado muy suave
    'TEXT_INPUT': '#1F2937',   # Texto en los inputs, usando el color base-content oscuro
    'SCROLL': '#E2E8F0',       # Mantiene la coherencia con el fondo de INPUT
    'BUTTON': ('white', '#1FB6FF'),  # Botón primario: fondo azul vibrante y texto blanco
    'PROGRESS': ('#1FB6FF', '#CBD5E1'),  # Barra de progreso en tonos que combinan con el botón y el fondo
    'BORDER': 1,
    'SLIDER_DEPTH': 0,
    'PROGRESS_DEPTH': 0
}

sg.theme_add_new('MyNewTheme', my_new_theme)

def main_interface():
    sg.theme('My New Theme')
    layout = [
        [sg.Text("Sistema Principal SP", font=("Helvetica", 20), justification='center', background_color=sg.theme_background_color())],
        [[sg.Image(sg.EMOJI_BASE64_READING)]],
        [sg.Button("Registro Nuevo", font=("Helvetica", 12), size=(20, 1))],
        [sg.Button("Registrar Cita", font=("Helvetica", 12), size=(20, 1))],
        [sg.Button("Cerrar Sesión", font=("Helvetica", 12), size=(20, 1))]
    ]
    return sg.Window("Interfaz Principal", layout, size=(600, 400), element_justification='c', background_color=sg.theme_background_color(), finalize=True)

# BLOQUE PARA PRUEBAS

if __name__ == "__main__":
    window = main_interface()
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Salir"):
            break
    window.close()
# FIN DEL BLOQUE PARA PRUEBAS