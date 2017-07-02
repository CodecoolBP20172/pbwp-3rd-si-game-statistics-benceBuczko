import csv
from reports import *


# Export functions
def export_results(file_name, title, export_file):
    with open(export_file, "w") as export:
        results = csv.writer(export, delimiter="\t")
        results.writerow([get_most_played(file_name)])
        results.writerow([sum_sold(file_name)])
        results.writerow([get_selling_avg(file_name)])
        results.writerow([count_longest_title(file_name)])
        results.writerow([get_date_avg(file_name)])
        results.writerow(get_game(file_name, title))
        results.writerow([count_grouped_by_genre(file_name)])
        results.writerow(get_date_ordered(file_name))
