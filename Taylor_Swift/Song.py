class Song:
    def __init__(self, name, album, track_number, release_date, popularity, danceability, duration_ms, acousticness, energy,
                 valence, tempo, liveness):
        self.name = name
        self.album = album
        self.track_number = track_number
        self.release_date = release_date
        self.popularity = popularity
        self.danceability = danceability
        self.duration_ms = duration_ms
        self.acousticness = acousticness
        self.energy = energy
        self.valence = valence
        self.tempo = tempo
        self.liveness = liveness

    def __repr__(self):
        return repr((self.name, self.album, self.track_number, self.release_date, self.popularity, self.danceability, self.duration_ms,  self.acousticness, self.energy, self.valence, self.tempo, self.liveness))
