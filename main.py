from lib import *

def main():
    # initialize_project_structure()
    # download_youtube_video("https://www.youtube.com/watch?v=fHI8X4OXluQ", "music")
    # crop_video_to_aspect_ratio("music.mp4", "cropped.mp4")
    # convert_mp4_to_mp3("music.mp4", "audio.mp3")
    #transcribe_audio("audio.mp3", "base")
    cut_media("audio.mp3", "cut.mp3", "00:30", "02:00")

if __name__ == '__main__':
    main()