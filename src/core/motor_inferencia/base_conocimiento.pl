% Carga de los modulos de reglas
:- [reglas/sintomas].
:- [reglas/enfermedades].
:- [reglas/diagnostico].
:- [reglas/tratamientos].

% Hechos
gravedad(leve).
gravedad(moderada).
gravedad(grave).
gravedad(critica).

tipo_enfermedad(infecciosa).
tipo_enfermedad(respiratoria).
tipo_enfermedad(cardiovascular).
tipo_enfermedad(neurologica).
tipo_enfermedad(dermatologica).
tipo_enfermedad(digestiva).
