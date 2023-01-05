# this code dowload and write text of youtube  video. https://www.youtube.com/watch?v=pTCxXZh6VyE - link from example

from pytube import YouTube as yt
import sys, os
from moviepy import *
import moviepy.editor as mp
import speech_recognition as sr
from pydub import AudioSegment



link = sys.argv[1]  #get youtube link

def load_video(my_link): #download youtube vidio from a link
    yt(my_link).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path='./', filename='video.mp4')

def get_audio():
    load_video(link) # call the function
    my_video = mp.VideoFileClip(r"./video.mp4") # get video
    audio = my_video.audio # get audio from video
    audio.write_audiofile('./audios/audio.mp3') # write a audiofile
    os.remove('./video.mp4')

def get_audio_text(audio_file):
    #formating audio from mp3 to wav
    sound = AudioSegment.from_mp3(f'./audios/{audio_file}.mp3')
    sound.export(f"./audios/{audio_file}.wav", format="wav")

    AUDIO_FILE = f'./audios/{audio_file}.wav' # get sourse to .wav file

    r = sr.Recognizer()

    with sr.AudioFile(AUDIO_FILE) as source: # listening audio-file
        audio = r.record(source) # recording....
        with open("./text_of_audio.txt", "w") as file: #open text file
            file.write(r.recognize_google(audio)) # writing the text of video.
get_audio() # call the fucntion

get_audio_text('audio') # call transcripting function
