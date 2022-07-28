import os, re
from backend import Download, Color


version = "0.2.0"
supported_formats = ["mp3", "mp4"]
supported_file_types = ["txt"]


# Start the program
print(" ")
print(Color.OKBLUE, """
$$$$$$$\              $$\               $$\     $$\                $$$$$$$$\        $$\                       $$$$$$$\                                    $$\                           $$\                     
$$  __$$\             $  |              \$$\   $$  |               \__$$  __|       $$ |                      $$  __$$\                                   $$ |                          $$ |                    
$$ |  $$ | $$$$$$\  $$\_/$$$$$$$\        \$$\ $$  /$$$$$$\  $$\   $$\ $$ |$$\   $$\ $$$$$$$\   $$$$$$\        $$ |  $$ | $$$$$$\  $$\  $$\  $$\ $$$$$$$\  $$ | $$$$$$\   $$$$$$\   $$$$$$$ | $$$$$$\   $$$$$$\  
$$$$$$$  | \____$$\ \__|$$  _____|        \$$$$  /$$  __$$\ $$ |  $$ |$$ |$$ |  $$ |$$  __$$\ $$  __$$\       $$ |  $$ |$$  __$$\ $$ | $$ | $$ |$$  __$$\ $$ |$$  __$$\  \____$$\ $$  __$$ |$$  __$$\ $$  __$$\ 
$$  __$$<  $$$$$$$ |$$\ \$$$$$$\           \$$  / $$ /  $$ |$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$$$$$$$ |      $$ |  $$ |$$ /  $$ |$$ | $$ | $$ |$$ |  $$ |$$ |$$ /  $$ | $$$$$$$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|
$$ |  $$ |$$  __$$ |$$ | \____$$\           $$ |  $$ |  $$ |$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$   ____|      $$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$ |$$ |  $$ |$$  __$$ |$$ |  $$ |$$   ____|$$ |      
$$ |  $$ |\$$$$$$$ |$$ |$$$$$$$  |          $$ |  \$$$$$$  |\$$$$$$  |$$ |\$$$$$$  |$$$$$$$  |\$$$$$$$\       $$$$$$$  |\$$$$$$  |\$$$$$\$$$$  |$$ |  $$ |$$ |\$$$$$$  |\$$$$$$$ |\$$$$$$$ |\$$$$$$$\ $$ |      
\__|  \__| \_______|$$ |\_______/           \__|   \______/  \______/ \__| \______/ \_______/  \_______|      \_______/  \______/  \_____\____/ \__|  \__|\__| \______/  \_______| \_______| \_______|\__|      
              $$\   $$ |                                                                                                                                                                                        
              \$$$$$$  |                                                                                                                                                                                        
               \______/                                                                                                                                                                                         
""" + Color.ENDC)
print(" ")
print(f"{Color.OKGREEN}Welcome to Raj's Youtube Downloader")
print(f"Made by Raj Dave#3215. Version {version}{Color.ENDC}")
print(" ")
print(" ")



# Inputs
# 1. input_type => txt or url
# 2. is_playlist => True or False
# 3. video_source => YT url or filepath
# 4. output_format => mp3 or mp4


class Initialize:
    def __init__(self):
        self.input_type = ""    # "file" or "url"
        self.is_playlist = False    # True or False
        self.video_source = ""  # filepath or actual url
        self.output_format = "" # mp3/mp4

        self.get_input_type() # Get input_type and video_source
        self.get_output_format() # Get output_format
        self.get_is_playlist() # Get is_playlist

        dwn = Download(input_type=self.input_type, is_playlist=self.is_playlist, video_source=self.video_source, output_format=self.output_format)
        if dwn in ["invalid_input_type", "invalid_url", "invalid_output_type"]:
            print(f"{Color.FAIL}There was an error downloading the file!")
            print(f"Error code: {dwn}{Color.ENDC}")



    def declare_option(self, output_format):
        self.output_format = output_format
        self.is_playlist = False
        self.input_type = ""
        self.video_source = ""


    def get_input_type(self):   # Gets input_type and video_source
        self.input_type = input("Enter input type: (File/URL) ")

        if self.input_type.lower().startswith("f"): # If it's a File
            self.input_type = "file"
            self.video_source = input("Enter filepath: ")   # Get filepath
            if not os.path.exists(self.video_source):   # If filepath doesn't exist
                print(f"{Color.FAIL}Filepath does not exist{Color.ENDC}")
                self.get_input_type()
            elif not self.video_source.endswith("txt") :  # If file is not txt/csv
                print(f"{Color.FAIL}File format must be match {supported_file_types}{Color.ENDC}")
                self.get_input_type()


        elif self.input_type.lower().startswith("u"):  # If it's a URL
            self.input_type = "url"
            self.video_source = input("Enter URL: ")    # Get URL
            if not re.match(r'^(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+$', self.video_source):  # Check YouTube URL with regex
                print(f"{Color.FAIL}Invalid URL{Color.ENDC}")
                self.get_input_type()

        else:
            print(f"{Color.FAIL}Invalid input type. Send either F or U{Color.ENDC}")
            self.get_input_type()



    def get_output_format(self):    # Gets output_format
        self.output_format = input("Enter output format: ") # Get output_format
        if self.output_format.lower().startswith("mp3"):    # If it's mp3
            self.output_format = "mp3"
        elif self.output_format.lower().startswith("mp4"):  # If it's mp4
            self.output_format = "mp4"
        else:
            print(f"{Color.FAIL}Invalid output format{Color.ENDC}. Supported formats: {supported_formats}")
            self.get_output_format()


    def get_is_playlist(self):  # Gets is_playlist
        if self.input_type == "url":
            if "&list=" in self.video_source:
                self.is_playlist = input("Detected a Playlist URL. Do you want to download the whole playlist? (y/n): ")
                if self.is_playlist.lower().startswith("y"):
                    self.is_playlist = True
                elif self.is_playlist.lower().startswith("n"):
                    self.is_playlist = False

                else:
                    print(f"{Color.FAIL}Invalid input{Color.ENDC}. Reply with y or n")
                    self.get_is_playlist()


        if self.input_type == "file":
            self.is_playlist = input("This file may contain a playlist. Do you want to download the whole playlist for each video? (y/n): ")
            if self.is_playlist.lower().startswith("y"):
                self.is_playlist = True
            elif self.is_playlist.lower().startswith("n"):
                self.is_playlist = False
            else:
                print(f"{Color.FAIL}Invalid input{Color.ENDC}. Reply with y or n")
                self.get_is_playlist()





while True:
    Initialize()
    print(" ")
    print(" ")
    print(" ")
