import pandas as pd


serve = pd.json_normalize(data["Leaderboard"])[
    ["PlayerId", "PlayerName", "Stats.ServeRatingSortField"]
]