% Enfermedades
enfermedad(neumonia).
enfermedad(covid).
enfermedad(gripe).
enfermedad(bronquitis).
enfermedad(asma).
enfermedad(hipertension).
enfermedad(diabetes).
enfermedad(dermatitis).
enfermedad(gastritis).
enfermedad(colitis).
enfermedad(hepatitis).

tiene_sintomas(neumonia, [tos, fiebre, dificultad_respiratoria, dolor_pecho]).
tiene_sintomas(covid, [tos, fiebre, dificultad_respiratoria, dolor_pecho, fatiga]).
tiene_sintomas(gripe, [tos, fiebre, dolor_cabeza, fatiga]).
tiene_sintomas(bronquitis, [tos, dificultad_respiratoria, dolor_pecho]).
tiene_sintomas(asma, [dificultad_respiratoria, tos]).
tiene_sintomas(hipertension, [dolor_pecho, mareos]).
tiene_sintomas(diabetes, [fatiga, mareos]).
tiene_sintomas(dermatitis, [picazon, enrojecimiento]).
tiene_sintomas(gastritis, [dolor_abdominal, nauseas]).
tiene_sintomas(colitis, [dolor_abdominal, diarrea]).
tiene_sintomas(hepatitis, [fatiga, dolor_abdominal, nauseas, vomitos]).

tipo_enfermedad(neumonia, respiratoria).
tipo_enfermedad(covid, respiratoria).
tipo_enfermedad(covid, infecciosa).
tipo_enfermedad(gripe, respiratoria).
tipo_enfermedad(bronquitis, respiratoria).
tipo_enfermedad(asma, respiratoria).
tipo_enfermedad(hipertension, cardiovascular).
tipo_enfermedad(diabetes, endocrina).
tipo_enfermedad(dermatitis, dermatologica).
tipo_enfermedad(gastritis, digestiva).
tipo_enfermedad(colitis, digestiva).
tipo_enfermedad(hepatitis, digestiva).

gravedad_enfermedad(neumonia, grave).
gravedad_enfermedad(covid, grave).
gravedad_enfermedad(gripe, leve).
gravedad_enfermedad(bronquitis, moderada).
gravedad_enfermedad(asma, moderada).
gravedad_enfermedad(hipertension, moderada).
gravedad_enfermedad(diabetes, moderada).
gravedad_enfermedad(dermatitis, leve).
gravedad_enfermedad(gastritis, leve).
gravedad_enfermedad(colitis, leve).
gravedad_enfermedad(hepatitis, moderada).
