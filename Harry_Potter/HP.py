import pandas
from Character import Character
from Movie import Movie
from Place import Place

#from place_class import category

chapters_file = pandas.read_csv('data/Chapters.csv', encoding='latin1', usecols=['Chapter ID', 'Chapter Name', 'Movie ID', 'Movie Chapter'])
chapters = chapters_file.to_dict(orient='records')

characters_file = pandas.read_csv('data/Characters.csv', encoding='latin1',  usecols=['Character ID', 'Character Name', 'Species', 'Gender', 'House','Patronus', 'Wand (Wood)', 'Wand (Core)'])
characters = characters_file.to_dict(orient='records')

dialogues_file = pandas.read_csv('data/Dialogue.csv', encoding='latin1', usecols=['Dialogue ID','Chapter ID','Place ID','Character ID','Dialogue'])
dialogues = dialogues_file.to_dict(orient='records')

movies_file = pandas.read_csv('data/Movies1.csv', encoding='latin1', usecols=['Movie ID','Movie Title','Release Year','Runtime','Budget','Box Office'])
movies = movies_file.to_dict(orient='records')

places_file = pandas.read_csv('data/Places.csv', encoding='latin1', usecols=['Place ID','Place Name','Place Category'])
places = places_file.to_dict(orient='records')

chapter_id = set()
movie_id = set()
movie_name = set()
profit = 0
richest_movie = ""
place_id = set()
place_name = set()
richest = 0
dict1 = {}
dict2 = {}
count = 0
largest = 0
most = ''
list1 = []
list2 = []
largest_movie_id = 0
characters1 = {}
chapters1 = {}
movies1 = {}
final_characters = {}
final_movies = {}
places1 = {}


'''
    def is_in_same_house(self, character_obj):

    def no_of_movies_played_in(self):
'''
for character in characters:
    name = str(character['Character Name'])
    id = int(character['Character ID'])
    gender = str(character['Gender'])
    house = str(character['House'])
    if id not in characters1.keys():
        character_obj = Character(id, name, gender, house)
        characters1[id] = character_obj

for movie in movies:
    name = str(movie['Movie Title'])
    id = int(movie['Movie ID'])
    release_year = str(movie["Release Year"])
    if id not in movies1.keys():
        movies_obj = Movie(id, name, release_year)
        movies1[id] = movies_obj

for chapter in chapters:
    movie = int(chapter["Movie ID"])
    chapter1 = int(chapter["Chapter ID"])
    if chapter1 not in chapters1.keys():
        chapters1[chapter1] = movie

for place in places:
    id = int(place["Place ID"])
    name = str(place["Place Name"])
    category = str(place["Place Category"])
    if id not in places1.keys():
        place_obj = Place(id, name, category)
        places1[id] = place_obj

for dialogue in dialogues:
    characterid = int(dialogue['Character ID'])
    chapterid = int(dialogue['Chapter ID'])
    placeid = int(dialogue['Place ID'])
    dialogueid = int(dialogue['Dialogue ID'])
    movieid = chapters1.get(chapterid)
    character_obj = characters1.get(characterid)
    movie_obj = movies1.get(movieid)
    character_obj.movies.add(movie_obj)
    character_obj.dialogue.add(dialogueid)
    place_obj = places1.get(placeid)
    if character_obj.name not in final_characters.keys():
        final_characters[character_obj.name] = character_obj
    movie_obj.characters.add(character_obj)
    if movie_obj.name not in final_movies.keys():
        final_movies[movie_obj.name] = movie_obj
    movie_obj.places.add(place_obj)
    character_obj.places.add(place_obj)
    place_obj.characters.add(character_obj)
'''
which character had the least dialogues?
least = 123456789
name = ''
for character in final_characters.values():
    count = len(character.dialogue)
    if count < least:
        least = count
        name = character.name
print(name)
'''
'''
which character has the most dialogues?
most = 0
name = ''
for character in final_characters.values():
    count = len(character.dialogue)
    if count > most:
        most = count
        name = character.name
print(name)
'''
'''
which characters appear in only one movie? 
place12 = set()
for character in final_characters.values():
    count = len(character.movies)
    if count == 1:
        place12.add(character.name)
print(place12)
'''
'''
which character has been to the most places?
most_char = {}
character_answer = None
largest_places_count = 0
for character in final_characters.values():
    places_count = len(character.places)
    most_char[character.name] = places_count
    
print(most_char)
'''
'''
what place shows up the most in all movies?
count1 = 0
largest1 = 0
final_place = None
most_place = {}
for movie in final_movies:
    movie_obj1 = final_movies.get(movie)
    for place in movie_obj1.places:
        count = 1
        if place in most_place.keys():
            count = most_place.get(place)
            count += 1
            most_place[place] = count
        if place not in most_place.keys():
            most_place[place] = count
        if count > largest1:
            largest1 = count
            final_place = place

print(final_place.name)
'''
'''
for place in places1.values():
    length = len(place.characters)
    if length > largest:
        largest = length
        name = place.name
print(name)
'''
'''
movie1 = input("Put in a first movie name ")
movie2 = input("Put in a second movie name ")

movie1_obj = final_movies.get(movie1)
movie2_obj = final_movies.get(movie2)
print(movie1_obj.common_characters(movie2_obj))
print("Common Places")
print(movie1_obj.common_places(movie2_obj))
'''
'''
char2 = input("Put in a second character name ")

char1 = input("Put in a first character name ")
movie_in = input("Enter a movie ")

char1_obj = final.get(char1)
char1_obj.has_acted_in(movie_in)
'''

'''
char1_obj = final.get(char1)

char2_obj = final.get(char2)

char1_obj.acted_with(char2_obj)
'''

'''
if char1 in final.keys():
    character_obj = final.get(char1)
    print(character_obj)
if char1 not in final.keys():
    print("Error! Put enter an actual character")
'''
'''
    if character_obj.name in final.keys():
        t = final.get(character_obj.name)
        t.add(character_obj)
    if character_obj.name not in final.keys():
        t = set()
        t.add(character_obj)
        final[character_obj.name] = t
'''







'''
for character in characters:
    name = str(character['Character Name'])
    id = str(character['Character ID'])
    if id not in characters1.keys():
        characters1[id] = name
for chapter in chapters:
    movie = str(chapter["Movie ID"])
    chapter1 = str(chapter["Chapter ID"])
    if chapter1 not in chapters1.keys():
        chapters1[chapter1] = movie
for movie in movies:
    id = str(movie["Movie ID"])
    name = str(movie['Movie Title'])
    if id not in movies1.keys():
        movies1[id] = name
for dialogue in dialogues:
    characterid = str(dialogue['Character ID'])
    chapterid = str(dialogue['Chapter ID'])
    movieid = chapters1.get(chapterid)
    charactername = characters1.get(characterid)
    name = movies1.get(movieid)
    if charactername in final.keys():
        t = final.get(charactername)
        t.add(name)
    if charactername not in final.keys():
        t = set()
        t.add(name)
        final[charactername] = t
x = input("Put in a character name ")
if x in final.keys():
    ans = final.get(x)
    print(ans)
if x not in final.keys():
    print("Error! Put enter an actual character")
'''
'''
for character in characters:
    name = str(character['Character Name'])
    id = str(character['Character ID'])
    if name == "Sirius Black":
        character_id = id
        break

for dialogue in dialogues:
    chapter = str(dialogue['Chapter ID'])
    id = str(dialogue['Character ID'])
    if id == character_id:
        chapter_id.add(chapter)

for chapter in chapters:
    id = str(chapter['Chapter ID'])
    movie = str(chapter['Movie ID'])
    if id in chapter_id:
        movie_id.add(movie)
for movie in movies:
    id = str(movie['Movie ID'])
    name = str(movie['Movie Title'])
    if id in movie_id:
        movie_name.add(name)

print(movie_name)
'''
'''
for chapter in chapters:
    mid = int(chapter['Movie ID'])
    cid = int(chapter['Chapter ID'])
    dict1[cid] = mid
for dialogue in dialogues:
    cid = int(dialogue['Chapter ID'])
    pid = int(dialogue['Place ID'])
    movie = dict1.get(cid)
    if movie in dict2.keys():
        place_id = dict2.get(movie)
        place_id.add(pid)
    if movie not in dict2.keys():
        place_id = set()
        dict2[movie] = place_id
    if len(place_id) > largest:
        largest = len(place_id)
        largest_movie_id = movie
for movie in movies:
    name = str(movie['Movie Title'])
    id = int(movie['Movie ID'])
    if id == largest_movie_id:
        print(name)
'''
'''
for chapter in chapters:
    id = int(chapter['Movie ID'])
    cid = int(chapter['Chapter ID'])
    dict1[cid] = id
for dialogue in dialogues:
    id = int(dialogue['Chapter ID'])
    cid = int(dialogue['Character ID'])
    movie = dict1.get(id)
    if movie in dict2.keys():
        character_id = dict2.get(movie)
        character_id.add(cid)
        dict2[movie] = character_id
    if movie not in dict2.keys():
        character_id = set()
        dict2[movie] = character_id
    if len(character_id) > largest:
        largest = len(character_id)
        largest = movie
for movie in movies:
    name = str(movie['Movie Title'])
    id = int(movie['Movie ID'])
    if id == largest:
        print(name)
'''
'''
for dialogue in dialogues:
    place = int(dialogue['Place ID'])
    if place in dict1.keys():
        count = dict1.get(place)
        count += 1
        dict1[place] = count
    if place not in dict1.keys():
        dict1[place] = 1
for place in places:
    id = int(place['Place ID'])
    name = str(place['Place Name'])
    if dict1.get(id) > largest:
        largest = dict1.get(id)
        most = name
print(most)
'''
'''
for movie in movies:
    box_office = str(movie['Box Office'])
    name = str(movie['Movie Title'])
    budget = str(movie['Budget'])
    box_office = box_office.replace(',','')
    box_office = box_office.replace('$', '')
    box_office = int(box_office)
    budget = budget.replace(',','')
    budget = budget.replace('$', '')
    budget = int(budget)
    profit = box_office - budget
    if profit > richest:
        richest_movie = name
print(richest_movie)
'''
'''
for character in characters:
    name = str(character['Character Name'])
    id = str(character['Character ID'])
    if name == "Molly Weasley":
        character_id = id
        break
for dialogue in dialogues:
    id = str(dialogue['Character ID'])
    place = str(dialogue['Place ID'])
    if id == character_id:
        place_id.add(place)

for place in places:
    id = str(place['Place ID'])
    name = str(place['Place Name'])
    if id in place_id:
        place_name.add(name)
print(place_name)
'''
'''
for character in characters:
    name = str(character['Character Name'])
    id = str(character['Character ID'])
    if name == "Sirius Black":
        character_id = id
        break

for dialogue in dialogues:
    chapter = str(dialogue['Chapter ID'])
    id = str(dialogue['Character ID'])
    if id == character_id:
        chapter_id.add(chapter)

for chapter in chapters:
    id = str(chapter['Chapter ID'])
    movie = str(chapter['Movie ID'])
    if id in chapter_id:
        movie_id.add(movie)

for movie in movies:
    id = str(movie['Movie ID'])
    name = str(movie['Movie Title'])
    if id in movie_id:
        movie_name.add(name)

print(movie_name)
'''












