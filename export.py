import csv
from reports import *


# Export functions
def export_results(file_name, year, title, genre, export_file):
    with open(export_file, "w") as export:
        results = csv.writer(export, delimiter="\t")
        results.writerow([count_games(file_name)])
        results.writerow([decide(file_name, year)])
        results.writerow([get_latest(file_name)])
        results.writerow([count_by_genre(file_name, genre)])
        results.writerow([get_line_number_by_title(file_name, title)])
        results.writerow(get_genres(file_name))
        results.writerow([when_was_top_sold_fps(file_name)])
