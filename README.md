# Análise Exploratória de Dados: Churn de Clientes Bancários# Análise Exploratória de Dados: Churn de Clientes Bancários

Este projeto é uma análise exploratória de dados (EDA) baseada no conjunto de dados **Churn Modelling** do Kaggle. O objetivo é entender os fatores que levam os clientes a saírem de um banco, através de análises estatísticas e visualizações.

O conjunto de dados `Churn_Modelling.csv` contém informações de clientes de um banco, incluindo dados demográficos, financeiros e de produtos, além de uma variável de interesse que indica se o cliente saiu do banco (`Exited`).

##Bibliotecas Utilizadas

- **`pandas`**: Manipulação e análise de dados.
- **`numpy`**: Funções matemáticas e manipulação de arrays.
- **`matplotlib`**: Criação de gráficos estáticos.
- **`seaborn`**: Criação de gráficos estatísticos mais atraentes.
- **`scipy`**: Funções para cálculos científicos e estatísticos.

##Análise e Visualizações

O código realiza as seguintes etapas de análise:

###Análise Exploratória de Dados (EDA)

- **Inspeção inicial**: Exibição das primeiras linhas do dataframe, nomes das colunas, tipos de dados (`.info()`) e estatísticas descritivas (`.describe()`).
- **Contagem de valores**: Análise da distribuição de variáveis categóricas como `Gender` (gênero), `Exited` (churn) e `Geography` (país).
- **Médias por grupo**: Cálculo da média de idade e salário estimado para homens e mulheres.

###Visualizações

- **Gráfico de dispersão**: Mostra a relação entre o saldo da conta (`Balance`) e o escore de crédito (`CreditScore`).
- **Gráfico de pizza**: Ilustra a proporção de clientes por gênero (homens e mulheres).

### Análise de Correlação

- Cálculo e impressão dos coeficientes de correlação de **Pearson** e **Spearman** entre `CreditScore` e `EstimatedSalary`.

##Como Executar o Projeto

1.  **Pré-requisitos**: Certifique-se de ter o Python instalado.
2.  **Instale as bibliotecas**:
    ```bash
    pip install pandas numpy matplotlib seaborn scipy
    ```
3.  **Baixe o conjunto de dados**:
    - Baixe o arquivo `Churn_Modelling.csv` do Kaggle e coloque-o na mesma pasta do seu script Python.
    - Você pode encontrar o dataset [aqui](https://www.kaggle.com/datasets/shrutimechlearn/churn-modelling).
4.  **Execute o script**:
    ```bash
    python seu_script.py
    ```
    
##Conclusões

Este projeto serve como uma base para uma análise de churn mais aprofundada. Os insights iniciais mostram a distribuição dos dados e algumas relações básicas entre as variáveis. As próximas etapas poderiam incluir a limpeza mais robusta dos dados, a criação de novas variáveis (feature engineering) e a construção de modelos de Machine Learning para prever quais clientes provavelmente farão churn.
