% Reglas de diagnostico
diagnostico(Enfermedad) :-
    enfermedad(Enfermedad),
    tiene_sintomas(Enfermedad, ListaSintomas),
    todos_sintomas_presentes(ListaSintomas).

% Verifica si el paciente tiene los sintomas de la enfermedad
todos_sintomas_presentes([]).
todos_sintomas_presentes([Sintoma|Resto]) :-
    sintoma(Sintoma),
    todos_sintomas_presentes(Resto).

% Diagnóstico y el tratamiento
diagnostico_con_tratamiento(Enfermedad, Tratamientos) :-
    diagnostico(Enfermedad),
    tratamiento(Enfermedad, Tratamientos).



