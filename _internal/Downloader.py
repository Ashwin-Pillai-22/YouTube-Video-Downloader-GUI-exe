# from pytubefix import YouTube
import os
from pathlib import Path


def check_conflict(title, extension):
    """Check for filename conflicts and generate a unique name."""
    base_name = f"{title}.{extension}"
    new_name = base_name
    counter = 1
    while os.path.exists(os.path.join(Path.home(), 'Downloads', new_name)):
        new_name = f"{title} ({counter}).{extension}"
        counter += 1
    return new_name


def download_audio(link):
    """Download audio-only stream."""
    audio_stream = link.streams.get_audio_only()
    if audio_stream:
        file_name = check_conflict(link.title, "m4a")
        audio_stream.download(output_path=os.path.join(Path.home(), 'Downloads'), filename=file_name)
        return ["Downloaded"]
    else:
        return "Audio stream is not available."


def download_video(link, quality):
    """Download video stream based on quality preference."""
    resolution_map = {
        "Highest Quality" : link.streams.get_highest_resolution(),
        "Lowest Quality" : link.streams.get_lowest_resolution(),
        "720p" : link.streams.get_by_resolution("720p"),
        "480p" : link.streams.get_by_resolution("480p"),
        "360p" : link.streams.get_by_resolution("360p"),
        "240p" : link.streams.get_by_resolution("240p"),
        "144p" : link.streams.get_by_resolution("144p")
    }
    
    stream = resolution_map.get(quality)
    if stream:
        file_name = check_conflict(link.title, "mp4")
        stream.download(output_path=os.path.join(Path.home(), 'Downloads'), filename=file_name)
        return ["Downloaded"]
    else:
        return "Selected resolution is not available."