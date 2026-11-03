import csv
import matplotlib.pyplot as plt
from collections import defaultdict

MATCH_CSV_PATH = "resources/matches.csv"
DELIVERIES_PATH = "./resources/deliveries.csv"

def fetch_economical_bowler_in_year(path_of_matches:str,path_of_deliveries:str, year: str):
    match_ids = set()
    with open(path_of_matches,'r',encoding="utf-8") as match_csv:
        matches = csv.DictReader(match_csv)
        for match in matches:
            if match["season"] == year:
                match_ids.add(match["id"])
    bowler_run_conceded = defaultdict(int)
    total_ball_bowled = defaultdict(int)
    with open(path_of_deliveries,'r',encoding= "utf-8") as del_csv:
        deliveries = csv.DictReader(del_csv)
        for delivery in deliveries:
            if delivery["match_id"] in match_ids:
                bowler = delivery["bowler"]
                bowler_run_conceded[bowler] += int(delivery["total_runs"])-int(delivery["bye_runs"]) - int(delivery["legbye_runs"])-int(delivery["penalty_runs"])
                wide = int(delivery["wide_runs"])
                no_ball = int(delivery["noball_runs"])
                if wide == 0 and no_ball == 0:
                   total_ball_bowled[bowler] += 1

    economy_of_bowler = {}
    for bowler in bowler_run_conceded.keys():
        economy_of_bowler[bowler] = round(bowler_run_conceded[bowler]/total_ball_bowled[bowler],2)

    return economy_of_bowler
def plot_economical_bowler(data : dict):
    sorted_data = sorted(data.items(),key= lambda item : item[1])
    bowler_names = [bowler for bowler,_ in sorted_data][:10]
    extra_runs = [runs for _,runs in sorted_data][:10]
    fig,ast = plt.subplots()
    ast.bar(bowler_names,extra_runs)
    ast.set_title("Top 10 Economical bowlers year 2015")
    ast.set_xlabel("Bowlers")
    ast.set_ylabel("runs conceded")

    ast.tick_params(axis="x", labelrotation=45)
    plt.setp(ast.get_xticklabels(), ha="right")
    fig.tight_layout()
    plt.savefig('output/bowler_economy.png', dpi=300, bbox_inches='tight')
    plt.show()


def execute():
    data = fetch_economical_bowler_in_year(MATCH_CSV_PATH, DELIVERIES_PATH, "2015")
    plot_economical_bowler(data)


if __name__ == "__main__":
    execute()
