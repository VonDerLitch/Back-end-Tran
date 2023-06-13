import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'bucketkey.json'

storage_client = storage.Client()

#dir(storage_client)
#-------------------Create a New Bucket------------------------#
#bucket_name = ''
#bucket = storage_client.bucket(bucket_name)
#bucket.location = 'BR'
#bucket = storage_client.create_bucket(bucket)


#-------------printar bucket detailhes----------------------------#
#vars(bucket)


#------------Acessar um Bucket Específico---------------------#

my_bucket = storage_client.get_bucket('exemplo-teste123')


#Upar arquivos

def upload_to_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as e:
        print(e)
        return False
    

#-----------------Lugar para upar-----------------------#

#file_path = r'C:\Users\kelvin.silveira\Documents\Transcrisor-main'
#upload_to_bucket('grav', os.path.join(file_path, 'grav.wav'), 'exemplo-teste123')


#-----------------Download Files----------------------#

def download_file_from_bucket(blob_name,file_path,bucket_name):
        try:
            bucket = storage_client.get_bucket(bucket_name)
            blob = bucket.blob(blob_name)
            with open(file_path, 'wb') as f:
                 storage_client.download_blob_to_file(blob, f)
            return True
        except Exception as e:
            print(e)
            return False
    
#bucket_name = 'exemplo-teste123'
#download_file_from_bucket('grav', os.path.join(os.getcwd(), 'grav.wav'), bucket_name)

