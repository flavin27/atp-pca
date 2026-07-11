# ATP-PCA

Aplicação da técnica de **Análise de Componentes Principais (PCA)** em estatísticas de jogadores profissionais de tênis disponibilizadas pela ATP (Association of Tennis Professionals).

O objetivo do projeto é investigar a relação entre métricas de desempenho dos jogadores e sua posição no ranking mundial, utilizando técnicas de redução de dimensionalidade e visualização de dados.

## Atributos avaliados

Para reduzir a complexidade do problema, foram selecionados três indicadores agregados disponibilizados pela ATP:

* **Serve Rating**: representa o desempenho do jogador durante o saque;
* **Return Rating**: representa o desempenho do jogador durante a devolução;
* **Pressure Rating**: representa o desempenho do jogador em situações de pressão durante a partida.

Além dessas métricas, também foi utilizada a variável:

* **ATP Points**: quantidade de pontos acumulados pelo jogador no ranking mundial.

As estatísticas consideradas correspondem ao desempenho médio dos jogadores nas últimas **52 semanas**, seguindo a metodologia utilizada pela própria ATP.

## Estrutura do projeto

```text
.
├── data/
│   └── ...
├── pca.py
├── graficos.py
├── requirements.txt
└── README.md
```

### `pca.py`

Responsável pela etapa de preparação dos dados e execução do PCA.

O script realiza:

* carregamento dos dados coletados da ATP;
* limpeza e integração das informações;
* construção do dataset final utilizado no estudo;
* centralização e padronização das variáveis;
* cálculo da matriz de correlação;
* cálculo dos autovalores e autovetores;
* cálculo da variância explicada pelas componentes principais.

As saídas desse script correspondem aos resultados apresentados na seção de metodologia do relatório.

### `graficos.py`

Responsável pela geração das visualizações utilizadas na análise dos resultados.

O script produz:

* mapa de calor da matriz de correlação;
* gráfico da variância explicada por componente principal;
* projeção dos jogadores no espaço formado por PC1 e PC2;
* visualizações auxiliares utilizadas na interpretação das componentes principais.

As figuras geradas correspondem aos gráficos apresentados na Seção 4 do relatório.

## Instalação

Clone o repositório e instale as dependências:

```bash
pip install -r requirements.txt
```

## Como executar

### 1. Executar a etapa de processamento e PCA

```bash
python pca.py
```

Esse comando irá gerar os resultados numéricos utilizados na análise, incluindo:

* matriz de correlação;
* autovalores;
* autovetores;
* variância explicada pelas componentes principais.

### 2. Gerar os gráficos

```bash
python graficos.py
```

Esse comando irá gerar todas as figuras utilizadas na seção de resultados do trabalho.

## Principais resultados

A análise mostrou que:

* as duas primeiras componentes principais explicam aproximadamente **82,74%** da variância total dos dados;
* o atributo **Pressure Rating** apresentou a maior associação com a pontuação no ranking da ATP;
* a projeção em duas dimensões permitiu identificar agrupamentos e perfis semelhantes entre jogadores profissionais.

## Tecnologias utilizadas

* Python 3
* NumPy
* Pandas
* Scikit-Learn
* Matplotlib
* Seaborn
