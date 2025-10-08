import os
import shutil

import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text
from official.nlp import optimization  # to create AdamW optimizer

import matplotlib.pyplot as plt

import io

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

import zipfile

def download_file(real_file_id):
  """Downloads a file
  Args:
      real_file_id: ID of the file to download
  Returns : IO object with location.

  Load pre-authorized user credentials from the environment.
  TODO(developer) - See https://developers.google.com/identity
  for guides on implementing OAuth2 for the application.
  """
  creds, _ = google.auth.default()

  try:
    # create drive api client
    service = build("drive", "v3", credentials=creds)

    file_id = real_file_id

    # pylint: disable=maybe-no-member
    request = service.files().get_media(fileId=file_id)
    file = io.BytesIO()
    downloader = MediaIoBaseDownload(file, request)
    done = False
    while done is False:
      status, done = downloader.next_chunk()
      print(f"Download {int(status.progress() * 100)}.")

  except HttpError as error:
    print(f"An error occurred: {error}")
    file = None

  return file.getvalue()



def analyzeText(inputs):
    if(not os.path.isdir("./api/model")):
        if(download_file("17-rxZOH4kmp1Linj7TPTHPq3wE3VYntB") == None):
            return "error, model doesn't exist"
        with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
            zip_ref.extractall(directory_to_extract_to)


    reloaded_model = tf.saved_model.load("./api/model")

    #def print_my_examples(inputs, results):
    #    result_for_printing = \
    #        [f'input: {inputs[i]:<30} : score: {results[i][0]:.6f}'
    #                            for i in range(len(inputs))]
    #    print(*result_for_printing, sep='\n')
    #    print()

    examples = [
        "Around 40% of the cotton we are using is organic, and we are targeting a 2030 goal of converting all our cotton to organic cotton.",
        "We are currently leading the fashing industry with 80% of our products being sustainable.",
        "I am feeling sick",
        "I love you",
        "I go to school",
        "I go to work",
    ]

    results = tf.sigmoid(reloaded_model(tf.constant([inputs])))

    return results.numpy()[0][0]
