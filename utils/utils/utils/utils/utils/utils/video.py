# ==========================================
# video.py
# Create Final Video
# Merge Video + AI Voice + Subtitles
# ==========================================

import os
from moviepy.editor import (
    VideoFileClip,
    AudioFileClip
)



def create_video(
        video_path,
        voice_path,
        subtitle_path
):

    """
    Replace original audio with AI voice
    and create final video.

    Input:
        video_path   -> original video
        voice_path   -> generated AI audio
        subtitle_path -> subtitle file

    Output:
        final video path
    """


    output_folder = "outputs"


    if not os.path.exists(output_folder):

        os.makedirs(output_folder)



    output_video = os.path.join(

        output_folder,

        "AI_Translated_Video.mp4"

    )



    # Load original video

    video = VideoFileClip(
        video_path
    )



    # Load generated voice

    voice = AudioFileClip(
        voice_path
    )



    # Replace audio

    final_video = video.set_audio(
        voice
    )



    # Export final video

    final_video.write_videofile(

        output_video,

        codec="libx264",

        audio_codec="aac"

    )



    video.close()

    voice.close()

    final_video.close()



    return output_video
