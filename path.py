import os

#Getting Absolute path of the parent directory of app.py|path.py file

APP_DIR_PATH = os.path.dirname(__file__)

#defining the paths of folders

IMAGES_DIR_PATH = f"{APP_DIR_PATH}/images/"
VIDEOS_DIR_PATH = f"{APP_DIR_PATH}/videos/"
AUDIO_PATH = f"{APP_DIR_PATH}/audios/"
IMAGES_PATH = f"{APP_DIR_PATH}/images/" 

#Specify the path of image viewer and video player you want to use for showing images and playing videos

IMAGE_VIEWER_PATH = "" #eg : image viewer exe path C:/program files(x86)/imageviewer.exe or something like this 
VIDEO_PLAYER_PATH = "" #eg : vlc media player's exe path C:/program files(x86)/videolan/vlc.exe