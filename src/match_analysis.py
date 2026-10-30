import csv
import matplotlib.pyplot as plt
from collections import defaultdict

MATCH_CSV_PATH = "resources/matches.csv"
matches_data = {}

def calculate(path : str):
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

def plot(data: dict):
    if not data:
        print("No data exists")
        return

    years = sorted(list(data.keys()))
    teams = set()
    for year in years:
        teams.update(team for team in data[year] if team != "total_matches")

    fig, ax = plt.subplots()

    bottom = [0] * len(years)

    for team in teams:
        counts = [data[year].get(team, 0) for year in years]

        ax.bar(years, counts, bottom=bottom, label=team)

        bottom = [bottom[i] + counts[i] for i in range(len(years))]

    ax.set_title("Matches Played by Team by Season")
    ax.set_xlabel("Season")
    ax.set_ylabel("Matches Played")
    ax.legend()

    plt.show()

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


    plt.show()








data = calculate(MATCH_CSV_PATH)
plot_number_of_matches_played_per_year(data)


