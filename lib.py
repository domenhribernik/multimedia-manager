import yt_dlp
from moviepy.editor import VideoFileClip
import subprocess
import os
import whisper
from datetime import timedelta

def initialize_project_structure():
    directories = ["audios", "videos"]
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Directory '{directory}' created.")
        else:
            print(f"Directory '{directory}' already exists.")

def download_youtube_video(url, output_filename=None):
    output_filename = os.path.join("videos", output_filename) if output_filename else None
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

def get_video_title(url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'force_generic_extractor': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_title = info_dict.get('title', None)
            return video_title
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def crop_video_to_aspect_ratio(input_video, output_video):
    video = VideoFileClip(input_video)

    input_video = os.path.join("videos", input_video)
    output_video = os.path.join("videos", output_video)
    
    # Define the desired crop parameters
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
    if not output_audio.lower().endswith('.mp3'):
        output_audio += '.mp3'

    input_video = os.path.join("videos", input_video)
    output_audio = os.path.join("audios", output_audio)

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

def transcribe_audio(input_audio, model_size="base"):
    input_audio = os.path.join("audios", input_audio)
    
    model = whisper.load_model(model_size)  # Load the Whisper model
    result = model.transcribe(input_audio)  # Transcribe the audio file
    print(result["text"])

    return result["text"]

def generate_subtitles(song_name):
    model = whisper.load_model('base')  # Load the Whisper model
    result = model.transcribe(song_name, word_timestamps=True)  # Transcribe the audio file
    segments = result["segments"]

    for i, segment in enumerate(segments, start=1):
        start_time = str(timedelta(seconds=segment['start']))
        end_time = str(timedelta(seconds=segment['end']))
        text = segment['text']
        print(f"Segment {i}:")
        print(f"  Start Time: {start_time}")
        print(f"  End Time:   {end_time}")
        print(f"  Text:       {text}")
        print("-" * 40)

        for word_info in segment.get('words', []):  # 'words' contains word-level timestamps
            word_text = word_info.get('text') or word_info.get('word')  # Handle cases for 'text' or 'word'
            word_start = str(timedelta(seconds=word_info['start'])) if 'start' in word_info else "N/A"
            word_end = str(timedelta(seconds=word_info['end'])) if 'end' in word_info else "N/A"
            
            # Print word details with start and end times
            if word_text:
                print(f"    {word_text}: {word_start} --> {word_end}")

        print("-" * 40)

def cut_media(input_file, output_file, start_time, end_time):
    input_path = os.path.join("videos" if input_file.endswith(('.mp4', '.mkv')) else "audios", input_file)
    output_path = os.path.join("videos" if output_file.endswith(('.mp4', '.mkv')) else "audios", output_file)

    command = [
        'ffmpeg',
        '-i', input_path,  # Input file
        '-ss', start_time,  # Start time in "mm:ss" format
        '-to', end_time,  # End time in "mm:ss" format
        '-c', 'copy',  # Copy codec (no re-encoding)
        output_path  # Output file
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Media successfully cut and saved as {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error while cutting media: {e}")