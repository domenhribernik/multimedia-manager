from lib import *
import os
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

def initialize_project_structure_gui():
    initialize_project_structure()
    messagebox.showinfo("Info", "Project structure initialized")

def show_tooltip(message, time):
    tooltip = tk.Label(root, text=message, bg="yellow")
    tooltip.pack(pady=5)
    root.after(time, tooltip.destroy)

def download_youtube_video_gui():
    url = url_entry.get()
    video_title = get_video_title(url)
    download_youtube_video(url, video_title)
    update_file_lists()
    show_tooltip(f"Downloaded: {video_title}", 3000)

def crop_video_to_aspect_ratio_gui():
    input_file = input_file_entry.get()
    output_file = output_file_entry.get()
    crop_video_to_aspect_ratio(input_file, output_file)
    update_file_lists()
    show_tooltip("Video cropped to aspect ratio", 3000)

def convert_mp4_to_mp3_gui():
    input_file = input_file_entry.get()
    output_file = output_file_entry.get()
    convert_mp4_to_mp3(input_file, output_file)
    update_file_lists()
    show_tooltip("Video converted to MP3", 3000)

def transcribe_audio_gui():
    input_file = input_file_entry.get()
    output_file = output_file_entry.get()
    res = transcribe_audio(input_file, "base")
    show_tooltip("Audio transcribed", 3000)
    messagebox.showinfo("Text", res)

def cut_media_gui():
    start_time = start_time_entry.get()
    end_time = end_time_entry.get()
    input_file = input_file_entry.get()
    output_file = output_file_entry.get()
    cut_media(input_file, output_file, start_time, end_time)
    show_tooltip(f"Media was cut from {start_time} to {end_time}", 3000)
    update_file_lists()

def update_file_lists():
    # Clear existing items in the Treeviews
    videos_tree.delete(*videos_tree.get_children())
    audios_tree.delete(*audios_tree.get_children())

    # Populate the videos list
    video_files = os.listdir("videos") if os.path.exists("videos") else []
    for file in video_files:
        videos_tree.insert("", "end", text=file, image=video_icon)  # Add each file with video icon

    # Populate the audios list
    audio_files = os.listdir("audios") if os.path.exists("audios") else []
    for file in audio_files:
        audios_tree.insert("", "end", text=file, image=audio_icon)

def main():
    global url_entry, start_time_entry, end_time_entry, root, input_file_entry, output_file_entry
    global videos_tree, audios_tree, video_icon, audio_icon
    root = tk.Tk()
    root.title("Media Processing Tool")
    root.geometry("800x700")
    root.config(padx=10, pady=10)

    # Define fonts
    title_font = ("Helvetica", 14, "bold")
    label_font = ("Helvetica", 10)

    # Title
    title_label = tk.Label(root, text="Media Processing Tool", font=title_font)
    title_label.pack(pady=5)

    style = ttk.Style()
    style.configure('Custom.TButton', 
                    foreground='#111111',  # White text color
                    font=('Helvetica', 12, 'bold'),  # Font style
                    borderwidth=2,         # Border width
                    padding=(10, 5))            # Padding

    style.element_create('Custom.TButton', 'from', 'clam')
    style.layout('Custom.TButton', [('Button.button', {'children': [('Button.focus', {'children': [('Button.padding', {'children': [('Button.label', {'sticky': 'nswe'})], 'sticky': 'nswe'})], 'sticky': 'nswe'})], 'sticky': 'nswe'})])
    style.configure('Custom.TButton', background='#333333')


    # Frame for the left-side file lists
    file_list_frame = ttk.Frame(root)
    file_list_frame.pack(side="left", fill="y", padx=10, pady=10)

    # Load icons
    video_icon = Image.open("images/video_icon.png")  
    audio_icon = Image.open("images/audio_icon.png") 

    # Resize icons to fit nicely in the Treeview
    video_icon = video_icon.resize((15, 15), Image.LANCZOS)
    audio_icon = audio_icon.resize((15, 15), Image.LANCZOS)

    # Convert icons for use in Tkinter
    video_icon = ImageTk.PhotoImage(video_icon)
    audio_icon = ImageTk.PhotoImage(audio_icon)

    style = ttk.Style()
    style.configure("Custom.Treeview", indent=0, padding=0)  # Remove extra padding
    style.layout("Custom.Treeview", [("Treeview.treearea", {"sticky": "nswe"})]) 

    # Videos Treeview
    videos_frame = ttk.LabelFrame(file_list_frame, text="Videos", padding=(3, 3))
    videos_frame.pack(fill="both", expand=True)
    videos_tree = ttk.Treeview(videos_frame, show="tree")
    videos_tree.pack(side="left", fill="both", expand=True)
    videos_scrollbar = ttk.Scrollbar(videos_frame, orient="vertical", command=videos_tree.yview)
    videos_scrollbar.pack(side="right", fill="y")
    videos_tree.configure(yscrollcommand=videos_scrollbar.set)

    # Audios Treeview
    audios_frame = ttk.LabelFrame(file_list_frame, text="Audios", padding=(5, 5))
    audios_frame.pack(fill="both", expand=True)
    audios_tree = ttk.Treeview(audios_frame, show="tree")
    audios_tree.pack(side="left", fill="both", expand=True)
    audios_scrollbar = ttk.Scrollbar(audios_frame, orient="vertical", command=audios_tree.yview)
    audios_scrollbar.pack(side="right", fill="y")
    audios_tree.configure(yscrollcommand=audios_scrollbar.set)

    update_file_lists()

    # Right-side main interface frame
    main_frame = ttk.Frame(root)
    main_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    # YouTube Download Section
    download_frame = ttk.LabelFrame(root, text="YouTube Download", padding=(10, 5))
    download_frame.pack(fill="x", pady=5)
    
    tk.Label(download_frame, text="YouTube URL:", font=label_font).grid(row=0, column=0, padx=5, pady=2, sticky="e")
    url_entry = tk.Entry(download_frame, width=40)
    url_entry.grid(row=0, column=1, padx=5, pady=2)
    ttk.Button(download_frame, text="Download Video", style="Custom.TButton", command=download_youtube_video_gui).grid(row=1, column=0, columnspan=2, pady=5)
    
    # Video Crop Section
    crop_frame = ttk.LabelFrame(root, text="Crop Video to Aspect Ratio", padding=(10, 5))
    crop_frame.pack(fill="x", pady=5)

    tk.Label(crop_frame, text="Input File:", font=label_font).grid(row=0, column=0, padx=5, pady=2, sticky="e")
    input_file_entry = tk.Entry(crop_frame, width=30)
    input_file_entry.grid(row=0, column=1, padx=5, pady=2)
    
    tk.Label(crop_frame, text="Output File:", font=label_font).grid(row=1, column=0, padx=5, pady=2, sticky="e")
    output_file_entry = tk.Entry(crop_frame, width=30)
    output_file_entry.grid(row=1, column=1, padx=5, pady=2)
    ttk.Button(crop_frame, text="Crop Video", style="Custom.TButton", command=crop_video_to_aspect_ratio_gui).grid(row=2, column=0, columnspan=2, pady=5)

    # Convert Video to MP3 Section
    convert_frame = ttk.LabelFrame(root, text="Convert MP4 to MP3", padding=(10, 5))
    convert_frame.pack(fill="x", pady=5)

    ttk.Button(convert_frame, text="Convert to MP3", style="Custom.TButton", command=convert_mp4_to_mp3_gui).grid(row=0, column=0, columnspan=2, pady=5)

    # Transcribe Audio Section
    transcribe_frame = ttk.LabelFrame(root, text="Transcribe Audio", padding=(10, 5))
    transcribe_frame.pack(fill="x", pady=5)
    
    ttk.Button(transcribe_frame, text="Transcribe Audio", style="Custom.TButton", command=transcribe_audio_gui).grid(row=0, column=0, columnspan=2, pady=5)

    # Cut Media Section
    cut_frame = ttk.LabelFrame(root, text="Cut Media", padding=(10, 5))
    cut_frame.pack(fill="x", pady=5)
    
    tk.Label(cut_frame, text="Start Time (HH:MM:SS):", font=label_font).grid(row=0, column=0, padx=5, pady=2, sticky="e")
    start_time_entry = tk.Entry(cut_frame, width=15)
    start_time_entry.grid(row=0, column=1, padx=5, pady=2)
    
    tk.Label(cut_frame, text="End Time (HH:MM:SS):", font=label_font).grid(row=1, column=0, padx=5, pady=2, sticky="e")
    end_time_entry = tk.Entry(cut_frame, width=15)
    end_time_entry.grid(row=1, column=1, padx=5, pady=2)
    ttk.Button(cut_frame, text="Cut Media", style="Custom.TButton", command=cut_media_gui).grid(row=2, column=0, columnspan=2, pady=5)
    ttk.Button(root, text="Initialize Project Structure", style="Custom.TButton", command=initialize_project_structure_gui).pack(pady=10)

    root.mainloop()

if __name__ == '__main__':
    main()
