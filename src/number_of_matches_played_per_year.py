import csv
import matplotlib.pyplot as plt
from collections import defaultdict

MATCH_CSV_PATH = "resources/matches.csv"
DELIVERIES_PATH = "./resources/deliveries.csv"


def calculate(path : str):
    matches_data = {}
    try:
        with open(path,'r',encoding="utf-8") as matches_csv:
            matches = csv.DictReader(matches_csv)
            for match in matches:
                year = match.get("season")
                team1 = match.get("team1")
                team2 = match.get("team2")
                if not year or not team1 or not team2:
                    continue


                if year not in matches_data:
                    matches_data[year] = defaultdict(int)

                matches_data[year][team1]= matches_data[year][team1] + 1
                matches_data[year][team2] = matches_data[year][team2] + 1
                matches_data[year]["total_matches"] = matches_data[year]["total_matches"]+1



    except FileNotFoundError:
        raise FileNotFoundError(f"file not found {path}")
    except OSError:
        raise OSError("permission denied")

    return matches_data

def plot_number_of_matches_played_per_year(data:dict):
    years = sorted(list(data.keys()))
    total_matches_played_per_season = [data[year]["total_matches"] for year in years]

    fig,ast = plt.subplots()
    ast.bar(years, total_matches_played_per_season)
    ast.set_title("total number of matches played in each year")
    ast.set_xlabel("Years")
    ast.set_ylabel("Scores")

    plt.setp(ast.get_xticklabels(), ha="right")
    fig.tight_layout()
    plt.savefig('output/number_of_matches_played_per_year.png', dpi=300, bbox_inches='tight')

    plt.show()

def main():
    data = calculate(MATCH_CSV_PATH)
    plot_number_of_matches_played_per_year(data)

if __name__ == "__main__":
    main()