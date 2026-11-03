import csv
import matplotlib.pyplot as plt
from collections import defaultdict

MATCH_CSV_PATH = "resources/matches.csv"
DELIVERIES_PATH = "./resources/deliveries.csv"

def fetch_extra_runs_conceded_by_year(path_of_matches:str,path_of_deliveries:str, year: str):
    #get match id from the given year
    match_ids = set()
    with open(path_of_matches,'r',encoding="utf-execute()8") as match_csv:
        matches = csv.DictReader(match_csv)
        for match in matches:
            if match["season"] == year:
                match_ids.add(match["id"])
    extra_deliveries = defaultdict(int)
    with open(path_of_deliveries,'r',encoding= "utf-8") as del_csv:
        deliveries = csv.DictReader(del_csv)
        for delivery in deliveries:
            if delivery["match_id"] in match_ids:
                team = delivery["bowling_team"]
                extra_deliveries[team] += int(delivery["extra_runs"])
    return extra_deliveries



def plot_extra_runs_conceded(data : dict):
    sorted_data = sorted(data.items(),key= lambda item : item[1])
    teams = [team for team,_ in sorted_data]
    extra_runs = [runs for _,runs in sorted_data]
    fig,ast = plt.subplots()
    ast.bar(teams,extra_runs)
    ast.set_title("Extra runs conceded in year 2016")
    ast.set_xlabel("teams")
    ast.set_ylabel("Extra Runs")

    ast.tick_params(axis="x", labelrotation=45)
    plt.setp(ast.get_xticklabels(), ha="right")
    fig.tight_layout()
    plt.savefig('output/extra_runs_conceded.png', dpi=300, bbox_inches='tight')

    plt.show()

if __name__ == "__main__":
    data = fetch_extra_runs_conceded_by_year(MATCH_CSV_PATH, DELIVERIES_PATH, "2016")
    plot_extra_runs_conceded(data)

