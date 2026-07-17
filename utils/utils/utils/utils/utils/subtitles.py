# ==========================================
# subtitles.py
# Create SRT Subtitle File
# ==========================================

import os
import pysrt


def create_subtitle(text):

    """
    Create subtitle (.srt) file

    Input:
        text -> translated text

    Output:
        subtitle file path
    """

    output_folder = "temp"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


    subtitle_path = os.path.join(
        output_folder,
        "subtitle.srt"
    )


    subs = pysrt.SubRipFile()


    # Split text into subtitle lines

    sentences = text.split(".")


    start_seconds = 0


    for index, sentence in enumerate(sentences):

        sentence = sentence.strip()


        if sentence:

            item = pysrt.SubRipItem(

                index=index + 1,

                start=pysrt.SubRipTime(
                    seconds=start_seconds
                ),

                end=pysrt.SubRipTime(
                    seconds=start_seconds + 5
                ),

                text=sentence

            )


            subs.append(item)


            start_seconds += 5



    subs.save(
        subtitle_path,
        encoding="utf-8"
    )


    return subtitle_path
