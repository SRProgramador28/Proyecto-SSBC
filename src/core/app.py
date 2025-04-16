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

# Módulo de usuarios
from usuarios.registro import crear_usuario_interface
from usuarios.editar import editar_usuario_interface

# Módulos de sistema de diagnóstico
from sistema.consulta import consulta_interface
from sistema.pruebas_laboratorio import pruebas_laboratorio_interface
from sistema.pruebas_postmortem import pruebas_postmortem_interface

def main():
    current_state = "login"
    window = login_interface()

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Salir"):
            break
        
        # -----> Login <-----
        if current_state == "login":
            if event == "Iniciar Sesión":
                usercode = values["-USERCODE-"]
                password = values["-PASSWORD-"]
                if usercode == "1" and password == "1":
                    window.close()
                    current_state = "main"
                    window = main_interface()

        # ------> Main <-----
        elif current_state == "main":
            if event == "Nuevo Paciente":
                window.close()
                current_state = "registro"
                window = registro_interface()

        # -----> Pacientes <-----
            elif event == "Editar Paciente":
                window.close()
                current_state = "editar_paciente"
                window = editar_paciente_interface()

            elif event == "Buscar Paciente":
                window.close()
                current_state = "buscar"
                window = buscar_paciente_interface()

            elif event == "Listar Pacientes":
                window.close()
                current_state = "listar"
                window = listar_paciente_interface()

        # ------> Citas <------
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

        # ------> Usuarios <------
            elif event == "Nuevo Usuario":
                window.close()
                current_state = "crear_usuario"
                window = crear_usuario_interface()

            elif event == "Editar Usuario":
                window.close()
                current_state = "editar_usuario"
                window = editar_usuario_interface()

        # ------> Sistema de Diagnóstico <------
            elif event == "Consulta":
                window.close()
                current_state = "consulta"
                window = consulta_interface()

            elif event == "Revisión":
                window.close()
                current_state = "main"
                window = main_interface()

            elif event == "Pruebas de Laboratorio":
                window.close()
                current_state = "pruebas_laboratorio"
                window = pruebas_laboratorio_interface()

            elif event == "Pruebas Post Mortem":
                window.close()
                current_state = "pruebas_postmortem"
                window = pruebas_postmortem_interface()

            # -----> Cerrar Sesión <-----
            elif event == "Cerrar Sesión":
                window.close()
                current_state = "login"
                window = login_interface()

        # Manejo de eventos en las ventanas secundarias
        elif current_state == "registro":
            if event == "Enviar":
                nombre = values["-NAME-"]
                apellido = values["-LASTNAME-"]
                sg.popup("Registro Creado", f"Nombre: {nombre}", f"Apellido: {apellido}")
            elif event == "Volver":
                window.close()
                current_state = "main"
                window = main_interface()

        elif current_state == "editar_paciente":
            if event == "editar_paciente":
                # Lógica para Editar
                pass
            elif event == "Volver":
                window.close()
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
            if event == "editar_cita":
                # Lógica para Editar
                pass
            elif event == "Volver":
                window.close()
                current_state = "main"
                window = main_interface()

        elif current_state == "buscar_citas":
            if event == "Volver":
                window.close()
                current_state = "main"
                window = main_interface()

        elif current_state == "crear_usuario":
            if event == "Crear Usuario":
                username = values["-USERNAME-"]
                confirm = values["-CONFIRM-"]
                sg.popup("Usuario Creado", f"Usuario: {username}")
            elif event == "Volver":
                window.close()
                current_state = "main"
                window = main_interface()


        elif current_state == "editar_usuario":
            if event == "Editar Usuario":
                # Lógica para Editar
                pass
            elif event == "Volver":
                window.close()
                current_state = "main"
                window = main_interface()

        elif current_state == "consulta":
            if event == "Guardar Consulta":
                id_paciente = values["-ID_PACIENTE-"]
                id_doctor = values["-ID_DOCTOR-"]
                diagnostico = values["-DIAGNOSTICO-"]
                tratamiento = values["-TRATAMIENTO-"]
                observaciones = values["-OBSERVACIONES-"]
                estado = values["-ESTADO-"]
                sg.popup("Consulta Guardada", f"ID Paciente: {id_paciente}", f"ID Doctor: {id_doctor}")
            elif event == "Volver":
                window.close()
                current_state = "main"
                window = main_interface()

        elif current_state == "pruebas_laboratorio":
            if event == "Guardar Prueba":
                id_consulta = values["-ID_CONSULTA-"]
                nombre_prueba = values["-NOMBRE_PRUEBA-"]
                fecha = values["-FECHA-"]
                sg.popup("Prueba Guardada", f"ID Consulta: {id_consulta}", f"Nombre de la Prueba: {nombre_prueba}")
            elif event == "Volver":
                window.close()
                current_state = "main"
                window = main_interface()

        elif current_state == "pruebas_postmortem":
            if event == "Guardar Prueba":
                id_consulta = values["-ID_CONSULTA-"]
                fecha = values["-FECHA-"]
                detalles = values["-DETALLES-"]
                sg.popup("Prueba Guardada", f"ID Consulta: {id_consulta}", f"Fecha: {fecha}")
            elif event == "Volver":
                window.close()
                current_state = "main"
                window = main_interface()

    window.close()

if __name__ == "__main__":
    main()

