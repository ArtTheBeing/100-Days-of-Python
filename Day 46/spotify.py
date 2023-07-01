from api import SpotifyAPI
from scrapper import  Scraper

spotify = SpotifyAPI()
song_scraper = Scraper()
song_scraper.scrape()


#spotify.results()
p_id = spotify.playlist_create('TimeMachine')
songs = song_scraper.songs

for song in songs:
    try:
        song_id = spotify.search(song)
        print(song_id)
        spotify.sp.user_playlist_add_tracks(spotify.userid, p_id, [song_id])
    except:
        print('Song not found')
