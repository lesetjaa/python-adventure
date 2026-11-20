import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic
import json

# 2023-11-18
date = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://appbrewery.github.io/bakeboard-hot-100/{date}/"


response = requests.get(url=URL)
response.raise_for_status()
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

titles = [title.get_text() for title in soup.find_all(
    name="h3", class_="chart-entry__title")]

yt = YTMusic("browser.json")

playlists = yt.get_library_playlists()
print(f"Found {len(playlists)} playlists in your library.")

playlist_titles = [title["title"] for title in playlists]

new_playlist = f"{date} Bakeboard 100"

if new_playlist not in playlist_titles:
    playlistId = yt.create_playlist(
        title=new_playlist, description="Created using ytmusicapi")

    for song_title in titles:
        try:
            search_results = yt.search(query=song_title, filter="songs")
        except Exception as e:
            print(f"Skipped: {song_title} | Reason: {e}")
        else:
            if isinstance(playlistId, str):
                yt.add_playlist_items(
                    playlistId, [search_results[0]["videoId"]])
                print(f"Added: {song_title}")
            else:
                print("Failed to create playlist. Response:", playlistId)
else:
    print(f"Playlist: {new_playlist} already available")
