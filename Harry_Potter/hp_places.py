import pandas

places_file = pandas.read_csv('/Users/Ananya/Downloads/Harry_Potter_Movies/Places.csv', encoding='latin1',
                              usecols=['Place ID', 'Place Name', 'Place Category'])
places = places_file.to_dict(orient='records')

dialogues_file = pandas.read_csv('/Users/Ananya/Downloads/Harry_Potter_Movies/Dialogue.csv', encoding='latin1',
                                 usecols=['Dialogue ID', 'Chapter ID', 'Place ID', 'Character ID', 'Dialogue'])
dialogues = dialogues_file.to_dict(orient='records')

characters_file = pandas.read_csv('/Users/Ananya/Downloads/Harry_Potter_Movies/Characters.csv', encoding='latin1',
                                  usecols=['Character ID', 'Character Name', 'Species', 'Gender', 'House', 'Patronus',
                                           'Wand (Wood)', 'Wand (Core)'])
characters = characters_file.to_dict(orient='records')

place_dict = {}
character_dict = {}


class Character:
    def __init__(self, id, name, gender, house):
        self.id = id
        self.name = name
        self.gender = gender
        self.house = house
        self.places1 = set()


class Place:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category
        self.characters = set()
        self.character_count = 0

    def __repr__(self):
        return repr(self.name)


for character in characters:
    character_obj = Character(int(character['Character ID']), str(character['Character Name']),
                              str(character['Gender']), str(character['House']))
    character_dict[character_obj.id] = character_obj

for place in places:
    category = str(place['Place Category'])
    place_obj = Place(int(place['Place ID']), str(place['Place Name']), category)
    place_dict[place_obj.id] = place_obj

for dialogue in dialogues:
    cid = int(dialogue['Character ID'])
    pid = int(dialogue['Place ID'])
    character_obj = character_dict.get(cid)
    place_obj = place_dict.get(pid)
    character_obj.places1.add(place_obj)

hp = character_dict.get(1)

print(hp.places1)