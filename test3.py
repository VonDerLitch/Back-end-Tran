from google.cloud import speech
import os
import io


#setting Google credential
os.environ['GOOGLE_APPLICATION_CREDENTIALS']= 'key.json'
# create client instance 
client = speech.SpeechClient()

#the path of your audio file
file_name = "Ligacao1.wav"
with io.open(file_name, "rb") as audio_file:
    content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    enable_automatic_punctuation=True,
    audio_channel_count=2,
    language_code="pt-BR",
)