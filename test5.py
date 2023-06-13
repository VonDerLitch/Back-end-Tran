from google.cloud import speech_v1p1beta1 as speech
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'

client = speech.SpeechClient()

speech_file = "teste_rapido.wav"

with open(speech_file, "rb") as audio_file:
    content = audio_file.read()

audio = speech.RecognitionAudio(content=content)

diarization_config = speech.SpeakerDiarizationConfig(
    enable_speaker_diarization=True,
    min_speaker_count=1,
    max_speaker_count=3,
)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.MP3,
    sample_rate_hertz=44100,
    language_code="pt-BR",
    diarization_config=diarization_config,
)

print("Waiting for operation to complete...")
response = client.recognize(config=config, audio=audio, timeout=90)

# The transcript within each result is separate and sequential per result.
# However, the words list within an alternative includes all the words
# from all the results thus far. Thus, to get all the words with speaker
# tags, you only have to take the words list from the last result:
result = response.results[-1]

words_info = result.alternatives[0].words

# Printing out the output:
for word_info in words_info:
    print(
        "word: '{}', speaker_tag: {}".format(word_info.word, word_info.speaker_tag)
    )