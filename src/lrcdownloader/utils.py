import os
from mutagen.easyid3 import EasyID3

def search_all_music_files(directory):
    """Search all music files in the directory."""
    music_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.mp3', '.flac', '.wav', '.m4a')):
                music_files.append(os.path.join(root, file))
    return music_files

def get_tags(file):
    """Get tags from the music file."""
    return EasyID3(file).items()

def main():
    music_files = search_all_music_files('path/to/music/directory')
    for file in music_files:
        tags = get_tags(file)
        for tag in tags:
            print(tag)
        print("----------")
    print(music_files)