import ffmpeg


def stream_song(song):
    return (
        ffmpeg.input(song, re=None)
        .output(
            "rtmp://127.0.0.1:1935/tswf",
            preset="fast",
            acodec="aac",
            audio_bitrate="192k",
            ar=44100,
            threads=0,
            format="flv",
        )
        .run()
    )
