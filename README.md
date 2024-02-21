# ALX MVP Project.

# NM Player Version 1.0

# Technology Stack:
* Python for primary programming language for development.
* Tkinter to help with creating a GUI toolkit for building user interface.
* Pygame as a library to utilize audio playback and manipulation.

# Architecture:
* This project follows a modular architecture, separating GUI components from backend logic.
* Tkinter widgets are used to create the user-interface, including buttons, labels, and file dialogs,
* Pygame utilize audio playback, providing functionalities such as play, stop, and playlist management

# Music Player Created with Python 3.12.2 using Tkinter library, Pygame 2.5.2 (SDL 2.82.3) and OS module. 

The tkinter library is used for making the Music Player GUI, os module for the file path, mixer module from pygame library for loading and controlling the music.

# Install the necessary libraries and modules using the pip installer.
pip install tk
python -m pip install pygame
pip install os-sys

# Importing the required libraries and modules in the program
* os- This module helps in interacting with  the operating  system, to fetch the playlist of songs from the specified directories.

* pygame.mixer - Module that is used to load and play music.

* Tkinter- This library will help us in creating a GUI window  for our app.

# Elements of Mixer Module
* load(filename) – This method is used to load a file so that  other actions can be performed on that file. The argument it takes is a file of a supported audio format [.wav, .mp3, .ogg].
* .play() – This method is used to play the music file that was loaded by the .load() method.
* .stop() – This method can stop the loaded file such that it cannot be resumed again.
* .pause() – This method is used to pause a loaded file, at least with this option, it can be played again before needing to be loaded again.
* .unpause() – This method is used to unpause a loaded audio file, also known as the resume option.

# Initializing the mixer module of pygame by using the .init() method.

# Initializing our GUI window for python mp3 music player
* Tk() assignment will be used to initialize the window.
* title() and .geometry() will be used to specify the title and initial geometry of the GUI window of music player.
* resizable() method is used to permit/forbid the user from being able to resize the window. This method takes the arguments in the form of (height, width) ; the default for both of these are True but you can change it 0 or False to forbid the user from resizing the window.
* update() and mainloop() methods are used to put the window on loop and stop it from closing the moment it opens.

# Initializing the GUI Window and the mixer file to create user-defined functions that load, play, pause, resume and stop the music using the OS and mixer modules.
* In the load function, we will ask the user for a directory that has the audio files and then insert all the files in python music player as values in the ListBox widget we will provide as an argument to the function.

* The os.chdir() command is used to change the current working directory to the specified path.
* The tkinter.filedialog.askdirectory() method is used to request a directory from the user.
* The os.listdir() command is used to list all the files in the current working directory in the form of a list.
* The .insert() function, that takes the index, and *elements arguments, is used to insert new element(s) to the Listbox widget on the index parameter.
* The play function, which loads and plays a file, requires 3 arguments: 2 StringVar objects and a ListBox object where the StringVar objects manipulate the text in the Labels that display the current song and its status:
1. Firstly, we set the song_name argument to the name of the song by getting the selected option from the ListBox object and set the status to “Playing”.
2. The .set() method of a StringVar class changes the value of the StringVar object.
3. The .get() method of the ListBox class is used to get certain values from the object. When ACTIVE is provided as an argument to it, it gives you the selected value in the object.
4. The stop(), pause() and resume() functions are all provided with only one StringVar object as argument, use their respective functions and set the StringVar object to their corresponding status.

# Creating LabelFrames and StringVar variables:
* A LabelFrame is a container in Python Tkinter GUIs that acts as a container for different window layouts.
1. The master parameter is the parent window it is associated with.
2. The text parameter is the text that will be displayed on the frame.
3. The width, height parameters are used to specify the width and height of the widget.
4. The bg parameter specifies the background color.
5. The StringVar class is used to manipulate and edit text in Labels, Entry widgets, and OptionMenus.
6. The value parameter denotes the initial value of the widget. Default is ”.
7. The master parameter is the same as in LabelFrames.
8. The .pack() method is one of the 3 Tkinter geometry manager methods that is used to position a widget in its parent using abscissa and ordinate points as though the parent widget/window is a Cartesian Plane. The default is (0, 0) , which is also the North West corner of the parent widget/window.
8. The x, y parameters denote the horizontal and vertical offsets of the widget this method is associated with.

# Placing the widgets in all the three LabelFrames:
* Horizontal and vertical offsets of the widgets, using the .place() method have to be according to their parent widget, not the master window.
* In the playlist LabelFrame we will define a Listbox with a Scrollbar packed to it.
* The ListBox class is used to add a Listbox widget on the window, which displays multiple values in different lines to choose from.
* master and font parameters have the same description as in the other widgets.
* selectbackground parameter defines the color of the background when a value is selected.
* selectmode parameter specifies how many values can be selected at once. Default is ‘browse’ for single selection, and other options include ‘multiple’ and ‘extended’ that allow multiple selection.
* config() method is used to configure some other parameters to the widget it is associated with.
* yscrollcommand parameter defines the Scrollbar object that will be associated with the widget. Similarly, the xscrollcommand defines the vertical Scrollbar.
* The ScrollBar class is used to add a Scrollbar to the music player window.
* master parameter and .command() and .config() method have the same description as in the other widgets.
* orient parameter defines whether the Scrollbar will control the widget vertically, or horizontally.
* set() method is used to set the Scrollbar to another widget.
* In the current_song LabelFrame, we will define 2 Labels; one with a constant text and the other with variable text.
* The Label widget is used to display static text on its parent widget.
* master, width and bg are the same as they are in the Label widget.
* font parameter is used to designate the font family and font effects of the text on the widget.
* textvariable parameter is a Tkinter variable that will automatically update the value in the widget when the argument provided is updated.
* In the control_panel LabelFrame, we will define the buttons whose commands we defined in the last-to-last step.
* The Button class is used to add a button to the GUI application that executes a command when it is pressed.
master, text, bg, font and width parameters have the same description as in the other widgets.
* command parameter is used to define the command the button will execute when it is pressed. It may be a statement, function with or without arguments. The functions without arguments can be executed without anything extra, but you need to use the lambda: keyword to assign functions with arguments.
* The .pack() method, another Tkinter geometry manager method, is used to pack a widget as though the master window or the parent widget was a spreadsheet, in the form of rows and columns.

# Inspiration 
* The inspiration behind this project was emerged by my passion for music with my interest in Python programming.
* Music changed my life in so many ways that one wouldn’t believe and at some point I would struggle with playing other formats due to Apps specifications, so I observed the growing popularity of music streaming services and the ubiquity of music apps, then saw an opportunity to delve into developing a personalized solution that could also allow other people to listen to their choice of music, in any formats of their choice as I will be adding more formats preferences.

# Challenges 
* I encountered challenges that sharpened my skills in integrating Tkinter and Pygame by carefully managing loops and application states. One notable challenge was implementing algorithms for managing playlists, being able to select and play songs and also removing songs and navigating through it.
* I gained a deeper understanding of GUI development using Tkinter and the intricacies of audio processing with Pygame.
* Also learned about event-driven programming paradigms and the significance of asynchronous operations in a GUI applications.
* I discovered techniques for optimizing audio playback performance and ensuring compatibility across different platforms and devices throughout my research and development process.
* I initially conducted research on available libraries and technologies suitable for this project. I started with developing the basic GUI layout using Tkinter and integrating with Pygame for audio playback.
* Iterative testing and debugging were conducted to ensure functionality and stability. 

*
* The side parameter of the .pack() method is used to specify where the widget will be placed on the parent widget or the master window.
* The fill parameter defines whether the widget will fill the horizontal (X has to be provided as argument) or the vertical (Y has to be provided as argument) parts of the parent widget/window or the entire parent (BOTH has to be provided as argument).
* The padx, pady parameters define how many pixels to leave between the widget and the nearby borders (horizontal, vertical).

* The justify parameter of the Label class denotes the alignment of the text on the widget.

  # Live Demo
  https://nicolasmabeleng.github.io/alx-landing_page/
  https://mabelengnicolas.wixsite.com/nm-player-1


Author: Nicolas Mabeleng(mabelengnicolas@outlook.com)
LinkedIn: Nicolas Mabeleng
LinkedIn | Facebook | Instagram | X(Twitter) 
Nicolas Mabeleng
