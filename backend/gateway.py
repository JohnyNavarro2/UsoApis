from fastapi import FastAPI, HTTPException
import requests
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
import io

# URL del backend de Django
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
            # Convertir la respuesta en un archivo de audio
            audio_stream = io.BytesIO(response.content)
            return StreamingResponse(audio_stream, media_type="audio/mpeg", headers={"Content-Disposition": "attachment; filename=output.mp3"})
        
        else:
            return HTTPException(status_code=response.status_code, detail=response.text)

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
