from pca import features, variancia_explicada, proj, autovetores, df
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pca
from adjustText import adjust_text



# 1) Heatmap da correlação

corr = pca.X_centered.corr()

plt.figure(figsize=(6,5))
plt.imshow(corr, interpolation='nearest')
plt.colorbar()

plt.xticks(range(len(features)), features, rotation=45)
plt.yticks(range(len(features)), features)

for i in range(len(features)):
    for j in range(len(features)):
        plt.text(
            j,
            i,
            f"{corr.iloc[i,j]:.2f}",
            ha='center',
            va='center'
        )

plt.title("Matriz de Correlação")
plt.tight_layout()
plt.show()


# 2) Scree Plot

plt.figure(figsize=(6,4))
plt.bar(
    range(1, len(variancia_explicada)+1),
    variancia_explicada * 100
)

plt.xticks(range(1, len(variancia_explicada)+1))
plt.xlabel("Componente Principal")
plt.ylabel("Variância Explicada (%)")
plt.title("Scree Plot")

plt.show()


# 3) Scatter PC1 x PC2

plt.figure(figsize=(10,8))

plt.scatter(
    proj[:,0],
    proj[:,1],
    alpha=0.5
)

texts = []

# nomes apenas do top 10
top10 = df.nlargest(10, "ATPPoints")

for _, player in top10.iterrows():
    idx = df.index[df["PlayerId"] == player["PlayerId"]][0]

    texts.append(
        plt.text(
            proj[idx,0],
            proj[idx,1],
            player["PlayerName"],
            fontsize=9,
            bbox=dict(
                boxstyle="round,pad=0.3",
                fc="white",
                alpha=0.7
            )
        )
    )

# move os textos para evitar sobreposição
adjust_text(
    texts,
    arrowprops=dict(
        arrowstyle="-",
        color="gray"
    )
)

plt.axhline(0)
plt.axvline(0)

plt.xlabel(f"PC1 ({variancia_explicada[0]*100:.1f}%)")
plt.ylabel(f"PC2 ({variancia_explicada[1]*100:.1f}%)")

plt.title("Jogadores projetados em PC1 x PC2")

plt.show()