class Album:
    def __init__(self, name, track_number, release_date,):
        self.name = name
        self.track_number = track_number
        self.release_date = release_date
    def __repr__(self):
        return repr((self.name, self.track_number, self.release_date))


