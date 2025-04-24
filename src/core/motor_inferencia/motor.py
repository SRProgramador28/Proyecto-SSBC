from pyswip import Prolog

class MotorInferencia:
    def __init__(self):
        self.prolog = Prolog()
        self.cargar_base_conocimiento()

    def cargar_base_conocimiento(self):
        self.prolog.consult("base_de_conocimientos.pl")

    def diagnostico(self, sintomas):
        diagnostico = None
        return diagnostico
