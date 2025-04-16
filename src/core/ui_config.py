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

if "MyNewTheme" not in sg.theme_list():
    sg.theme_add_new('MyNewTheme', my_new_theme)

sg.theme('MyNewTheme')
