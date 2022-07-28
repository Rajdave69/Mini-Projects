import re, yt_dlp, os


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



# Possible Returns
# 1. invalid_input_type
# 2. invalid_url
# 3. invalid_output_type

# Inputs
# 1. input_type => "txt" | "csv" | "url"
# 2. is_playlist => bool
# 3. video_source => url | path to input_type
# 4. output_format => mp3 or mp4


class Download:
    def __init__(self, output_format: str, is_playlist: bool , input_type: str, video_source: str) -> None:
        self.video_source = video_source
        self.output_format = output_format
        self.is_playlist = is_playlist
        self.song_id = []
        self.declare_option(output_format)



        # If input is a text file, parse and download
        if input_type == "file":
            try:
                lines = []
                with open(video_source, 'r') as f:
                    for line in f:
                        lines.append(line)
                    f.close()

            except Exception as err:
                self.return_class_error(err)
                lines = []

            print(f"Found {len(lines)} songs in {video_source}")
            for line in lines:

                if re.search(r'^(https?://)?(www\.)?(youtube\.com|youtu\.?be).+$', line):
                    if not self.is_playlist:  # is_playlist is False
                        if "&list=" in line:
                            line = line.split("&list=")[0]
                    self.download(line)
                    print(f"{Color.OKGREEN}Downloaded {line} {Color.ENDC}")

                if not re.search(r'^(https?://)?(www\.)?(youtube\.com|youtu\.?be).+$', line):
                    print(f"{Color.WARNING}Skipping Invalid URL on Line: {Color.BOLD}{line}{Color.ENDC}")




        elif input_type == "url":
            # Check if the URL is valid
            if not re.search(r'^(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+$', self.video_source):
                self.return_class_error("invalid_url")

            if not self.is_playlist:    # is_playlist is False
                if "&list=" in self.video_source:
                    self.video_source = self.video_source.split("&list=")[0]

            elif self.is_playlist:    # is_playlist is True
                if "&list=" not in self.video_source:
                    self.is_playlist = False
                    print(f"{Color.WARNING}Could not find playlist ID in Playlist Download. Downloading single video instead.{Color.ENDC}")
            # Download
            self.download(self.video_source)

        else:
            self.return_class_error("invalid_input_type")


    def return_class_error(self, msg) -> None:
        print(f"{Color.FAIL}{msg}{Color.ENDC}")
        return msg


    def declare_option(self, post) -> None:
        if post == "mp3":
            global ydl_opts
            ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320',
                }   ]   }
        elif post == "mp4":
            ydl_opts = {
            'format': 'best',
            }
        else:
            self.return_class_error("invalid_output_type")


    def download(self, url) -> None:

        video_title = []
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            video = ydl.extract_info(url, download=True)
            video_title.append(video.get('title', None))
            for file in os.listdir('./'):
                if file.endswith('.mp3') or file.endswith('.mp4'):
                    try:
                        if not os.path.exists('./downloads'):
                            os.makedirs('./downloads')
                        os.rename(file, './downloads/' + file)
                    except FileExistsError:
                        print(f"{Color.WARNING}File {file} already exists.{Color.ENDC}")
                    except Exception as err:
                        return self.return_class_error(err)
