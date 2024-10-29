import pytest
from unittest import mock
import os
from lagip import download_video, download_audio, clear_url, extract_audio
import tkinter as tk

# Helper fixture for setting up the tkinter entry widget
@pytest.fixture
def url_entry():
    return tk.Entry()

# Mock function to check download_video
@mock.patch('yt_dlp.YoutubeDL')
def test_download_video(mock_yt_dlp, url_entry):
    status_label = tk.Label()
    mock_yt_dlp.return_value.download.return_value = None  # Mock the download method

    # Call the download function
    download_video("https://www.youtube.com/watch?v=somevideoid", status_label)

    # Check if the status label was updated correctly
    assert "successful" in status_label.cget("text").lower()

# Mock function to check download_audio
@mock.patch('yt_dlp.YoutubeDL')
@mock.patch('moviepy.editor.AudioFileClip')
def test_download_audio(mock_audio_clip, mock_yt_dlp, url_entry):
    status_label = tk.Label()
    mock_yt_dlp.return_value.extract_info.return_value = {'_filename': 'downloads/test_video.mp4'}
    
    # Mock the behavior of AudioFileClip to simulate audio extraction
    mock_audio_clip.return_value.__enter__.return_value.write_audiofile = mock.Mock()

    # Call the download audio function
    download_audio("https://www.youtube.com/watch?v=somevideoid", status_label)

    # Check if the status label was updated correctly
    assert "successful" in status_label.cget("text").lower()

    # Check if the audio file was created (expect 'downloads/test_video.mp3')
    assert os.path.exists("downloads/test_video.mp3")
    os.remove("downloads/test_video.mp3")  # Cleanup

# Test clear_url function
def test_clear_url(url_entry):
    url_entry.insert(0, "https://www.youtube.com/watch?v=somevideoid")
    clear_url(url_entry)
    assert url_entry.get() == ""

# Mock function to test extract_audio
@mock.patch('moviepy.editor.AudioFileClip')
def test_extract_audio(mock_audio_clip):
    video_path = "downloads/test_video.mp4"
    audio_path = "downloads/test_video.mp3"
    open(video_path, 'a').close()  # Create an empty video file for testing

    # Mock the behavior of AudioFileClip to simulate audio extraction
    mock_audio_clip.return_value.__enter__.return_value.write_audiofile = mock.Mock()

    # Call the extract_audio function
    extract_audio(video_path)

    # Check if the audio file was created and video file deleted
    assert os.path.exists(audio_path)
    assert not os.path.exists(video_path)

    os.remove(audio_path)  # Cleanup after test

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
