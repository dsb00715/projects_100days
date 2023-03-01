from os import environ
import requests
from bs4 import BeautifulSoup
from spotipy import Spotify
import spotipy.util as util

URL = "https://www.billboard.com/charts/hot-100/"
SPOTIFY_CLIENT_ID = environ.get("SPOTIPY_CLIENT_ID")
SPOTIFY_SECRET_KEY = environ.get("SPOTIPY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = environ.get("SPOTIPY_REDIRECT_URI")
TOKEN = util.prompt_for_user_token(
    scope="playlist-modify-private",
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_SECRET_KEY,
    redirect_uri=SPOTIFY_REDIRECT_URI,
)


def get_songs(year):
    """_summary_

    Args:
        year (str): it should be year in form of YYYY-MM-DD

    Returns:
        list: list of songs from Billboard Hot 100 website via Scraping
    """
    response = requests.get(URL + year)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")
    song_tags = soup.find_all(
        name="ul",
        class_="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max",
    )
    list_of_songs = [
        f"{(tag.li.h3.text).strip()}" for tag in song_tags
    ]  # list of songs
    # artist_list = [f"{(tag.li.span.text).strip()}" for tag in song_tags]  # list of artist
    return list_of_songs


def get_uri_songs(song_list, spotify_object, year):
    """_summary_

    Args:
        song_list (list): list of songs
        spotify_object (spotipy): Spotify API Object
        year (_type_): year given by user.

    Returns:
        list: list of uri
    """
    uri_song = []
    for index in range(len(song_list) - 1):
        result = spotify_object.search(
            q=f"track:{song_list[index]} year:{year.split('-')[0]}",
            type="track",
        )  #  artist:{artist_list[index]}
        try:
            uri = result["tracks"]["items"][0]["uri"]
            uri_song.append(uri)
        except IndexError:
            print(f"{song_list[index]} doesn't exist in Spotify. Skipped.")
    return uri_song


def main(token):
    # get year from user
    year = input(
        "Which year do you want to travel to? Please type the date in this format YYYY-MM-DD: "
    )
    song_list = get_songs(year)

    sp = Spotify(auth=token)  # Create Spotify Object
    sp.trace = True
    # get user_id from spotify API
    user_id = sp.current_user()["id"]
    uri_song = get_uri_songs(song_list, sp, year)

    playlist = sp.user_playlist_create(
        user_id,
        name=f"{year} Billboard 100",
        public=False,
        description="top 100 songs as per Billboard",
    )
    add_songs_to_playlist = sp.playlist_add_items(
        playlist_id=playlist["id"], items=uri_song
    )
    print(add_songs_to_playlist)


if __name__ == "__main__":
    main(token=TOKEN)
