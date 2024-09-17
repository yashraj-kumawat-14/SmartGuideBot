from tkinter import Tk, PhotoImage, Label, Frame, Text, Button, END
import tkinter.messagebox as message
import speech_recognition as sr
import filterate
import data
import audio_info
import os, pygame, time, subprocess
from path import *
from fuzzywuzzy import process

data = data.data
audio_info = audio_info.audio_info

# Initialize the GUI components
def setup_gui():
    global root, userInput, botInput

    root = Tk()
    screen_height = root.winfo_screenheight()
    screen_width = root.winfo_screenwidth()

    root.geometry(f"{screen_width}x{screen_height}")
    root.title("Chatbot@S.I.T.E")
    root.config(background="white")

    main_frame = Frame(root)
    main_frame.pack(fill="both", expand=True)
    main_frame.rowconfigure(0, weight=1)
    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)
    main_frame.columnconfigure(2, weight=1)

    user_frame = Frame(main_frame, borderwidth=2, relief="groove")
    user_frame.grid(row=0, column=0, sticky="nsew")

    chatbot_frame = Frame(main_frame)
    chatbot_frame.grid(row=0, column=1, sticky="nsew")
    chatbot_frame.rowconfigure(0, weight=1)
    chatbot_frame.rowconfigure(1, weight=1)
    chatbot_frame.columnconfigure(0, weight=1)

    bot_response_frame = Frame(main_frame, borderwidth=2, relief="groove")
    bot_response_frame.grid(row=0, column=2, sticky="nsew")
    
    background_image = PhotoImage(file="./chatbot_background2.png")
    background_image = background_image.subsample(30, 30)  # Reduce the image size by half

    background_label = Label(chatbot_frame, image=background_image, bg="white")
    background_label.grid(row=0, column=0, sticky="nsew")

    # User frame work starts here
    youLabel = Label(user_frame, text="YOU : ", background="white", fg="black", font="COPPER 20 bold")
    youLabel.pack(fill="x")

    userInput = Text(user_frame, width=35, height=10, state="disabled", wrap="word", font="COPPER 25 bold",
                     padx=10, pady=20)  # Added padding
    userInput.pack(fill="both", expand=True)

    # Computer frame work starts here
    botLabel = Label(bot_response_frame, text="Computer : ", background="white", fg="black", font="COPPER 20 bold")
    botLabel.pack(fill="x")

    botInput = Text(bot_response_frame, width=35, height=10, state="disabled", wrap="word", font="COPPER 25 bold",
                    padx=10, pady=20)  # Added padding
    botInput.pack(fill="both", expand=True)

    # Listen button
    listen_button = Button(chatbot_frame, text="Click here \nto speak\n", command=listen, height=5, width=20, bg="black", fg="gold", font="COPPER 45 bold")
    listen_button.grid(row=1, column=0, sticky="nsew")

    root.mainloop()

# LISTEN TO USER
def listen():
    global usertext
    # recognizer = sr.Recognizer()

    # with sr.Microphone() as source:
    #     print("Adjusting for ambient noise... Please wait.")
    #     recognizer.adjust_for_ambient_noise(source)
    #     print("Listening...")
    #     audio = recognizer.listen(source)

    #     try:
    #         usertext = recognizer.recognize_google(audio, language='hi-IN')
    #     except sr.UnknownValueError:
    #         usertext = ""
    #     except sr.RequestError:
    #         usertext = ""

    #     process_input()
    usertext = input("enter something : ")
    process_input()

# PROCESS THE PROMPT OF USER INPUT
def process_input():
    global usertext, computertext
    print(usertext)
    if not usertext:
        usertext = "undefined"
        computertext = "I don't understand. Can you ask something relevant?"
        update_output(usertext, computertext)
        return

    # Apply filtering to the user input
    filterInputlist = filterate.filtrate(usertext)
    
    computertext = get_best_match(usertext, data)
    if not computertext:
        usertext="undefined"
        computertext="add some data or speak something relavent."

    # Update the GUI with the results
    update_output(usertext, computertext)

# UPDATE GUI WITH NEW USERTEXT AND COMPUTERTEXT
def update_output(usertext, computertext):
    print(usertext)
    global userInput, botInput
    userInput.config(state="normal")
    userInput.delete(1.0, END)
    userInput.insert(END, usertext)
    userInput.config(state="disabled")

    botInput.config(state="normal")
    botInput.delete(1.0, END)
    botInput.insert(END, computertext)
    botInput.config(state="disabled")
    root.update()

    # IF THE USER TEXT IS VALID THEN SPEAK THE COMPUTERTEXT IN SPEAKER
    if usertext != "undefined":
        speak(computertext)

# SPEAK OUT THE COMPUTERTEXT
def speak(computertext):
    # Getting relavent path audio file to speak as output of computer to the usertext

    audio_file_path = f"{AUDIO_PATH}{audio_info.get(computertext, [None])[0]}"
    
    if audio_file_path:
        # Initialize the mixer
        pygame.mixer.init()

        # Load and play the MP3 file
        pygame.mixer.music.load(f'{audio_file_path}')
        pygame.mixer.music.play()

        # Keep the script running while the music plays
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    #Getting the relavent video and image name associated with the computertext        
    video_name = audio_info.get(computertext, [None])[1]
    image_name = audio_info.get(computertext, [None])[2]

    # show video/image if present 
    if video_name:
        showvideo(video_name)

    if image_name:
        showimage(image_name)

# get_best_match function returns the best key of dictionary matching with the user prompt
def get_best_match(user_input, prompts_dict):
    # Extract the prompts (keys) from the dictionary
    prompts = list(prompts_dict.keys())
    
    # Find the best match for the user input
    if prompts:
        best_match, score = process.extractOne(user_input, prompts)
    else :
        return None
    
    # Return the corresponding answer if a good match is found
    if score > 70:  # You can adjust this threshold as needed
        return prompts_dict[best_match]
    else:
        return None

# showvideo will play the video and will exits the video when the playback is over
def showvideo(video_name):
    # Start Video player with the video
    video_path = VIDEOS_DIR_PATH + video_name

    process = subprocess.Popen([
        VIDEO_PLAYER_PATH,  # VLC media player command
        video_path,  # Path to the video file
        '--play-and-exit'  # Automatically exit when playback ends
    ])
    process.wait()
# showimage will present the image and will exits the image viewer window after the time specified in time.sleep(<time>) function 
def showimage(image_name):
    image_path = IMAGES_DIR_PATH + image_name
    print(image_path)
    process = subprocess.Popen([
        IMAGE_VIEWER_PATH,
        image_path,  # Path to the image file
    ])
    time.sleep(5)
    process.terminate()

#initializing the usertext and computertext
usertext = "undefined"
computertext = "Sorry, I didn't understand that."

#starting the app here.

setup_gui()
