# Biblioteca
from google.cloud import speech
import os

# Autenticador
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'

client = speech.SpeechClient()

# O nome do arquivo, com key, pegando na cloud
gcs_uri = "gs://exemplo-teste123/audio-files/grav.wav"

def transcribe_speech():
  audio = speech.RecognitionAudio(uri=gcs_uri)

  config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    language_code="pt-BR",
    use_enhanced=True,
    model="latest_long",
    audio_channel_count=2,
    enable_word_confidence=True,
    enable_word_time_offsets=True,
    enable_automatic_punctuation=True,
    
  )

  # Detecta o audio
  operation = client.long_running_recognize(config=config, audio=audio)

  print("Espere Terminar...")
  response = operation.result(timeout=90)

  for result in response.results:
    alternative = result.alternatives[0]
    print("Transcrissão: {}".format(result.alternatives[0].transcript))
    print("Confiança: {}".format(result.alternatives[0].confidence))
    for word_info in alternative.words:
            word = word_info.word
            start_time = word_info.start_time
            end_time = word_info.end_time

            print(
                f"{word},{start_time.total_seconds()},{end_time.total_seconds()}"
            )
  

transcribe_speech()

#teste feito com Wav 44100, tentativa com time elpase