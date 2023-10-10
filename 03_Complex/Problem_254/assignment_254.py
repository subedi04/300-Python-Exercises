'''
Write a Python Program to play a wav file in python using pydub library
'''
from pydub import AudioSegment
from pydub.playback import play

# Replace 'your_audio_file.wav' with the path to your WAV file
audio_path = 'your_audio_file.wav'

# Load the audio file
audio = AudioSegment.from_file(audio_path, format="wav")

# Play the audio
play(audio)
