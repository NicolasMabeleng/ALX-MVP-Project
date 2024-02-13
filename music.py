# Importing necessary modules
import tkinter
from tkinter import *
from tkinter import filedialog
import pygame
import os
import pygame.mixer as mixer

# initializing the mixer
mixer.init()

# Functions
def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    song_name.set(songs_list.get(ACTIVE))
    
    mixer.music.load(songs_list.get(ACTIVE))
    mixer.music.play()

    status.set("Song Playing")

def stop_song(status: StringVar):
    mixer.music.stop()
    status.set("Song Stopped")

def load(listbox):
    os.chdir(filedialog.askdirectory(title="Browse Music File"))

    tracks = os.listdir()

    for track in tracks:
        listbox.insert(END, track)

def pause_song(status: StringVar):
    mixer.music.pause()
    status.set("Song Paused")

def resume_song(status: StringVar):
    mixer.music.unpause()
    status.set("Song Resumed")

# Creating the master GUI for Python Music Player
root = Tk() # used to initialize the window
root.geometry('700x220') # used to specify the initial geometry of the GUI window
root.title('NM Player V1.0') # title of music player
root.resizable(0, 0) # used to permit/ forbid user from being able to resize the indow

# Creating the LabelFrames and StringVar variables
song_frame = LabelFrame(root, text='Current Song', bg='darkgreen', width=400, height=80)
song_frame.place(x=0, y=0)

button_frame = LabelFrame(root, text='ControlButtons', bg='darkgreen', width=400, height=120)
button_frame.place(y=80)

listbox_frame = LabelFrame(root, text='Playlist', bg='darkgreen')
listbox_frame.place(x=400, y=0, height=200, width=300)

current_song = StringVar(root, value='<Not Selected>')
song_status = StringVar(root, value='<Not Available>')

# Playlist ListBox
playList = Listbox(listbox_frame, font=('Helvetica', 11), selectbackground='green3')

scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=BOTH)

playList.config(yscrollcommand=scroll_bar.set)

scroll_bar.config(command=playList.yview)

playList.pack(fill=BOTH, padx=5, pady=5)

# SongFrame Labels
Label(song_frame, text='Currently Playing:', bg='orange1', font=('Times',10, 'bold')).place(x=5, y=20)

song_lbl = Label(song_frame, textvariable=current_song, bg='thistle1', font=("Times", 12), width=25)
song_lbl.place(x=150, y=20)

# Buttons in the main screen
pause_btn = Button(button_frame, text='Pause', bg='orange1', font=("Arial", 13), width=7, command=lambda: pause_song(song_status))
pause_btn.place(x=15, y=10)

stop_btn = Button(button_frame, text='Stop', bg='red1', font=("Arial", 13), width=7, command=lambda: stop_song(song_status))
stop_btn.place(x=105, y=10)

play_btn = Button(button_frame, text='Play', bg='green', font=("Arial", 13), width=7, command=lambda: play_song(current_song, playList, song_status))
play_btn.place(x=195, y=10)

resume_btn = Button(button_frame, text='Resume', bg='steelblue', font=("Arial", 13), width=7, command=lambda: resume_song(song_status))
resume_btn.place(x=285, y=10)
    
load_btn = Button(button_frame, text='Browse Music Folder', bg='whitesmoke', font=("Arial", 13), width=35, command=lambda: load(playList))
load_btn.place(x=10, y=55)

# Label that displays the state of the music
Label(root, textvariable=song_status, bg='darkgreen', font=('Arial', 9), justify=LEFT).pack(side=BOTTOM, fill=X)

# finalizing the GUI
root.update() #put the window on loop 
root.mainloop() # and stop it from closing the moment it opens