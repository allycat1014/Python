class Character:
    def __init__(self, id, name, gender, house):
        self.id = id
        self.name = name
        self.gender = gender
        self.house = house
        self.movies = set()
        self.places = set()
        self.dialogue = set()
        self.characters_mentioned = set()
    def __repr__(self):
        return repr((self.id, self.name, self.gender, self.house))
    def __eq__(self,other):
        return self.id == other.id
    def __hash__(self):
        return self.id

    def acted_with(self, character_obj):
        char3 = set()
        for x in self.movies:
            if x in character_obj.movies:
                char3.add(x)
        return char3


    def has_acted_in(self, movie_name):
        #print(self.movies)
        #print(movie_name)
        found_movie = False
        for i in self.movies:
            if i.name == movie_name:
                found_movie = True
        if found_movie == True:
            print ("Yes")
        else:
            print("No")

    def acted_in(self, movies):
        common_movies = set()
        for movie in self.movies:
            if movie in movies:
                common_movies.add(movie)
        return common_movies