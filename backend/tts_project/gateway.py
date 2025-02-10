from fastapi import FastAPI, HTTPException
import requests
from pydantic import BaseModel

# Definir el servicio del backend
BACKEND_URL = "http://127.0.0.1:8000/api/text-to-speech/"

# Crear una instancia de FastAPI
app = FastAPI()

# Modelo de datos para la petición
class TextRequest(BaseModel):
    text: str

@app.post("/api/gateway/text-to-speech/")
def text_to_speech_gateway(request_data: TextRequest):
    """
    Gateway que reenvía la solicitud de texto a voz al backend de Django.
    """
    try:
        response = requests.post(BACKEND_URL, json=request_data.dict())

        if response.status_code == 200:
            return response.content  # Devuelve el audio generado
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json())

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
