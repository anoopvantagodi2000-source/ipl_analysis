import csv
from collections import defaultdict
from matplotlib import pyplot as plt

DELIVERIES_PATH = "resources/deliveries.csv"
TEAM = "Royal Challengers Bangalore"

def calculate_top_batsman_by_team(path: str,team:str):
    player_scores_by_team = defaultdict(int)
    with open(path,'r',encoding="utf-8") as matches_csv:
        deliveries = csv.DictReader(matches_csv)
        for delivery in deliveries:
            batting_team = delivery.get("batting_team")
            batsman = delivery.get("batsman")
            runs = delivery.get("batsman_runs")
            if not batting_team or not batsman or not runs:
                continue
            if batting_team == team:
                player_scores_by_team[batsman] += int(runs)
    return player_scores_by_team

def plot_rcb_top_batsman_over_the_years(data:dict[str,int]):
    sorted_data = list(sorted(data.items(),key= lambda items :items[1],reverse=True))[:10]
    batsman = [batsman for batsman,_ in sorted_data]#  top 10 batsman list
    score = [score for _,score in sorted_data] # scores each top 10 batsman

    plt.title("Top 10 batsman for rcb")
    plt.bar(batsman,score)
    plt.xlabel("Batsman")
    plt.ylabel("Scores")
    plt.xticks(rotation = 45)
    plt.show()


def main():

    data = calculate_top_batsman_by_team(DELIVERIES_PATH,TEAM)
    plot_rcb_top_batsman_over_the_years(data)

if __name__ == "__main__":
    main()



