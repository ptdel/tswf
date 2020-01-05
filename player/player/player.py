import ffmpeg

class Stream:

    process = None
    
    def __init__(self):
        self.process = None
    
    def stream_song(self, song):
        self.process = (
                    ffmpeg
                    .input(song, re=None, vn=None)
                    .output(
                        "rtmp://127.0.0.1:1935/tswf",
                        preset="fast",
                        acodec="aac",
                        audio_bitrate="192k",
                        ar=44100,
                        threads=0,
                        format="flv",
                    )
                    .run_async(pipe_stdout=True)
                )
        return
        
stream = Stream()