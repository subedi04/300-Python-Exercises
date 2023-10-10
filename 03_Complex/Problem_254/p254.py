'''
Write a Python Program to play a wav file 
in python using pydub library
'''
from pydub import AudioSegment
from pydub.playback import play

audio = AudioSegment.from_wav("au.wav")
play(audio)