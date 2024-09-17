from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as message
import shutil
import sqlite3 
import os
from gtts import gTTS
import path

video_path = None
image_path = None

def select(file="video"):
    global video_path, image_path
    if file=="video":
        video_path = filedialog.askopenfilename(title="Select a mp4 video file", filetypes=[("mp4", ".mp4")])

    if file=="image":
        image_path = filedialog.askopenfilename(title="Select a mp4 video file", filetypes=[("png", ".png"), ("jpeg", ".jpg")])

def ok():
    if not prompt.get():
        user_text_label.config(fg="red")
        return None
    else:
        user_text_label.config(fg="black")

    if not response.get():
        response_label.config(fg="red")
        return None
    else:
        response_label.config(fg="black")

    conn = sqlite3.connect("smartguidebot.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT MAX(id) + 1 from data")
    id = cursor.fetchone()[0]
    
    try:
        tts = gTTS(text=response.get(), lang='hi')
        tts.save(f"{path.AUDIO_PATH}{id}.mp3")
    except:
        message.showerror("Error", "Internet not connected properly.")
        return None

    try:
        video_name = os.path.basename(video_path)
        video_button.config(text="copying...", fg="yellow", bg="black")
        shutil.copy(video_path, path.VIDEOS_DIR_PATH)
        video_button.config(text="done !!", fg="green", bg="white")
    except:
        video_name = ""

    try:
        image_name = os.path.basename(image_path)
        image_button.config(text="copying...", fg="yellow", bg="black")
        shutil.copy(image_path, path.IMAGES_DIR_PATH)
        image_button.config(text="done !!", fg="green", bg="white")

    except:
        image_name = ""
    try:
        cursor.execute(f"INSERT INTO data (prompt, response, audio, video, image) VALUES ('{prompt.get()}', '{response.get()}', '{id}.mp3', '{video_name}', '{image_name}')")
    except:
        message.showerror("Error", "Error adding / updating the data in database.")
        root.destroy()
        return None 
    conn.close()

    prompt.set("")
    response.set("")
    video_path = None
    image_path = None
    
    image_button.config(fg="black", text="select")
    video_button.config(fg="black", text="select")

    message.showinfo("Info", "Data was added / updated successfully.")


root = Tk()
root.title("Add/Update Data")
root.geometry("350x250")
root.resizable(False, False)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

mainframe = Frame(root, borderwidth=2, relief="groove")
mainframe.grid(row=0, column=0)

user_text_label = Label(mainframe, text="User Prompt : ")
user_text_label.grid(row=0, column=0)

response_label = Label(mainframe, text="Computer Response : ")
response_label.grid(row=1, column=0)

video_label = Label(mainframe, text="Video File(Optional) : ")
video_label.grid(row=2, column=0)

image_label = Label(mainframe, text="Image File(Optional) :")
image_label.grid(row=3, column=0)

prompt = StringVar()
prompt.set("")
user_text_entry = Entry(mainframe, textvariable=prompt)
user_text_entry.grid(row=0, column=1)

response = StringVar()
response.set("")
response_entry = Entry(mainframe, textvariable=response)
response_entry.grid(row=1, column=1)

video_button = Button(mainframe, text="Select", command=lambda file = "video": select(file))
video_button.grid(row=2, column=1)

image_button = Button(mainframe, text="Select", command=lambda file = "image": select(file))
image_button.grid(row=3, column=1)

ok_button = Button(mainframe, text="Add / Update", bg="orange", command=ok)
ok_button.grid(row=4, column=0, columnspan=2, sticky="ew")

root.mainloop()