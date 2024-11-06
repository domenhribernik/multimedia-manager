# Multimedia Manager
## Project Overview
This project provides a comprehensive suite of tools for managing multimedia files. It includes features such as downloading YouTube videos as MP4 files, converting MP4 videos to MP3 audio files, transcribing text from audio, and so on. It is a versatile tool for anyone needing to manage multimedia files efficiently.

## Installation Instructions

### Python Dependencies

To install the necessary Python dependencies, run the following command:

```bash
pip install -r requirements.txt
```

Make sure you have a `requirements.txt` file in your project directory with all the required packages listed.

### FFmpeg Installation

To install FFmpeg, follow these steps:

1. Go to the [FFmpeg download page](https://ffmpeg.org/download.html).
2. Choose the appropriate version for your operating system.
3. Download the executable files.
4. Follow the installation instructions provided on the website.

After installation, ensure that FFmpeg is added to your system's PATH so that it can be accessed from the command line.

You can verify the installation by running:

```bash
ffmpeg -version
```

This should display the installed version of FFmpeg.

## Functionality Documentation

### `initialize_project_structure()`

This function sets up the initial project structure by creating the necessary folders for storing audio and video files. It ensures that the `audios` and `videos` directories are created only once, preventing any redundant directory creation during subsequent runs.

**Example:**
```python
initialize_project_structure()
```

### `download_youtube_video(url, output_filename=None)`

This function downloads a YouTube video to an MP4 file.

**Parameters:**
- `url` (str): The URL of the YouTube video to download.
- `output_filename` (str, optional): The name of the output file. If not provided, the video's title will be used.

**Returns:**
- `str`: The path to the downloaded video file.

**Example:**
```python
download_youtube_video('https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'my_video')
```

### `convert_mp4_to_mp3(input_video, output_audio)`

This function converts an MP4 video file to an MP3 audio file.

**Parameters:**
- `input_video` (str): The path to the input video file.
- `output_audio` (str): The desired name for the output audio file.

**Example:**
```python
convert_mp4_to_mp3('my_video.mp4', 'my_audio')
```

### `transcribe_audio(input_audio, model_size="base")`

This function transcribes text from an audio file using the Whisper model.

**Parameters:**
- `input_audio` (str): The name of the input audio file located in the `audios` directory.
- `model_size` (str, optional): The size of the model to use. Options are `"tiny"`, `"base"`, `"small"`, `"medium"`, `"large"`. Defaults to `"base"`.

**Returns:**
- `str`: The transcribed text from the audio file.

**Example:**
```python
transcribe_audio('my_audio.mp3', 'large')
```

### `cut_media(input_file, output_file, start_time, end_time)`

This function cuts a segment from a media file (either video or audio) based on the specified start and end times.

**Parameters:**
- `input_file` (str): The name of the input media file located in the `videos` or `audios` directory.
- `output_file` (str): The desired name for the output media file.
- `start_time` (str): The start time of the segment to cut in "mm:ss" format.
- `end_time` (str): The end time of the segment to cut in "mm:ss" format.

**Example:**
```python
cut_media('input_video.mp4', 'output_video.mp4', '00:30', '01:00')
```

### `crop_video_to_aspect_ratio(input_video, output_video)`

This function crops a video to a 9:16 (standard phone) aspect ratio.

**Parameters:**
- `input_video` (str): The name of the input video file located in the `videos` directory.
- `output_video` (str): The desired name for the output cropped video file.

**Example:**
```python
crop_video('input_video.mp4', 'output_video.mp4')
```