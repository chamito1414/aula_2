import pandas as pd

base = pd.read_csv("https://www.football-data.co.uk/mmz4281/2425/D1.csv")
base.to_csv("base.csv",index=False)