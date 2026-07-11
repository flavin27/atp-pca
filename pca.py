import json
import pandas as pd
from pathlib import Path
import numpy as np

DATA_DIR = Path("data")


def load_atp_stat(filename, stat_field, output_name):
    with open(DATA_DIR / filename, encoding="utf-8") as f:
        data = json.load(f)

    rows = []

    for player in data["Leaderboard"]:
        rows.append({
            "PlayerId": player["PlayerId"],
            output_name: player["Stats"][stat_field]
        })

    return pd.DataFrame(rows)


# Ranking ATP

ranking = pd.read_json(DATA_DIR / "ranking.json")

ranking = ranking[
    [
        "PlayerId",
        "PlayerName",
        "ATPPoints"
    ]
]

# Remove possíveis entradas duplicadas (mesmo PlayerId com formas diferentes do nome)
ranking = ranking.drop_duplicates(subset="PlayerId", keep="first")

# Estatísticas ATP

serve = load_atp_stat(
    "serve.json",
    "ServeRatingSortField",
    "ServeRating"
)

returns = load_atp_stat(
    "return.json",
    "ReturnRatingSortField",
    "ReturnRating"
)

pressure = load_atp_stat(
    "pressure.json",
    "PressureRatingSortField",
    "PressureRating"
)

# Merge

df = ranking.merge(serve, on="PlayerId")
df = df.merge(returns, on="PlayerId")
df = df.merge(pressure, on="PlayerId")

print("\nDataset final:")
print(df.head())


# Matriz de correlação

features = [
    "ATPPoints",
    "ServeRating",
    "ReturnRating",
    "PressureRating"
]

corr_matrix = df[features].corr()

print("\nMatriz de correlação:")
print(corr_matrix)

# Centralização

X_centered = df[features] - df[features].mean()

# PCA

autovalores, autovetores = np.linalg.eig(X_centered.corr())

# índices dos autovalores em ordem decrescente
idx = np.argsort(autovalores)[::-1]

# reordena ambos
autovalores = autovalores[idx]
autovetores = autovetores[:, idx]

variancia_explicada = autovalores / autovalores.sum()

print("Autovalores:")
print(autovalores)

print("\nVariância explicada:")
for i, v in enumerate(variancia_explicada):
    print(f"PC{i+1}: {100*v:.2f}%")



features = X_centered.columns

print("\nComponentes principais:")

for i in range(len(autovalores)):
    print(f"\nPC{i+1} ({100*variancia_explicada[i]:.2f}% da variância)")
    for feature, peso in zip(features, autovetores[:, i]):
        print(f"{feature:15} {peso: .4f}")


#projecao

proj = X_centered.to_numpy() @ autovetores

