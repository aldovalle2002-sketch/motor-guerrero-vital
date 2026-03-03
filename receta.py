def generar_receta(doctor_nombre, cedula, medicamentos):
    return {
        "doctor": doctor_nombre,
        "cedula": cedula,
        "medicamentos": medicamentos,
        "sello_digital": "GV-IA-VERIFIED-2026"
    }