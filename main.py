import yt_dlp
from moviepy.editor import VideoFileClip
import subprocess
import os
import whisper

def download_youtube_video(url, output_filename=None):
    ydl_opts = {
        'format': 'bestvideo+bestaudio[ext=m4a]/mp4',  # Best quality video and audio with mp4 format
        'outtmpl': f"{output_filename}.mp4" if output_filename else "%(title)s.mp4",  # Output file template
        'merge_output_format': 'mp4'  # Ensure final file is in .mp4 format
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.download([url])
            print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
    output_file = output_filename + '.mp4' if output_filename else result[0]['title'] + '.mp4'
    return output_file


def crop_video(input_video, output_video):
    # Load the video file
    video = VideoFileClip(input_video)
    
    # Define the desired crop parameters (9:16 aspect ratio)
    aspect_ratio = 9 / 16
    video_width, video_height = video.size
    
    # Calculate crop dimensions
    new_width = video_height * aspect_ratio
    x_center = video_width / 2
    x1 = x_center - (new_width / 2)
    x2 = x_center + (new_width / 2)
    
    cropped_video = video.crop(x1=x1, x2=x2)
    cropped_video.write_videofile(output_video, codec='libx264', audio_codec='aac')
    print(f"Video successfully cropped and saved as {output_video}")


def convert_mp4_to_mp3(input_video, output_audio):
    # Ensure the output file name has the .mp3 extension
    if not output_audio.lower().endswith('.mp3'):
        output_audio += '.mp3'

    # Build the ffmpeg command to extract audio from the video and convert to mp3
    command = [
        'ffmpeg',
        '-i', input_video,  # Input video file
        '-vn',  # No video (only audio)
        '-acodec', 'libmp3lame',  # Use the MP3 codec
        '-ar', '44100',  # Audio sample rate
        '-ac', '2',  # Number of audio channels (stereo)
        '-ab', '192k',  # Audio bitrate
        output_audio  # Output audio file (MP3)
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Audio successfully extracted and saved as {output_audio}")
    except subprocess.CalledProcessError as e:
        print(f"Error while converting video to audio: {e}")


# download_youtube_video("https://www.youtube.com/watch?v=fHI8X4OXluQ", "music")
#crop_video("music.mp4", "cropped.mp4")
convert_mp4_to_mp3("music.mp4", "audio.mp3")


# model = whisper.load_model("base") # tiny, base, small, medium, large
# result = model.transcribe("your_audio_file.mp3")
# print(result["text"])
