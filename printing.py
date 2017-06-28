import pprint
from reports import *


# Printing functions
def pretty_print_results(file_name, year, title, genre):
    pprint.pprint(count_games(file_name))
    pprint.pprint(decide(file_name, year))
    pprint.pprint(get_latest(file_name))
    pprint.pprint(count_by_genre(file_name, genre))
    pprint.pprint(get_line_number_by_title(file_name, title))
    pprint.pprint(get_genres(file_name))
    pprint.pprint(when_was_top_sold_fps(file_name))
