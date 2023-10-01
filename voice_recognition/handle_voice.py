# import speech_recognition as sr
# from bidi.algorithm import get_display
# from arabic_reshaper import reshape
# from pydub import AudioSegment
# from gtts import gTTS
# import os

# def voice_handler():
#     # this function to convert any audio file to .wav
#     def convert_ogg_to_wav(audio_filename, wav_file):
#         sound = AudioSegment.from_file(audio_filename)
#         sound.export(wav_file, format="wav")
#     # this function to convert the audio file to text
#     def convert_speech_to_text(filename):
#         r = sr.Recognizer()
#         with sr.AudioFile(filename) as source:
#             audio = r.record(source)  # read the entire audio file
#         try:
#             # Use the Google Speech Recognition API for Arabic
#             text = r.recognize_google(audio, language='ar-AR')
#             reshaped_text = reshape(text)
#             return reshaped_text
#         except sr.UnknownValueError:
#             return "Sorry, I could not understand the audio."
#         except sr.RequestError:
#             return "Sorry, I'm currently experiencing technical issues."
#     other_filename="../voice_message/audio.ogg"
#     wav_filename="../voice_message/new.wav"
#     convert_ogg_to_wav(other_filename, wav_filename)
#     return convert_speech_to_text(wav_filename)


# Import the Speech-to-Text client library
from google.protobuf import wrappers_pb2
from google.cloud import speech


def voice_handler():
    # Instantiates a client
    client=speech.SpeechClient.from_service_account_file("../voice_recognition/key.json")

    file_name = "../voice_message/audio.ogg"

    with open(file_name,"rb") as f:
      data = f.read()

    audio_file = speech.RecognitionAudio(content=data)

    config=speech.RecognitionConfig(
      encoding=speech.RecognitionConfig.AudioEncoding.OGG_OPUS,
      sample_rate_hertz=48000,
      language_code="ar-IL",
      model="command_and_search",
      audio_channel_count=1,
      enable_word_time_offsets=True,
    )
    response = client.recognize(
      config=config,
      audio=audio_file
    )
    for result in response.results:
      return result.alternatives[0].transcript