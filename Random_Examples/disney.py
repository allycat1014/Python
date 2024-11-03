# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import csv
import pandas


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def word_frequency():
    f = open("/Users/Ananya/Downloads/sample_text.txt", "r")
    word_freq = {}
    for x in f:
        tokens = x.split()
        for y in tokens:
            if y in word_freq.keys():
                count = word_freq.get(y)
                count = count + 1
                word_freq[y] = count
            else:
                word_freq[y] = 1
    print(word_freq)


# using tuples
def square_numbers():
    sample_tuple = (4, -9, 0, 34, 67, 23, 5)
    sample_tuple_sqr = []

    for x in sample_tuple:
        y = x * x
        sample_tuple_sqr.append(y)
    new_tuple = tuple(sample_tuple_sqr)
    print(new_tuple)


def add_grade(grade, grades, result):
    if grade in grades.keys():
        list1 = grades[grade]
        list1.append(result)
    # grades[grade] = list1
    else:
        list1 = [grade];
        grades[grade] = list1


def categorize_grades():
    results = [45, 96, 88, 76, 23, 90, 84, 64, 90, 85, 98, 58, ]
    ranges = {"A": 100, "B": 89, "C": 79, "D": 69, "F": 59}
    grades = {}
    for result in results:
        if result > ranges["B"]:
            grade = "A"
            add_grade(grade, grades, result)
        elif result > ranges["C"]:
            add_grade("B", grades, result)
        elif result > ranges["D"]:
            add_grade("C", grades, result)
        elif result > ranges["F"]:
            add_grade("D", grades, result)
        else:
            add_grade("F", grades, result)
    print(grades)


def disney_fun():
    result = pandas.read_csv('/Users/ananya/Python/disney_plus_titles.csv',
                             usecols=['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added',
                                      'release_year', 'rating', 'duration', 'listed_in', 'description'])
    records = result.to_dict(orient='records')
    movies_count = 0
    largest = 0
    title1 = ""
    set1 = set()
    dict1 = {}
    year = 0
    list1 = []
    list2 = []
    list3 = []
    count = 0
    for record in records:
        cast = str(record['cast'])
        title = str(record['title'])
        show_id = str(record['show_id'])
        type1 = str(record['type'])
        director = str(record['director'])
        country = str(record['country'])
        release_year = int(record['release_year'])
        rating = str(record['rating'])
        duration = str(record['duration'])
        listed_in = str(record['listed_in'])
        description = str(record['description'])


    '''
        for x in listed_in.split(","):
            x = x.strip()
            if x == "Comedy":
                for i in cast.split(","):
                    i = i.strip()
                    if i in dict1.keys():
                        value = dict1.get(i)
                        value.add(type1)
                        dict1[i] = value
                        if len(value) > 1 and i != "nan":
                            set1.add(i)
                    else:
                        set2 = set()
                        set2.add(type1)
                        dict1[i] = set()
    print(set1)



    
        if type1 == "Movie":
            for i in cast.split(","):
                i = i.strip()
                list1.append(i)
        elif type1 == "TV Show":
            for x in cast.split(","):
                x = x.strip()
                list2.append(x)
    for a in list1:
        if a in list2 and a != "nan":
            set1.add(a)
    print(set1)


        if type1 == "Movie":
            for i in director.split(","):
                i = i.strip()
                if i in cast.split(",") and i != "nan":
                    set1.add(i)
    print(set1)

        if type1 == "Movie":
            directors  = director.split(",")
            for movie_director in directors:
                movie_director = movie_director.strip()
                seen_directors = dict1.keys()
                if movie_director in seen_directors:
                    count = dict1.get(movie_director)
                    count += 1
                    dict1[movie_director] = count
                    if dict1.get(movie_director) > 1:
                        list1.append(movie_director)
                else:
                    dict1[movie_director] = 1
    print(list1)






        if type1 == "Movie":
            if len(director.split(",")) > 1:
                set1.add(title)
    print(set1)



        if type1 == "Movie":
            for i in listed_in.split(","):
                i = i.strip()
                if rating == "PG-13" and i == "Comedy" or "Family":
                    set1.add(title)

    print(set1)


    
        if type1 == "Movie":
            for i in listed_in.split(","):
                i = i.strip()
                if i in dict1.keys():
                    count = dict1.get(i)
                    count += 1
                    dict1[i] = count
                else:
                    dict1[i] = 1
                if dict1.get(i) > largest:
                    largest = dict1.get(i)
                    genre = i
    print(genre)
    print(dict1)
    
        if type1 == "Movie":
            duration = duration.split()
            number = duration[0]
            genres = listed_in.split(",")
            list2 = []
            for i in genres:
                i = i.strip()
                list2.append(i)
            if "Family" in list2 and int(number) > 60:
                list1.append(title)
            else:
                pass
    print(list1)

    
        if release_year >= 2023:
            print(title)
            movies_count += 1
    print(movies_count)
    
        if type1 == "Movie":
            for i in duration.split():
                if i.isdigit():
                    duration_min = int(i)
                    if duration_min > largest:
                        largest = duration_min
                        title1 = title
                        movies_count += 1
    print(title1)
    print(largest)
    print(movies_count)
    
        if "Dove Cameron" in cast:
            if type1 == "Movie":
                for i in duration.split():
                    if i.isdigit():
                        duration_min = int(i)
                        if duration_min > largest:
                            largest = duration_min
                            title1 = title
                            movies_count += 1
    

        if "Dove Cameron" in cast:
            for i in listed_in.split(","):
                i = i.strip()
                set1.add(i)
    print(set1)
    
        if type1 == "Movie":
            for i in listed_in.split(","):
                i = i.strip()
                key2 = '***** ' + i + ' *******'
                if key2 in dict1.keys():
                    list_movies = dict1.get(key2)
                    list_movies.append(title)
                else:
                    list1 = []
                    list1.append(title)
                    key1 = '***** ' + i + ' *******'
                    dict1[key1] = list1
    print(dict1)
    
        if type1 == "Movie":
            for i in str(release_year).split(","):
                if i in dict1.keys():
                    count = dict1.get(i)
                    count += 1
                    dict1[i] = count
                else:
                    dict1[i] = 1
                if dict1.get(i) > largest:
                    largest = dict1.get(i)
                    year = release_year
    print(year)
    print(dict1)
    '''


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # word_frequency()
    # square_numbers()
    # categorize_grades()
    disney_fun()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# with open('/Users/hiren/Downloads/disney_plus_titles.csv', newline='') as csvfile:
# reader = csv.reader(csvfile)
#    for row in reader:
#       print(row)
