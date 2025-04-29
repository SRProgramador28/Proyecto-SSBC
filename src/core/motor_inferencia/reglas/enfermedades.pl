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
enfermedad(migraña).
enfermedad(sinusitis).
enfermedad(faringitis).
enfermedad(amigdalitis).
enfermedad(otitis).
enfermedad(infeccion_urinaria).
enfermedad(anemia).
enfermedad(tuberculosis).
enfermedad(varicela).
enfermedad(mono_infecciosa).
enfermedad(artritis).
enfermedad(osteoporosis).
enfermedad(conjuntivitis).
enfermedad(rinitis_alergica).
enfermedad(insuficiencia_renal).
enfermedad(litiasis_renal).
enfermedad(dengue).
enfermedad(chikungunya).
enfermedad(zika).
enfermedad(infeccion_estomacal).
enfermedad(golpe_calor).
enfermedad(sida).
enfermedad(vih).
enfermedad(sifilis).
enfermedad(vph).
enfermedad(gonorrea).
enfermedad(depresion).
enfermedad(ansiedad).
enfermedad(estres).

% Sintomas de las enfermedades
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
tiene_sintomas(migrana, [dolor_cabeza, nauseas, fotofobia]).
tiene_sintomas(sinusitis, [dolor_cabeza, escurrimiento_nasal, congestion]).
tiene_sintomas(faringitis, [dolor_garganta, fiebre, malestar_general]).
tiene_sintomas(amigdalitis, [inflamacion_amigdalas, dolor_garganta, fiebre]).
tiene_sintomas(otitis, [dolor_oido, fiebre, irritacion_oido]).
tiene_sintomas(infeccion_urinaria, [dolor_abdominal, disuria, urgencia_miccion]).
tiene_sintomas(anemia, [fatiga, mareos, palidez]).
tiene_sintomas(tuberculosis, [tos, fiebre, sudoracion_nocturna, perdida_peso]).
tiene_sintomas(varicela, [fiebre, erupcion_cutanea, picazon, malestar_general]).
tiene_sintomas(mono_infecciosa, [fatiga, fiebre, inflamacion_ganglios, dolor_garganta]).
tiene_sintomas(artritis, [dolor_articular, inflamacion, rigidez, dificultad_movimiento]).
tiene_sintomas(osteoporosis, [fracturas, dolor_huesos, disminucion_estatura]).
tiene_sintomas(conjuntivitis, [enrojecimiento, picazon, lagrimeo, secrecion_ocular]).
tiene_sintomas(rinitis_alergica, [estornudos, picazon_nasal, congestión, escurrimiento_nasal]).
tiene_sintomas(insuficiencia_renal, [fatiga, edemas, hipertension, cambios_orina]).
tiene_sintomas(litiasis_renal, [dolor_abdominal, hematuria, nauseas, urgencia_miccion]).
tiene_sintomas(dengue, [fiebre, dolor_muscular, dolor_articular, dolor_cabeza, erupcion_cutanea]).
tiene_sintomas(chikungunya, [fiebre, dolor_articular, fatiga, dolor_cabeza]).
tiene_sintomas(zika, [fiebre, erupcion_cutanea, conjuntivitis, dolor_articular]).
tiene_sintomas(infeccion_estomacal, [nauseas, vomitos, diarrea, dolor_abdominal]).
tiene_sintomas(golpe_calor, [fiebre, sudoracion, mareos, fatiga, dolor_cabeza]).
tiene_sintomas(sida, [fatiga, fiebre, perdida_peso, sudoracion_nocturna, inflamacion_ganglios]).
tiene_sintomas(vih, [fatiga, fiebre, perdida_peso, sudoracion_nocturna, inflamacion_ganglios]).
tiene_sintomas(sifilis, [erupcion_cutanea, fiebre, inflamacion_ganglios]).
tiene_sintomas(vph, [erupcion_cutanea, picazon]).
tiene_sintomas(gonorrea, [disuria, secrecion, dolor_abdominal]).
tiene_sintomas(depresion, [fatiga, insomnio, cambios_apetito, dolor_muscular]).
tiene_sintomas(ansiedad, [palpitaciones, sudoracion, temblores, fatiga]).
tiene_sintomas(estres, [tension_muscular, dolor_cabeza, palpitaciones, sudoracion]).

% Tipo de enfermedad
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
tipo_enfermedad(migrana, neurologica).
tipo_enfermedad(sinusitis, respiratoria).
tipo_enfermedad(faringitis, respiratoria).
tipo_enfermedad(amigdalitis, respiratoria).
tipo_enfermedad(otitis, auditiva).
tipo_enfermedad(infeccion_urinaria, urinaria).
tipo_enfermedad(anemia, hematologica).
tipo_enfermedad(tuberculosis, respiratoria).
tipo_enfermedad(tuberculosis, infecciosa).
tipo_enfermedad(varicela, dermatologica).
tipo_enfermedad(varicela, infecciosa).
tipo_enfermedad(mono_infecciosa, infecciosa).
tipo_enfermedad(artritis, osteoarticular).
tipo_enfermedad(osteoporosis, osteoarticular).
tipo_enfermedad(conjuntivitis, ocular).
tipo_enfermedad(rinitis_alergica, alergica).
tipo_enfermedad(insuficiencia_renal, renal).
tipo_enfermedad(litiasis_renal, renal).
tipo_enfermedad(dengue, infecciosa).
tipo_enfermedad(dengue, tropical).
tipo_enfermedad(chikungunya, infecciosa).
tipo_enfermedad(chikungunya, tropical).
tipo_enfermedad(zika, infecciosa).
tipo_enfermedad(zika, tropical).
tipo_enfermedad(infeccion_estomacal, digestiva).
tipo_enfermedad(golpe_calor, ambiental).
tipo_enfermedad(sida, infecciosa).
tipo_enfermedad(vih, infecciosa).
tipo_enfermedad(sifilis, infecciosa).
tipo_enfermedad(vph, infecciosa).
tipo_enfermedad(gonorrea, infecciosa).
tipo_enfermedad(depresion, mental).
tipo_enfermedad(ansiedad, mental).
tipo_enfermedad(estres, mental).

% Gravedad de la enfermedad
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
gravedad_enfermedad(migrana, moderada).
gravedad_enfermedad(sinusitis, moderada).
gravedad_enfermedad(faringitis, moderada).
gravedad_enfermedad(amigdalitis, moderada).
gravedad_enfermedad(otitis, moderada).
gravedad_enfermedad(infeccion_urinaria, moderada).
gravedad_enfermedad(anemia, leve).
gravedad_enfermedad(tuberculosis, grave).
gravedad_enfermedad(varicela, moderada).
gravedad_enfermedad(mono_infecciosa, moderada).
gravedad_enfermedad(artritis, moderada).
gravedad_enfermedad(osteoporosis, moderada).
gravedad_enfermedad(conjuntivitis, leve).
gravedad_enfermedad(rinitis_alergica, leve).
gravedad_enfermedad(insuficiencia_renal, grave).
gravedad_enfermedad(litiasis_renal, moderada).
gravedad_enfermedad(dengue, moderada).
gravedad_enfermedad(chikungunya, moderada).
gravedad_enfermedad(zika, leve).
gravedad_enfermedad(infeccion_estomacal, leve).
gravedad_enfermedad(golpe_calor, grave).
gravedad_enfermedad(sida, grave).
gravedad_enfermedad(vih, grave).
gravedad_enfermedad(sifilis, moderada).
gravedad_enfermedad(vph, moderada).
gravedad_enfermedad(gonorrea, moderada).
gravedad_enfermedad(depresion, leve).
gravedad_enfermedad(ansiedad, leve).
gravedad_enfermedad(estres, leve).
