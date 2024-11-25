from pyexpat import features
import pandas
from Albums import Album
from Song import Song
import operator

taylor_file = pandas.read_csv('tay_data/taylor_swift_spotify.csv', encoding='latin1', usecols=['name', 'album', 'release_date', 'track_number', 'id', 'uri','acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'valence', 'popularity', 'duration_ms'])
taylors = taylor_file.to_dict(orient='records')

'''
Identify the most popular song in each album.
Find the longest song across all albums
Find the album with highest average danceability across all her albums
find trend between popularity and danceabliltiy
given a favorite song give a list of recommendations 
'''
songs = {}
albums = {}
list1 = []

class Similarity:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        return repr((self.name, self.score))


def calculate_similarity(song1, song2):
    similarity = 0
    similarity += abs(song1.danceability - song2.danceability)
    similarity += abs(song1.energy - song2.energy)
    similarity += abs(song1.acousticness - song2.acousticness)
    similarity += abs(song1.valence - song2.valence)
    similarity += abs(song1.tempo - song2.tempo)
    return similarity

for song in taylors:
    name = str(song['name'])
    album = str(song['album'])
    popularity = int(song['popularity'])
    track = int(song['track_number'])
    release_date = str(song['release_date'])
    danceability = float(song['danceability'])
    duration = int(song['duration_ms'])
    acousticness = float(song['acousticness'])
    energy = float(song['energy'])
    valence = float(song['valence'])
    tempo = float(song['tempo'])
    liveness = float(song['liveness'])
    if name not in songs.keys():
        song_obj = Song(name, album, popularity, track, release_date, danceability, duration, acousticness, energy, valence, tempo,liveness)
        songs[name] = song_obj
input = songs.get('Paper Rings')
for song in songs.values():
    score = calculate_similarity(input, song)
    name = song.name
    similarity_obj = Similarity(name, score)
    list1.append(similarity_obj)

def getScore(similarity):
    return similarity.score

list1.sort(key=getScore)
print(list1)








'''
for album in taylors:
    album = str(album['album'])
    name = str(album['name'])
    track = int(album['track_number'])
    release_date = int(album['release_date'])
    if album not in albums.keys():
        album_obj = Album(name, track, release_date)
        album[album] = album_obj
'''
'''
def calculate_similarity(song1, song2):
    features = ['danceability', 'energy', 'acousticness', 'valence', 'tempo']
    similarity = 0
    for feature in features:
        similarity += abs[song1[feature] - song2[feature]]
    return similarity

'''




