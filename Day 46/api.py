import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyAPI:
    def __init__(self):
        self.id = "6fba3c5dd47743a6ab40e1385ffb2dcd"
        self.secret = '3243a07ff72c41d1bb1ec505298a0050'
        self.authorization()
        self.get_user_id()

    def authorization(self):
        scope = 'playlist-modify-private'
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.id, client_secret=self.secret, scope=scope, redirect_uri='http://localhost:8888/callback'))


    def get_user_id(self):
        self.userid = self.sp.current_user()['id']
    
    def all_playlists(self):
        playlists = self.sp.user_playlists(self.userid)
        while playlists:
            for i, playlist in enumerate(playlists['items']):
                print("%4d %s %s" % (i + 1, playlist['id'],  playlist['name']))
            if playlists['next']:
                playlists = self.sp.next(playlists)
            else:
                playlists = None

    def playlist_create(self, title):
        playlist = self.sp.user_playlist_create(user=self.userid, name=title, public=False)
        return(playlist['id'])
    
    def playlist_delete(self, id):
        self.sp.user_playlist_unfollow(self.userid, id)
        print("successfully removed")

    def track_add(self, playlist_id, track):
        self.sp.user_playlist_add_tracks(self.userid, playlist_id, track)

    def search(self, track_name):
        results = self.sp.search(q=track_name, type='track')
        if results['tracks']['items']:
            return(results['tracks']['items'][0]['uri'])
        else:
            return 'track not found'
