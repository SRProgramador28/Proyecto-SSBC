% tratamiento(Enfermedad, ListaTratamientos).

tratamiento(neumonia, [antibioticos, reposo, hidratacion, oxigeno]).
tratamiento(covid, [reposo, hidratacion, soporte_ventilatorio, antivirales]).
tratamiento(gripe, [analgesicos, antipireticos, reposo, hidratacion]).
tratamiento(bronquitis, [broncodilatadores, excesiva_hidratacion, reposo]).
tratamiento(asma, [inhaladores_broncodilatadores, corticoides_inhalados, evitar_desencadenantes]).
tratamiento(hipertension, [antihipertensivos, dieta_baja_sodio, ejercicio]).
tratamiento(diabetes, [insulina, dieta_control_glucemica, ejercicio]).
tratamiento(dermatitis, [cremas_emolientes, corticoides_topicos, antihistaminicos]).
tratamiento(gastritis, [antiacidos, inhibidores_bomba_protona, dieta_blanda]).
tratamiento(colitis, [antinflamatorios_intestinales, probioticos, dieta_equilibrada]).
tratamiento(hepatitis, [antivirales, reposo, evitar_alcohol]).

tratamiento(migrana, [analgesicos, triptanes, evitar_desencadenantes]).
tratamiento(sinusitis, [descongestionantes, lavados_nasales, antibioticos_si_bacteriana]).
tratamiento(faringitis, [analgesicos, gargaras_agua_sal, reposo]).
tratamiento(amigdalitis, [antibioticos_si_bacteriana, analgesicos, reposo]).
tratamiento(otitis, [analgesicos, antibioticos_si_infeccion, gotas_oticas]).
tratamiento(infeccion_urinaria, [antibioticos, hidratacion, analgesicos]).
tratamiento(anemia, [suplementos_hierro, dieta_rica_hierro, descanso]).

tratamiento(tuberculosis, [rifampicina, isoniacida, pirazinamida, etambutol]).
tratamiento(varicela, [antivirales, antipruriginosos, hidratacion]).
tratamiento(mono_infecciosa, [reposo, analgesicos, hidratacion]).
tratamiento(artritis, [antiinflamatorios_no_esteroideos, fisioterapia, reposo_relativo]).
tratamiento(osteoporosis, [calcio, vitamina_d, bisfosfonatos, ejercicio]).
tratamiento(conjuntivitis, [colirios_antibioticos, antihistaminicos, higiene_ocular]).
tratamiento(rinitis_alergica, [antihistaminicos, descongestionantes, evitar_alergenos]).
tratamiento(insuficiencia_renal, [dieta_renal, dialisis, trasplante_renal]).
tratamiento(litiasis_renal, [hidratacion_intensa, analgesicos, litotricia]).

tratamiento(dengue, [hidratacion, analgesicos_no_aspirina, reposo]).
tratamiento(chikungunya, [analgesicos, antiinflamatorios, reposo]).
tratamiento(zika, [analgesicos, hidratacion, reposo]).
tratamiento(infeccion_estomacal, [rehidratacion_oral, dieta_blanda, probioticos]).
tratamiento(golpe_calor, [enfriamiento_inmediato, hidratacion, reposo]).

tratamiento(sida, [tratamiento_antirretroviral, seguimiento_inmunologico]).
tratamiento(vih, [tratamiento_antirretroviral, seguimiento_inmunologico]).
tratamiento(sifilis, [penicilina, seguimiento_serologico]).
tratamiento(vph, [remocion_lesiones, vigilancia_cervical, vacuna_preventiva]).
tratamiento(gonorrea, [ceftriaxona, azitromicina]).

tratamiento(depresion, [psicoterapia, antidepresivos, ejercicio]).
tratamiento(ansiedad, [psicoterapia, ansioliticos, tecnicas_relajacion]).
tratamiento(estres, [tecnicas_relajacion, ejercicio, gestion_tiempo]).