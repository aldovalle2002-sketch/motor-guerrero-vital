def analizar_prioridad(sintomas):
    palabras_clave_emergencia = ["pecho", "respirar", "inconsciente", "sangrado"]
    if any(palabra in sintomas.lower() for palabra in palabras_clave_emergencia):
        return "ROJO - Emergencia Inmediata"
    return "VERDE - Consulta General"