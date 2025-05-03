from ui_config import sg
from motor_inferencia.motor import MotorInferencia

# Definición de la interfaz para la revisión con el motor de inferencia
def revision_interface():
    sg.theme('MyNewTheme')

    layout = [

        [sg.Text("Sistema de Diagnóstico Automático", font=("Helvetica", 20), justification='center', expand_x=True)],

        [sg.Frame("Ingresar Síntomas", [
            [sg.Text("Síntomas (separados por comas):", size=(25, 1)), sg.Input(key="-SINTOMAS-", size=(50, 1))],
            [sg.Button("Diagnosticar", size=(15, 1))]
        ])],

        [sg.HorizontalSeparator()],

        [sg.Frame("Resultados del Diagnóstico", [
            [sg.Text("Diagnóstico:", size=(15, 1)), sg.Multiline(key="-DIAGNOSTICO-", size=(60, 5), disabled=True)],
            [sg.Text("Gravedad:", size=(15, 1)), sg.Multiline(key="-GRAVEDAD-", size=(60, 1))],
            [sg.Text("Tipo de Enfermedad:", size=(20, 1)), sg.Multiline(key="-TIPO-", size=(60, 1))],
            [sg.Text("Tratamientos Sugeridos:", size=(20, 1)), sg.Multiline(key="-TRATAMIENTOS-", size=(60, 5), disabled=True)]
        ])],

        [sg.Button("Volver", size=(15, 1))]
    ]
    window = sg.Window("Revisión", layout, size=(600, 600), element_justification='center', finalize=True)
    motor = MotorInferencia()

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Volver"):
            break

        elif event == "Diagnosticar":
            sintomas = values["-SINTOMAS-"].strip()
            if not sintomas:
                sg.popup("Error", "Por favor, ingrese al menos un síntoma.")
                continue

            try:
                lista_sintomas = [sintoma.strip() for sintoma in sintomas.split(",")]

                resultados = motor.diagnostico(lista_sintomas)

                if resultados:
                    resultado = resultados[0]
                    diagnostico = resultado.get("Enfermedad", "No se pudo determinar un diagnóstico.")
                    gravedad = resultado.get("Gravedad", "Desconocida")
                    tipo = resultado.get("Tipo", "Desconocido")
                    tratamientos = resultado.get("Tratamientos", "No hay tratamientos sugeridos.")

                    window["-DIAGNOSTICO-"].update(diagnostico)
                    window["-GRAVEDAD-"].update(gravedad)
                    window["-TIPO-"].update(tipo)
                    window["-TRATAMIENTOS-"].update(", ".join(tratamientos) if isinstance(tratamientos, list) else tratamientos)
                else:
                    window["-DIAGNOSTICO-"].update("No se pudo determinar un diagnóstico.")
                    window["-GRAVEDAD-"].update("")
                    window["-TIPO-"].update("")
                    window["-TRATAMIENTOS-"].update("No hay tratamientos sugeridos.")
            except Exception as e:
                sg.popup_error(f"Error al procesar el diagnóstico: {e}")

    window.close()
