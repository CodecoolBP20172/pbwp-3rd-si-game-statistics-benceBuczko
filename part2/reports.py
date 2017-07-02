import csv
import statistics
import math


# Report functions
def open_file(file_name):
    with open(file_name) as file:
        games = csv.reader(file, delimiter="\t")
        return list(games)


def get_most_played(file_name):
    titlebysold = {}
    for i in open_file(file_name):
        titlebysold[i[0]] = float(i[1])
    return max(titlebysold, key=titlebysold.get)


def sum_sold(file_name):
    return sum(float(i[1]) for i in open_file(file_name))


def get_selling_avg(file_name):
    return sum(float(i[1]) for i in open_file(file_name))/len(open_file(file_name))


def count_longest_title(file_name):
    return max(len(i[0]) for i in open_file(file_name))


def get_date_avg(file_name):
    return math.ceil(statistics.mean(int(i[2]) for i in open_file(file_name)))


def get_game(file_name, title):
    for i in open_file(file_name):
        if i[0] == title:
            i[1] = float(i[1])
            i[2] = int(i[2])
            return i


def count_grouped_by_genre(file_name):
    genres = {}
    for i in open_file(file_name):
        if i[3] in genres:
            genres[i[3]] += 1
        else:
            genres[i[3]] = 1
    return genres


def get_date_ordered(file_name):
    titlebyyear = {}
    for i in open_file(file_name):
            titlebyyear[i[0]] = i[2]
    sorted_list = sorted(titlebyyear.items(), key=lambda x: (-int(x[1]), x[0]))
    correct_list = []
    for i in sorted_list:
        correct_list.append(i[0])
    return correct_list
