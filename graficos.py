from pca import features, variancia_explicada, proj, autovetores, df
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import pca



# -------------------------
# 1) Heatmap da correlação
# -------------------------

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


# -------------------------
# 2) Scree Plot
# -------------------------

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


# -------------------------
# 3) Scatter PC1 x PC2
# -------------------------

plt.figure(figsize=(8,6))

plt.scatter(
    proj[:,0],
    proj[:,1]
)

for i, name in enumerate(df["PlayerName"]):
    plt.text(
        proj[i,0],
        proj[i,1],
        name,
        fontsize=8
    )

plt.axhline(0)
plt.axvline(0)

plt.xlabel(
    f"PC1 ({variancia_explicada[0]*100:.1f}%)"
)

plt.ylabel(
    f"PC2 ({variancia_explicada[1]*100:.1f}%)"
)

plt.title("Jogadores projetados em PC1 x PC2")

plt.show()



