# IPL Data Set Analytics

## AIM
To convert raw data into a story with the help of charts.

## Resources
**Data Source:** https://www.kaggle.com/manasgarg/ipl/version/5

## File Structure
```text
ipl
├── images
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   ├── 4.png
│   ├── 5.png
│   ├── 6.png
│   ├── 7.png
│   └── 8.png
├── resources
│   ├── deliveries.csv
│   ├── matches.csv
│   └── umpires.csv
├── src
│   ├── main.py
│   └── match_analysis.py
├── README.md
└── requirements.txt
```

## Project Setup
1. Fork this repository: https://github.com/anoopvantagodi2000-source/ipl_analysis.git
2. Create a **resources** folder in `ipl_analysis/`.
3. Download the CSV files from https://www.kaggle.com/manasgarg/ipl/version/5.
4. Copy the CSV files into the **resources** folder.
5. Set up a virtual environment.
6. Install the necessary libraries provided in `requirements.txt`.
7. Run the following command to analyse `deliveries.csv`:

   ```bash
   python3 src/main.py
   ```

8. Run the following command to analyse `matches.csv`:

   ```bash
   python3 src/match_analysis.py
   ```
 


