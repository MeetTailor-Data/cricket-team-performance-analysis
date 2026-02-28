import pandas as pd
import numpy as np

data = {
    "Team": ["India", "India", "Australia", "Australia", "India",
             "Australia", "India", "Australia", "India", "Australia"],
    "Player": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
    "Runs": [50, 30, 70, np.nan, 100, 20, 60, 80, np.nan, 40],
    "Balls": [30, 25, 40, 35, 60, 15, 45, 50, 20, 30]
}

df = pd.DataFrame(data)

# Unique Teams
print("Unique Teams:", df["Team"].nunique())

# Players per Team
print("\nPlayers per Team:")
print(df["Team"].value_counts())

# Total Runs per Team
print("\nTotal Runs per Team:")
print(df.groupby("Team")["Runs"].sum())

# Multiple Aggregations
print("\nTeam Statistics:")
print(df.groupby("Team")["Runs"].agg(["sum", "mean", "max", "min"]))

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill Missing Runs
df["Runs"] = df["Runs"].fillna(0)

# Team Average After Cleaning
print("\nTeam Average Runs:")
print(df.groupby("Team")["Runs"].mean())

# Strike Rate
df["Strike_Rate"] = (df["Runs"] / df["Balls"]) * 100

# Highest Strike Rate Player
highest_sr = df.loc[df["Strike_Rate"].idxmax()]
print("\nHighest Strike Rate Player:")
print(highest_sr)
print(df)
