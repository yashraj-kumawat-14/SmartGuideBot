# SmartGuideBot
SmartGuideBot is a Python-based chatbot. It helps with admissions, scholarships, faculty info, and campus navigation. Its flexible design allows it to be used for other purposes also, like hospital navigation or task scheduling.

## Project Images
![image alt](https://github.com/yashraj-kumawat-14/SmartGuideBot/blob/main/images/project_image1.png)

![image alt](https://github.com/yashraj-kumawat-14/SmartGuideBot/blob/main/images/project_image2.png)

![image alt](https://github.com/yashraj-kumawat-14/SmartGuideBot/blob/main/images/project_image3.png)

## Features

- **Dynamic Query Handling**: Responds to user queries about campus-related topics including admissions, scholarships, faculty, and more.
- **Multimedia Integration**: Displays videos and images to provide visual guidance on campus locations, departmental information, and schedules.
- **Adaptable Framework**: Easily customizable for different environments, such as hospitals, large events, or task management.

## Getting Started

To get started with SmartGuideBot, follow these steps:

1. **Clone the Repository**
   ```bash
   https://github.com/yashraj-kumawat-14/SmartGuideBot.git

2. **Navigate to the Project Directory**
   ```bash
   cd SmartGuideBot

3. **Installing required modules**
   ```bash
   pip install -r requirements.txt

4. **Execute install.py**
   ```bash
   python install.py

5. **Define Paths**
   FOR WINDOWS
   If you are in windows then in path.py file define path of video player's .exe file (eg: C:/program files/videolan/vlc.exe) and image viewer's .exe file (eg: C:/program files/irfanview/i_view.exe)

   FOR LINUX
   If you are in linux then in path.py write "vlc" (if vlc is installed) in VIDEO_PLAYER_PATH variable and in IMAGE_VIEWER_PATH write "image-viewer-name".
   
6. **Execute add_data.py**

   Add some data into it according to your needs.
you should be connected to internet while adding / updating data. The internet is necessary inorder to download audio file for the response. You can also attach video & image in add_data.py along with the user prompt and response. This will copy video & image if selected to the videos/inages folder in the project's directory.
   ```bash
   python add_data.py
   
7. **Execute the app**
   ```bash
   python app.py

## Important Notes

- **Microphone and Speakers**: Ensure that your microphone and speakers are functioning correctly. The bot relies on voice input and output, so proper operation of these devices is crucial for its performance.
  - **Microphone**: Test your microphone to confirm that it is capturing sound clearly and without distortion.
  - **Speakers**: Check your speakers to make sure they are working and producing sound at an appropriate volume.


