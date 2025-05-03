from pyswip import Prolog
from pathlib import Path

class MotorInferencia:
    def __init__(self):
        self.prolog = Prolog()
        self.cargar_base_conocimiento()

    def cargar_base_conocimiento(self):
        base_dir = Path(__file__).parent.resolve()
        filename = "base_conocimiento.pl"
        full_path = base_dir / filename

        if not full_path.exists():
            raise FileNotFoundError(f"No se encontró el fichero Prolog en: {full_path}")

        dir_posix = base_dir.as_posix()
        cmd = f"working_directory(_,'{dir_posix}')"
        print(f"[DEBUG] Ejecutando en Prolog: {cmd}")
        next(self.prolog.query(cmd))

        print(f"[DEBUG] Consultando Prolog: {filename}")
        self.prolog.consult(filename)

    def diagnostico(self, sintomas):
        self.prolog.retractall("sintoma(_)")
        for sint in sintomas:
            self.prolog.assertz(f"sintoma({sint})")
        return list(self.prolog.query("diagnostico_completo(Enfermedad, Tratamientos, Gravedad, Tipo)"))
