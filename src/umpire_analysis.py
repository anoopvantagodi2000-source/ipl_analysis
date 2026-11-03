import csv
from collections import defaultdict
from matplotlib import pyplot as plt



UMPIRES_PATH = "resources/umpires.csv"

def calculate_umpire_from_each_country(path : str):
    #represents number of umpires from each country who represented in ipl
    country_ump_freq = defaultdict(int)
    try :
        with open(path,'r',encoding="utf-8") as umpires_csv_file:
            umpires_row = csv.DictReader(umpires_csv_file)
            for row in umpires_row:
                country = row["country"]
                if not country:
                    continue
                else:
                   country_ump_freq[country]   += 1
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV File not found {path}")
    except OSError as err:
        raise OSError(f"permission denied by {err}") from err
    return  country_ump_freq



def plot_umpires_from_country(data : dict[str,int]):
    if not data:
        print("There is no data to plot")
    sorted_data = sorted(data.items(), key=lambda item: item[1])
    sorted_data = sorted_data[:len(sorted_data)-1]
    countries = [country for country ,_ in sorted_data]
    freq = [freq for _,freq in sorted_data]
    fig,ax = plt.subplots()
    ax.set_title("# of Umpires represented from countries in IPL")
    ax.set_xlabel("country")

    ax.bar(countries,freq)
    ax.tick_params(axis="x",labelrotation = 45)
    plt.setp(ax.get_xticklabels(), ha="right")
    plt.savefig('output/umpires_represented_by_country_in_ipl.png', dpi=300, bbox_inches='tight')
    plt.show()

def main():
    data = calculate_umpire_from_each_country(UMPIRES_PATH)
    plot_umpires_from_country(data)


if __name__ == "__main__":
    main()