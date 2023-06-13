from google.cloud import speech
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'

client = speech.SpeechClient()

audio = speech.RecognitionAudio(uri="gs://exemplo-teste123/audio-files/Ligacao44100.wav")
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    language_code="pt-BR",
)

operation = client.long_running_recognize(config=config, audio=audio)

print("Waiting for operation to complete...")
response = operation.result(timeout=90)

# Each result is for a consecutive portion of the audio. Iterate through
# them to get the transcripts for the entire audio file.
for result in response.results:
    # The first alternative is the most likely one for this portion.
    print("Transcript: {}".format(result.alternatives[0].transcript))
    print("Confidence: {}".format(result.alternatives[0].confidence))


#funciona bem, mas sem speaker's
#Sem ponto e virgula
#Sem Gravar as letras