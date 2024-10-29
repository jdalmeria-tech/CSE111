import tkinter as tk
from tkinter import messagebox
from tkinter import font
import yt_dlp
import os
import moviepy.editor as mp

def main():
    """
    Initializes the main Tkinter window for the Lagip application.
    Parameters: None
    Returns: None
    """
    root = tk.Tk()
    root.title("Lagip - YouTube Video Downloader")
    setup_gui(root)
    root.mainloop()

def setup_gui(root):
    """
    Sets up the GUI components for the Lagip application.
    Parameters:
        root (tk.Tk): The root window of the Tkinter application.
    Returns: None
    """
    tk.Label(root, text="YouTube URL:").grid(row=0, column=0, padx=10, pady=10)
    url_entry = tk.Entry(root, width=50)
    url_entry.grid(row=0, column=1, padx=10, pady=10)

    bold_font = font.Font(weight="bold")

    # Download Video button
    download_video_button = tk.Button(root, text="Download Video", command=lambda: download_video(url_entry.get(), status_label), bg="green", fg="white", font=bold_font)
    download_video_button.grid(row=1, column=1, padx=10, pady=10)

    # Download Audio button
    download_audio_button = tk.Button(root, text="Download Audio", command=lambda: download_audio(url_entry.get(), status_label), bg="blue", fg="white", font=bold_font)
    download_audio_button.grid(row=2, column=1, padx=10, pady=10)

    # Clear button
    clear_button = tk.Button(root, text="Clear", command=lambda: clear_url(url_entry), bg="red", fg="white", font=bold_font)
    clear_button.grid(row=1, column=0, padx=10, pady=10)

    # Status label
    global status_label
    status_label = tk.Label(root, text="", fg="green")
    status_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

def download_video(url, status_label):
    """
    Downloads a YouTube video from the provided URL.
    Parameters:
        url (str): The URL of the YouTube video to download.
        status_label (tk.Label): The label to update with status messages.
    Returns: None
    """
    try:
        status_label.config(text="Downloading video...", fg="blue")
        status_label.update_idletasks()

        if not url.startswith("https://www.youtube.com/"):
            raise ValueError("Invalid YouTube URL")

        ydl_opts = {
            'format': 'best',
            'outtmpl': 'downloads/%(title)s.%(ext)s'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        status_label.config(text="Video download successful!", fg="green")
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        status_label.config(text="Download failed", fg="red")
        messagebox.showerror("Error", f"Failed to download video: {e}")
        print(f"Error: {e}")

def download_audio(url, status_label):
    """
    Downloads a YouTube video as audio and converts it to MP3.
    Parameters:
        url (str): The URL of the YouTube video to download as audio.
        status_label (tk.Label): The label to update with status messages.
    Returns: None
    """
    try:
        status_label.config(text="Downloading and converting to audio...", fg="blue")
        status_label.update_idletasks()

        if not url.startswith("https://www.youtube.com/"):
            raise ValueError("Invalid YouTube URL")

        ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': 'downloads/%(title)s.%(ext)s'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            video_info = ydl.extract_info(url, download=True)
            video_file = ydl.prepare_filename(video_info)
            extract_audio(video_file)

        status_label.config(text="Audio download successful!", fg="green")
        messagebox.showinfo("Success", "Audio downloaded and converted to MP3 successfully!")
    except Exception as e:
        status_label.config(text="Download failed", fg="red")
        messagebox.showerror("Error", f"Failed to download audio: {e}")
        print(f"Error: {e}")

def clear_url(entry):
    """
    Clears the contents of the URL entry field.
    Parameters:
        entry (tk.Entry): The URL entry field to clear.
    Returns: None
    """
    entry.delete(0, tk.END)

def extract_audio(video_path, audio_format='mp3'):
    """
    Extracts audio from a downloaded video file and saves it as an MP3.
    Parameters:
        video_path (str): The path to the downloaded video file.
        audio_format (str): The desired audio format (default is 'mp3').
    Returns: None
    """
    try:
        audio_path = f"{os.path.splitext(video_path)[0]}.{audio_format}"
        # Only load audio, not the whole video
        with mp.AudioFileClip(video_path) as audio:
            audio.write_audiofile(audio_path)
        messagebox.showinfo("Success", f"Audio extracted successfully to {audio_path}!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to extract audio: {e}")

if __name__ == "__main__":
    main()




