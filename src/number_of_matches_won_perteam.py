import csv
import matplotlib.pyplot as plt
from collections import defaultdict

MATCH_CSV_PATH = "resources/matches.csv"
DELIVERIES_PATH = "./resources/deliveries.csv"


def fetch_number_of_matches_won_by_each_team(path : str):
    match_data = {}
    try:
        with open(path,'r',encoding="utf-8") as csv_file:
            rows = csv.DictReader(csv_file)
            for row in rows:
                year = row["season"]
                winner = row["winner"]
                if not year or not winner:
                    continue
                if year not in match_data:
                    match_data[year] = defaultdict(int)
                match_data[year][winner] += 1
    except FileNotFoundError:
        raise FileNotFoundError(f"file is not found @ {path}")
    except OSError:
        raise OSError("permission denied")
    return match_data

def plot_stack_graph(data:dict):
    years = sorted(list(data.keys()))
    teams = set()
    for year in years:
        teams.update(team for team in data[year])


    fig,ax = plt.subplots()
    bottom = [0] * len(years)

    for team in teams:
        counts = [data[year].get(team, 0) for year in years]

        ax.bar(years, counts, bottom=bottom, label=team)

        bottom = [bottom[i] + counts[i] for i in range(len(years))]

    ax.set_title("Matches won by each team")
    ax.set_xlabel("Year")
    ax.set_ylabel("Matches Won")
    ax.legend()

    plt.savefig('output/6.png')
    plt.show()


def main():
    data = fetch_number_of_matches_won_by_each_team(MATCH_CSV_PATH)
    plot_stack_graph(data)

if __name__ == "__main__":
    main()