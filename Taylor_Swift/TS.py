from pyexpat import features

import numpy as np
import pandas
from datetime import datetime
from numpy.ma.core import append

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
    def __init__(self, name, score, popularity):
        self.name = name
        self.score = score
        self.popularity = popularity
    def __repr__(self):
        return repr((self.name, self.score, self.popularity))


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
    sum1 = 0
    for track in album.tracks:
        sum1 =+ track.danceability
    album.average_danceability = sum1/len(album.tracks)
for album in albums.values():
    sum1 = 0
    for track in album.tracks:
        sum1 += track.popularity
    album.average_popularity = sum1/len(album.tracks)

for album in albums.values():
    popularity_list.append(album)
    danceability_list.append(album)

danceability_list1 = np.array([])
tempo_list = np.array([])
popularity_list1 = np.array([])
for song in songs.values():
    danceability_list1 = np.append(danceability_list1, [song.danceability])
    tempo_list = np.append(tempo_list,[song.tempo])
    popularity_list1 = np.append(popularity_list1,[song.popularity])


def pearsonCorrelation(x,y):
    if len(x) == len(y):
        sum_xy = sum((x-x.mean())*(y-y.mean()))
        sum_x_squared = sum((x-x.mean())**2)
        sum_y_squared = sum((y - y.mean()) ** 2)
        correlation = sum_xy / np.sqrt(sum_x_squared * sum_y_squared)
    return correlation

print(pearsonCorrelation(tempo_list,popularity_list1))







'''
# longest song by year
longest_song_by_year = {}

def parseYear(dateAsString):
    dt = datetime.strptime(dateAsString, '%Y-%m-%d')
    return dt.year

for song in songs.values():
    date = song.release_date
    release_year = parseYear(date)
    if release_year in longest_song_by_year.keys():
        x = longest_song_by_year.get(release_year)
        if x.duration < song.duration:
            longest_song_by_year[release_year] = song
    if release_year not in longest_song_by_year.keys():
        longest_song_by_year[release_year] = song
for duration in longest_song_by_year.keys():
    song = longest_song_by_year.get(duration)
    print(str(duration) + " : " + str(song.name))
'''
'''
#most popular song by year
most_popular_song_by_year = {}

def parseYear(dateAsString):
    dt = datetime.strptime(dateAsString, '%Y-%m-%d')
    return dt.year

for song in songs.values():
    date = song.release_date
    release_year = parseYear(date)
    if release_year in most_popular_song_by_year.keys():
        x = most_popular_song_by_year.get(release_year)
        if x.popularity < song.popularity:
            most_popular_song_by_year[release_year] = song
    if release_year not in most_popular_song_by_year.keys():
        most_popular_song_by_year[release_year] = song

for release_year in most_popular_song_by_year.keys():
    song = most_popular_song_by_year.get(release_year)
    print(str(release_year) + " : " + str(song.name))
'''
'''
#find tempo difference between summer and winter songs
def parseMonth(dateAsString):
    dt = datetime.strptime(dateAsString, '%Y-%m-%d')
    return dt.month

def findAverageTempo(songs):
    sum_of_tempo = 0
    average_tempo = 0
    for song in songs:
        tempo = song.tempo
        sum_of_tempo += tempo
    average_tempo = sum_of_tempo/len(songs)
    return average_tempo

summer_songs = []
winter_songs = []

for song in songs.values():
    date = song.release_date
    release_month = parseMonth(date)
    if release_month >= 4 and release_month <= 9:
        summer_songs.append(song_obj)
    else:
        winter_songs.append(song_obj)
summer_average_tempo = findAverageTempo(summer_songs)
winter_average_tempo = findAverageTempo(winter_songs)

print(summer_average_tempo)
print(winter_average_tempo)
'''
'''
average danceability and average popularity sorted
def sortByDanceability(album):
    return album.average_danceability

def sortByPopularity(album):
    return album.average_popularity

#danceability_list.sort(key=sortByDanceability)
sorted_popularity_list = sorted(popularity_list, key=sortByPopularity, reverse=True)

sorted_list = sorted(danceability_list, key=operator.attrgetter('average_danceability', 'average_popularity'), reverse=True)

#danceability_list.sort(key=operator.attrgetter('average_danceability', 'average_popularity'))

print(sorted_list)
print(sorted_popularity_list)
'''



'''
#given a favorite song give a list of recommendations
input = songs.get(input("Put in a Taylor Swift you like and we will give you 5 recommended songs "))
for song in songs.values():
    score = calculate_similarity(input, song)
    name = song.name
    similarity_obj = Similarity(name, score, song.popularity)
    list1.append(similarity_obj)

def getScore(similarity):
    return similarity.score

list1.sort(key=getscore)

# print(list1)
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
finding similarity between songs
def calculate_similarity(song1, song2):
    features = ['danceability', 'energy', 'acousticness', 'valence', 'tempo']
    similarity = 0
    for feature in features:
        similarity += abs[song1[feature] - song2[feature]]
    return similarity

'''




