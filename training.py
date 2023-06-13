from google.cloud import speech

# Função de confiabilidade
def transcribe_audio_with_confidence(audio_file):
    client = speech.SpeechClient.from_service_account_json('key.json')

    with open(audio_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
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

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        alternative = result.alternatives[0]
        transcript = alternative.transcript
        for word_info in alternative.words:
            word = word_info.word
            confidence = word_info.confidence
            print(f"Word: {word}\tConfidence: {confidence}")

# Executar
# Lembrando que o speech.Recognitions é usado apenas de teste, e tem um limite de tamanho se não for usado do bucket
audio_file = 'grav.wav'
transcribe_audio_with_confidence(audio_file)