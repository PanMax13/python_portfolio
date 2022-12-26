from pytube import YouTube as yt
import os
from moviepy import *
import moviepy.editor as mp


link = input("Type your link: ")  #get youtube link

def load_video(link): #download youtube vidio from a link
    yt(link).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path='./', filename='video.mp4')

def get_audio():
    load_video(link) # call the function
    my_video = mp.VideoFileClip(r"./video.mp4") # get video
    audio = my_video.audio # get audio from video
    audio.write_audiofile('./audios/audio.mp3') # write a audiofile
    os.remove('./video.mp4') # remove a video

get_audio() # call the fucntion
