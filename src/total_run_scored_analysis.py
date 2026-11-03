import csv

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from collections import defaultdict



DELIVERIES_PATH = "./resources/deliveries.csv"

def calculate_total_runs_scored(path : str):
    total_scores = defaultdict(int)
    try:
        with open(path,'r',encoding="utf-8") as deliveries_csv:
            deliveries_rows= csv.DictReader(deliveries_csv)
            for row in deliveries_rows:
                team = row.get("batting_team")
                runs = row.get("total_runs")
                if not team or not runs:
                    continue
                else:
                    try:
                        total_scores[team] += int(runs)
                    except ValueError:
                        continue
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found: {path}")
    except OSError as error:
        raise OSError(f"Could not read {path} :{error}") from error
    return total_scores




def plot(data: dict[str,int]) -> None:
    if not data:
        print("No data available to plot")
        return

    # sort the data based on total run scored
    sorted_data = sorted(data.items(), key= lambda item:item[1])
    teams = [team for team,_ in sorted_data]
    runs = [runs for _,runs in sorted_data]

    fig, ax = plt.subplots()
    ax.set_title("IPL Runs")
    ax.set_xlabel("Team")
    ax.bar(teams, runs)
    ax.tick_params(axis="x",labelrotation = 45)
    plt.setp(ax.get_xticklabels(), ha="right")
    fig.tight_layout()
    plt.savefig('output/total_runs_scored_by_each_team_in_ipl.png', dpi=300, bbox_inches='tight')


    plt.show()


def main():
    data = calculate_total_runs_scored(DELIVERIES_PATH)
    plot(data)


if __name__ == "__main__":
    main()
















