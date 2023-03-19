import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup
from pprint import pprint
# # ==================== Spotify API =======================
SPOTIPY_CLIENT_ID = "452fdfbbb2b0435caf8b530c686a3d74"
SPOTIPY_CLIENT_SECRET = "75710eac3a9b425da713f693a4ce99cd"
URL_REDIRECT = "https://example.com/"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=URL_REDIRECT,
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)
# =============== Top 100 Billboard Web scraping =========
date = "2016-08-12"
# date = input("what year you would like to travel to in YYY-MM-DD format: ")


Billboard_Hot100_URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url=Billboard_Hot100_URL)
Billboard_Hot100_web_page = response.text
soup = BeautifulSoup(Billboard_Hot100_web_page, "html.parser")
titles = soup.select(selector="li #title-of-a-story")
song_titles = [title.getText().strip() for title in titles]
artists = soup.select(selector="li .a-truncate-ellipsis-2line")
song_artist = [artist.getText().strip() for artist in artists]
song_uris = []
year = date.split("-")[0]
# print(song_artist)

for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # pprint(result["tracks"])
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)
link_to_playlist = (playlist["external_urls"]["spotify"])
print(f"this is your link for {year} top 100 : {link_to_playlist}")
# pprint(song_uris)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)