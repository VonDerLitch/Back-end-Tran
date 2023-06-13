from google.cloud import speech
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'

client = speech.SpeechClient()

gcs_uri = "gs://exemplo-teste123/audio-files/testerapido.flac"

audio = speech.RecognitionAudio(uri=gcs_uri)

config = speech.RecognitionConfig(
    encoding = 'FLAC',
    language_code="pt-BR",
    sample_rate_hertz = 8000,
    audio_channel_count = 1,
    enable_separate_recognition_per_channel = True,
    model="phone_call",
)

response = client.recognize(config=config, audio=audio)

for result in response.results:
    print("Transcript:{}".format(result.alternatives[0].transcript))




#funciona, mas traduz o inicio só