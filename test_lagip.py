import pytest
from unittest import mock
import os
from lagip import download_video, clear_url
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

# Test clear_url function
def test_clear_url(url_entry):
    url_entry.insert(0, "https://www.youtube.com/watch?v=somevideoid")
    clear_url(url_entry)
    assert url_entry.get() == ""

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
