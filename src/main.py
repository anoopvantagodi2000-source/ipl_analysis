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

def calculate_player_runs(path : str) -> dict[str,int]:
    teams_player_data = {}
    try:
        with open(path,'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                team = row["batting_team"]
                player = row["batsman"]
                runs = 0
                if not team or not player:
                    continue

                try:
                    runs = int(row["batsman_runs"])
                except ValueError:
                    raise ValueError("expected number")

                if team not in teams_player_data:
                    teams_player_data[team] = {
                     player : runs
                    }

                else:
                    if player not in teams_player_data[team]:
                        teams_player_data[team][player] = runs
                    else:
                        teams_player_data[team][player] += runs


    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found {path}")
    except OSError as error:
        raise OSError(f"file don't permission {error}") from error
    return teams_player_data




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


    plt.show()


def plot_top_batsman(data: dict[str,int]):
    if not data:
        print("no data to process")
        return
    #sort data based on runs scored by each player
    sorted_data = sorted(data.items(),key= lambda item :item[1],reverse=True)[:10]
    players = [player for player,_ in sorted_data]
    scores = [score for _,score in sorted_data]

    fig, ax = plt.subplots()
    ax.set_title("top run getters in RCB")
    ax.set_xlabel("Players Name")
    ax.bar(players,scores)
    ax.tick_params(axis="x", labelrotation=45)
    plt.setp(ax.get_xticklabels(), ha="right")

    plt.show()



# data = calculate_total_runs_scored(DELIVERIES_PATH)
# plot(data)

data = calculate_player_runs(DELIVERIES_PATH)["Royal Challengers Bangalore"]
plot_top_batsman(data)





