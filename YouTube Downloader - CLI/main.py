# import os
import re, yt_dlp

class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Download:
    def __init__(self, video_url, output_format, is_playlist):
        self.url = video_url
        self.format = output_format
        self.is_playlist = is_playlist
        self.song_id = []
        self.declare_option(output_format)
        self.download(video_url)





    def declare_option(self, post):
        if post == "mp3":
            global ydl_opts
            ydl_opts = {
            'format': 'bestaudio/best',
            'ffmpeg-location': 'C:\\Users\Raj Dave\AppData\Local\Programs\Python\Python310\Lib\site-packages\\ffmpeg',
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320',
                }   ]   }
        elif post == "mp4":
            ydl_opts = {
            'format': 'best',
            'ffmpeg-location': 'C:\\Users\Raj Dave\AppData\Local\Programs\Python\Python310\Lib\site-packages\\ffmpeg',
            }
        else:
            print("Invalid format")
            return False



    def download(self, url):
        if not re.search(r'^(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+$', url):
            return "invalid URL"

        if "=" in url:
            self.song_id.append(url.split("=")[1])
        elif url.startswith("youtu.be"):
            self.song_id.append(url.split("/")[-1])
        elif "/" in url:
            self.song_id.append(url.split("/")[3])
        else:
            self.song_id.append(None)

        song_id = self.song_id[0]
        song_id.strip('=').strip('list=')

        video_title = []

        if not self.is_playlist:
            if "&list=" in url:
                url = url.split("&list=")[0]


        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            video = ydl.extract_info(url, download=True)
            video_title.append(video.get('title', None))
            # for file in os.listdir('./'):
                # if file.endswith('.mp3') or file.endswith('.mp4'):
                #     try:
                #         os.rename(file, f'./download/{video_title[0]}.{self.format}')
                #     except FileExistsError:
                #         print(Color.FAIL, "File {file} already exists.")
                #     except Exception as err:
                #         print(Color.FAIL, f"Error {err}")







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


# >> Get Content TYPE
content_type = input(f"Enter the type of content you want to download: {Color.BOLD}(Video/Playlist) ")
if content_type is None:
    print(Color.FAIL, "Invalid input")
    exit()
if content_type.lower().startswith("v"):
    is_playlist = False
elif content_type.lower().startswith("p"):
    is_playlist = True
else:
    print(f"{Color.FAIL}Error: Invalid input. You must reply with V or P.{Color.ENDC}")
    exit()
print(" ")



# >> Get Content input Type
input_type = input(f"Do you want to give a .txt file or a URL? {Color.BOLD}(.txt/URL) ")
if input_type is None:
    print(f"{Color.FAIL}Error: Invalid input. You must reply with .txt or URL.{Color.ENDC}")
    exit()
if input_type.lower().replace(".", "").startswith("t"):
    input_type = "txt"
elif input_type.lower().startswith("u"):
    input_type = "url"
else:
    print(f"{Color.FAIL}Error: Invalid input. You must reply with .txt or URL.{Color.ENDC}")
    exit(1)
print(" ")


# >> Get Content URL
url = input(f"{Color.BOLD}Enter YouTube Video URL: ")
if not url:
    print(Color.FAIL, "Error: You must enter a URL.")
    exit(1)

if not re.search(r'^(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+$', url):
    print(f"{Color.FAIL}Error: Invalid YouTube URL.{Color.ENDC}")
    exit(1)
print(" ")


# >> Get Post Processing
post = input(f"What format do you want the Video to be in? {Color.BOLD}(mp3/mp4) ")
if post is None:
    print("Format not specified. Defaulting to mp3.")
    video_format = "mp3"
if post.lower().startswith("mp3"):
    video_format: str = "mp3"
elif post.lower().startswith("mp4"):
    video_format: str = "mp4"
else:
    print(f"{Color.FAIL}Error: Invalid input. You must reply with mp3 or mp4.{Color.ENDC}")
    exit(1)
print(" ")

print(Color.HEADER, f"{Color.BOLD}Downloading...{Color.ENDC}")


try:
    # noinspection PyUnboundLocalVariable
    Download(url, video_format, is_playlist)
except Exception as e:
    print(f"{Color.FAIL}Error: {e}{Color.ENDC}")
    exit()

