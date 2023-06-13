# Biblioteca utilizadas
from google.cloud import speech
import os
from docx import Document
from test2 import upload_to_bucket
from google.cloud import storage
from tkinter import filedialog

# Autenticador que puxa na google
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'

client = speech.SpeechClient()

storage_client = storage.Client()

user_file = filedialog.askopenfilename()

gcs_uri = 

# O nome do arquivo, com key, pegando na cloud

#aciona a biblioteca
Document = Document()

def transcribe_speech():
  audio = speech.RecognitionAudio(uri=gcs_uri)
  #configuração da API, econdig'Linear16' para o tipo do audio.
  #Sample_rate_heartz 44100 que é o heartz do arquivo, que eu defini como padrão, caso o arquvio não tenha essa quantidade, teremos que formatar.
  #language_code, é a linguagem de reconhecimento
  #use_enchanced,um aprimoramento para chamadas de audio longas
  #model, o modelo do audio, neste caso longa
  #audio_channel_count, quantos canais ele detectou no audio
  #enable_word_confidence, a confiança na tradução
  #enable_word_time_offsets, para colocar tempo na tradução
  #enable_automatic_punctuation,pontuação automatica
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
  #Tempo de espera
  response = operation.result(timeout=90)
  #Pega o nome do arquivo
  p = input(str("digite o nome do arquivo: "))
  #looping para colar o texto no docx e salvar
  for result in response.results:
    Document.add_paragraph(result.alternatives[0].transcript)

    Document.save("{}.docx".format(p))

#executar a def
file_path = r'C:\Users\kelvin.silveira\Documents\Transcrisor-main'
upload_to_bucket("documents/{}".format(user_file), os.path.join(file_path, user_file), 'exemplo-teste123')
transcribe_speech()

#teste feito com Wav 44100, Comprende o audio e transforma em Word.