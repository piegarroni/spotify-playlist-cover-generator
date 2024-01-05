import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from collections import Counter
from dotenv import load_dotenv
import os 
from spotipy.exceptions import SpotifyException



env_path = os.path.join(os.getcwd(), '.env')
load_dotenv(env_path)
CLIENT = os.getenv('SPOTIFY_CLIENT')
SECRET = os.getenv('SPOTIFY_SECRET')

class SpotifyPlaylistAnalyzer:
    def __init__(self, playlist_id):
        self.sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=CLIENT, client_secret=SECRET))
        self.playlist_id = playlist_id

    def get_playlist_details(self):
        """
        Method to retrieve the playlist's name and description
        """
        playlist = self.sp.playlist(self.playlist_id)
        return playlist['name'], playlist['description']

    def get_playlist_tracks(self):
        """
        Method to retrieve the tracks in the playlist (name, artist, id, album...)
        """
        tracks = []
        results = self.sp.playlist_tracks(self.playlist_id)
        while results:
            tracks.extend([{'track_name': track['track']['name'], 'track_id': track['track']['id'], 
                            'artist_id': track['track']['artists'][0]['id'], 
                            'artist_name': track['track']['artists'][0]['name'],  
                            'album_name': track['track']['album']['name']} for track in results['items']])
            results = self.sp.next(results)
        return tracks

    def get_song_features(self, song_id):
        """
        Method to get the features of a single song
        """
        try:

            audio_features = self.sp.audio_features(song_id)
            return audio_features[0]['energy'], audio_features[0]['danceability'], audio_features[0]['speechiness'], audio_features[0]['acousticness'], audio_features[0]['valence']

        except SpotifyException as e:
            if e.http_status == 429:
                retry_after = int(e.headers.get('Retry-After', 0))
                print(f"Rate limit reached. Retrying after {retry_after} seconds.")
            else:
                raise

        #audio_features = self.sp.audio_features(song_id)


    def get_song_genre(self, artist_id):
        """
        Method to get the genre of the artists' of every song
        """
        artist = self.sp.artist(artist_id)
        return artist['genres']

    def retrieve_data(self):
        """
        Method to merge all the previous methods and return playlist_name, description and song's data
        """
        playlist_name, playlist_description = self.get_playlist_details()

        playlist_tracks = self.get_playlist_tracks()
        data = pd.DataFrame(playlist_tracks)

        data[['energy', 'danceability', 'speechiness', 'acousticness', 'valence']] = data['track_id'].apply(self.get_song_features).apply(pd.Series) #self.get_song_features([i for i in data['track_id']])#

        # Get song genres
        data['genres'] = data['artist_id'].apply(self.get_song_genre)

        #data.to_csv(f'playlists_data/{playlist_name.replace(" ", "-")}.csv')
        return playlist_name, playlist_description, data





"""
# Get playlist details
playlist_name, playlist_description = analyzer.get_playlist_details(playlist_id)
print("Playlist Name:", playlist_name)
print("Playlist Description:", playlist_description)

# Get playlist tracks
playlist_tracks = analyzer.get_playlist_tracks(playlist_id)
data = pd.DataFrame(playlist_tracks)
data.name = playlist_name

# Get song features
data[['energy', 'danceability', 'speechiness', 'acousticness', 'valence']] = data['track_id'].apply(analyzer.get_song_features).apply(pd.Series)

# Get song genres
data['genres'] = data['artist_id'].apply(analyzer.get_song_genre)

# Save to CSV
data.to_csv(f'playlists_data/{playlist_name}.csv')
"""

