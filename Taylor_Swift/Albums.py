class Album:
    def __init__(self, name):
        self.name = name
        self.tracks = set()
        self.most_popular_track = None
    def __repr__(self):
        return repr((self.name))


