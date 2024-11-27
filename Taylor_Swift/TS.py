from pyexpat import features
import pandas
from Albums import Album
from Song import Song
import operator

taylor_file = pandas.read_csv('tay_data/taylor_swift_spotify.csv', encoding='latin1', usecols=['name', 'album', 'release_date', 'track_number', 'id', 'uri','acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'valence', 'popularity', 'duration_ms'])
taylors = taylor_file.to_dict(orient='records')

'''

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
    id = str(song['id'])
    album_name = str(song['album'])
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
    song_obj = None
    if name not in songs.keys():
        song_obj = Song(name, album_name, track, release_date, popularity, danceability, duration, acousticness, energy, valence, tempo,liveness)
        songs[name] = song_obj
    else:
        song_obj = songs[name]
    album_obj = None


'''
Identify the most popular song in each album.   
    if album_name not in albums.keys():
        album_obj = Album(album_name)
        albums[album_name] = album_obj
    else:
        album_obj = albums.get(album_name)
    album_obj.tracks.add(song_obj)
    if album_obj.most_popular_track is None:
        album_obj.most_popular_track = song_obj
    elif song_obj.popularity > album_obj.most_popular_track.popularity:
        album_obj.most_popular_track = song_obj


for album in albums.values():
    print(album.name, "  :: ",  album.most_popular_track.name)
'''

'''
given a favorite song give a list of recommendations 
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
'''
def calculate_similarity(song1, song2):
    features = ['danceability', 'energy', 'acousticness', 'valence', 'tempo']
    similarity = 0
    for feature in features:
        similarity += abs[song1[feature] - song2[feature]]
    return similarity

'''




