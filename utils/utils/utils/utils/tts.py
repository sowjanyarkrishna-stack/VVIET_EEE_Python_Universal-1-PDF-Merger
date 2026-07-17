# ==========================================
# tts.py
# AI Voice Generation using gTTS
# ==========================================

from gtts import gTTS
import os


def generate_voice(text, language):

    """
    Convert translated text into AI voice

    Input:
        text -> translated sentence
        language -> language code

    Output:
        generated audio file path
    """


    output_folder = "temp"


    if not os.path.exists(output_folder):

        os.makedirs(output_folder)



    audio_path = os.path.join(

        output_folder,

        "ai_voice.mp3"

    )



    tts = gTTS(

        text=text,

        lang=language

    )


    tts.save(

        audio_path

    )


    return audio_path
