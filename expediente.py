import datetime

def crear_nota_medica(paciente_id, diagnostico):
    return {
        "fecha": datetime.datetime.now().isoformat(),
        "paciente_id": paciente_id,
        "diagnostico": diagnostico,
        "institucion": "Guerrero Vital"
    }