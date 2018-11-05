from log import Logger
from hooks import download_hook

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '/songs/%(title)s.%(ext)s',
    'postprocessors':[{
        'key':'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
    'logger': Logger(),
    'progress_hooks': [download_hook],
    }
