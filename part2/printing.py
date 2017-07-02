import pprint
from reports import *


# Printing functions
def pretty_print_results(file_name, title):
    pprint.pprint(get_most_played(file_name))
    pprint.pprint(sum_sold(file_name))
    pprint.pprint(get_selling_avg(file_name))
    pprint.pprint(count_longest_title(file_name))
    pprint.pprint(get_date_avg(file_name))
    pprint.pprint(get_game(file_name, title))
    pprint.pprint(count_grouped_by_genre(file_name))
    pprint.pprint(get_date_ordered(file_name))

pretty_print_results("game_stat.txt", "Minecraft")
