# ==========================================
# helpers.py
# Utility Functions
# ==========================================

import os
import uuid



def save_uploaded_file(uploaded_file):

    """
    Save uploaded Streamlit file
    into uploads folder

    Input:
        uploaded_file -> Streamlit uploaded file

    Output:
        saved file path
    """

    folder = "uploads"


    if not os.path.exists(folder):

        os.makedirs(folder)



    file_extension = uploaded_file.name.split(".")[-1]


    file_name = (
        str(uuid.uuid4())
        + "."
        + file_extension
    )


    file_path = os.path.join(

        folder,

        file_name

    )



    with open(

        file_path,

        "wb"

    ) as f:

        f.write(

            uploaded_file.getbuffer()

        )



    return file_path



def create_folder(folder_name):

    """
    Create folder if not exists
    """

    if not os.path.exists(folder_name):

        os.makedirs(folder_name)



def clean_folder(folder_name):

    """
    Remove temporary files
    """

    if os.path.exists(folder_name):

        for file in os.listdir(folder_name):

            path = os.path.join(
                folder_name,
                file
            )

            if os.path.isfile(path):

                os.remove(path)
