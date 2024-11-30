from pyexpat import features
import pandas
from Albums import Album
from Song import Song
import operator

taylor_file = pandas.read_csv('tay_data/taylor_swift_spotify.csv', encoding='latin1', usecols=['name', 'album', 'release_date', 'track_number', 'id', 'uri','acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'valence', 'popularity', 'duration_ms'])
taylors = taylor_file.to_dict(orient='records')

'''
find trend between popularity and danceabliltiy
'''
songs = {}
albums = {}
list1 = []
danceability_list = []
popularity_list = []

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
    if album_name not in albums.keys():
        album_obj = Album(album_name)
        albums[album_name] = album_obj
    else:
        album_obj = albums.get(album_name)
    album_obj.tracks.add(song_obj)
for album in albums.values():
    sum = 0
    for track in album.tracks:
        sum =+ track.danceability
    album.average_danceability = sum/len(album.tracks)
for album in albums.values():
    sum = 0
    for track in album.tracks:
        sum += track.popularity
    album.average_popularity = sum/len(album.tracks)

for album in albums.values():
    popularity_list.append(album)
    danceability_list.append(album)

def sortByDanceability(album):
    return album.average_danceability

def sortByPopularity(album):
    return album.average_popularity

danceability_list.sort(key=sortByDanceability)
popularity_list.sort(key=sortByPopularity)
print(danceability_list)
print(popularity_list)


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
Find the album with highest average danceability across all the albums
highest_average_danceability = 0
highest_average_danceability_album = ''
for album in albums.values():
    sum = 0
    for track in album.tracks:
        sum =+ track.danceability
    album.average_danceability = sum/len(album.tracks)
    if highest_average_danceability < album.average_danceability:
        highest_average_danceability = album.average_danceability
        highest_average_danceability_album = album.name


print(highest_average_danceability_album, "  :: ",  highest_average_danceability)
'''
'''
Find the longest song across all albums
   
    if album_obj.longest_song is None:
        album_obj.longest_song = song_obj
    elif song_obj.duration > album_obj.longest_song.duration:
        album_obj.longest_song = song_obj

for album in albums.values():
    print(album.name, "  :: ", album.longest_song.name)
'''
'''
Identify the most popular song in each album.   
    if album_obj.most_popular_track is None:
        album_obj.most_popular_track = song_obj
    elif song_obj.popularity > album_obj.most_popular_track.popularity:
        album_obj.most_popular_track = song_obj


for album in albums.values():
    print(album.name, "  :: ",  album.most_popular_track.name)
'''


'''
def calculate_similarity(song1, song2):
    features = ['danceability', 'energy', 'acousticness', 'valence', 'tempo']
    similarity = 0
    for feature in features:
        similarity += abs[song1[feature] - song2[feature]]
    return similarity

'''




