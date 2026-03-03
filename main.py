from fastapi import FastAPI
import os

app = FastAPI(title="Motor Guerrero Vital")

@app.get("/")
def inicio():
    return {"status": "Motor Activo", "proyecto": "Guerrero Vital", "region": "Acapulco"}

@app.post("/triaje")
def procesar_paciente(datos: dict):
    # Aquí el motor usa la IA para analizar síntomas
    return {"mensaje": "Analizando síntomas...", "urgencia": "Verde"}

@app.get("/llamar-doctor")
def conectar_video():
    # Enlace para activar la teleconsulta integrada
    return {"url_video": "https://video.guerrerovital.com/sala-privada"}