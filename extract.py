from bs4 import BeautifulSoup
import json
import re

with open("ranking.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

players = []

for row in soup.select("tbody tr"):
    rank_td = row.select_one("td.rank")
    name_a = row.select_one("li.name a")
    points_td = row.select_one("td.points")

    if not (rank_td and name_a and points_td):
        continue

    # extrai o id do jogador da URL
    href = name_a["href"]

    # /en/players/jannik-sinner/s0ag/overview
    player_id = href.split("/")[-2].upper()

    player = {
        "PlayerRank": int(rank_td.get_text(strip=True)),
        "PlayerId": player_id,
        "PlayerName": name_a.get_text(strip=True),
        "ATPPoints": int(
            points_td.get_text(strip=True)
                     .replace(",", "")
        )
    }

    players.append(player)

with open("ranking.json", "w", encoding="utf-8") as f:
    json.dump(players, f, indent=2, ensure_ascii=False)