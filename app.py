from fastapi import FastAPI
from fastapi.responses import FileResponse
import edge_tts
import tempfile

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Amadeus Lab Kurisu TTS API is Online! 🚀"}

@app.get("/tts")
async def text_to_speech(text: str):
    voice = "ja-JP-NanamiNeural"
    communicate = edge_tts.Communicate(text, voice)
    
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tmp_path = tmp_file.name
    tmp_file.close()
    
    await communicate.save(tmp_path)
    return FileResponse(tmp_path, media_type="audio/mpeg")
