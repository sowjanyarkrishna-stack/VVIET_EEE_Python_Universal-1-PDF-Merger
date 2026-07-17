import whisper
import tempfile
import os

# Load Whisper model
model = whisper.load_model("base")

def speech_to_text(audio_file):
    """
    Converts speech in an audio file to text.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp:
        temp.write(audio_file.read())
        temp_path = temp.name

    result = model.transcribe(temp_path)

    os.remove(temp_path)

    return result["text"]
