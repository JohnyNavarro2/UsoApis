import requests
import time
from django.http import JsonResponse, FileResponse
from rest_framework.decorators import api_view

# 🔑 API Key de ElevenLabs (reemplázala con la tuya)
API_KEY = "sk_4cd0e0205b906668054976692bdc59a79110cb358400b121"
VOICE_ID = "21m00Tcm4TlvDq8ikWAM"

@api_view(["POST"])
def text_to_speech(request):
    """
    Convierte un texto en audio usando la API de ElevenLabs.
    """
    text = request.data.get("text", "")
    if not text:
        return JsonResponse({"error": "El texto es requerido"}, status=400)

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    
    headers = {
        "Content-Type": "application/json",
        "xi-api-key": API_KEY
    }

    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.5}
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        filename = f"tts_audio_{int(time.time())}.mp3"
        with open(filename, "wb") as f:
            f.write(response.content)

        return FileResponse(open(filename, "rb"), content_type="audio/mpeg")

    return JsonResponse({"error": "Error al procesar el audio"}, status=response.status_code)