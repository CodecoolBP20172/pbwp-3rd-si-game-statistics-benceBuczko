import csv


# Report functions

def open_file(file_name):
    with open(file_name) as file:
        games = csv.reader(file, delimiter="\t")
        return list(games)


def count_games(file_name):
    length = len(list(open_file(file_name)))
    return length


def decide(file_name, year):
    for i in open_file(file_name):
        if i[2] == str(year):
            return True
    return False


def get_latest(file_name):
    titlebyyear = {}
    for i in open_file(file_name):
        titlebyyear[i[0]] = int(i[2])
    return max(titlebyyear, key=titlebyyear.get)


def count_by_genre(file_name, genre):
    genres = []
    for i in open_file(file_name):
        genres.append(i[3])
    return genres.count(genre)


def get_line_number_by_title(file_name, title):
    for i in open_file(file_name):
        if i[0] == title:
            return open_file(file_name).index(i)+1
    raise ValueError


def get_genres(file_name):
    genres = []
    for i in open_file(file_name):
        if i[3] not in genres:
            genres.append(i[3])
    return sorted(genres, key=str.lower)


def when_was_top_sold_fps(file_name):
    yearbysold = {}
    for i in open_file(file_name):
        if i[3] == "First-person shooter":
            yearbysold[i[2]] = float(i[1])
    if yearbysold == {}:
        raise ValueError
    return int(max(yearbysold, key=yearbysold.get))
