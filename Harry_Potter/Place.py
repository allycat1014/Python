class Place:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category
        self.characters = set()
        def __repr__(self):
            return repr((self.id, self.name, self.category))
        def __eq__(self,other):
            return self.id == other.id
        def __hash__(self):
            return self.id