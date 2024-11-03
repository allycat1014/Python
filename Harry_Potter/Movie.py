class Movie:
    def __init__(self, id, name, release_year):
        self.id = id
        self.name = name
        self.release_year = release_year
        self.characters = set()
        self.places = set()
    def __repr__(self):
        return repr((self.id, self.name, self.release_year))
    def __eq__(self, other):
        return self.id == other.id
    def __hash__(self):
        return self.id
    def common_characters(self, movies_obj):
        characters = set()
        for character in self.characters:
            if character in movies_obj.characters:
                characters.add(character)
        return characters
    def common_places(self, movie_obj):
        places = set()
        for place in self.places:
            if place in movie_obj.places:
                places.add(place)
        return places
