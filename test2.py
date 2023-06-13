import os
from google.cloud import storage
from tkinter import filedialog

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'bucketkey.json'

storage_client = storage.Client()

user_file = filedialog.askopenfilename()

def upload_to_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
    except Exception as e:
        print(e)
        return False
    

#-----------------Lugar para upar-----------------------#

file_path = r'C:\Users\kelvin.silveira\Documents\Transcrisor-main'
upload_to_bucket("documents/{}".format(user_file), os.path.join(file_path, user_file), 'exemplo-teste123')

#file_path = r'C:\Users\kelvin.silveira\Documents\Transcrisor-main'
#upload_to_bucket('teste.wav', os.path.join(file_path, user_file), 'exemplo-teste123')