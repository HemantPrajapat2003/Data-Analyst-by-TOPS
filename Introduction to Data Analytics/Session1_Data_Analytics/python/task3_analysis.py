# Session 1 Task 3: count matches won by each team
from pathlib import Path
import pandas as pd

# Run this file from the project folder, or change the path if needed.
data_path = Path(__file__).resolve().parents[1] / "data" / "IPL_2023_Matches_PRACTICE_SAMPLE.csv"
df = pd.read_csv(data_path)

print("Dataset preview:")
print(df.head())

print("\nMatches won by each team:")
wins = (
    df["winner"]
    .dropna()
    .value_counts()
    .rename_axis("team")
    .reset_index(name="matches_won")
)
print(wins.to_string(index=False))

print("\nMatches played per city (Task 4 preparation):")
print(df["city"].value_counts().rename_axis("city").reset_index(name="matches_played").to_string(index=False))
