import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, spearmanr


df = pd.read_csv('Churn_Modelling.csv', index_col = 0)

#Análise exploratória dos dados
print(df.head())
print(df.columns)
print(df.info())
print(df.describe(include='object'))
print(df.shape)

#corrigindo tipo da variável
df['CustomerId'] = df['CustomerId'].astype(str)
df['IsActiveMember'] = df['IsActiveMember'].astype(str)
df['Exited'] = df['Exited'].astype(str)
df['HasCrCard'] = df['HasCrCard'].astype(str)

print(f'Nova classificação do tipo de variável: {df.info()}')

print(df['Gender'].value_counts())
print(df['Geography'].value_counts())
print(df['Exited'].value_counts())
print(df['IsActiveMember'].value_counts())
print(df['HasCrCard'].value_counts())



print(df['Age'].mean())

idade_homens = df[df['Gender'] == 'Male'] ['Age']
idade_mulheres = df[df['Gender'] == 'Female'] ['Age']

print(idade_homens.mean())
print(idade_mulheres.mean())

salario_homens = df[df['Gender'] == 'Male'] ['EstimatedSalary']
salario_mulheres = df[df['Gender'] == 'Female'] ['EstimatedSalary']

print(salario_homens.mean())
print(salario_mulheres.mean())

#gráfico = relação entre o saldo estimado e o escore de crédito
#gráfico de dispersão - avalia relação entre 2 variáveis numéricas
sns.set_style("white") #fundo branco sem linhas cinza
plt.figure(figsize=(10,10))
g = sns.scatterplot(x=df['Balance'], y=df['CreditScore'], data=df)
plt.title("Relação entre o saldo atual e o escore de crédito")
plt.xlabel("Saldo Atual")
plt.ylabel("Escore de Crédito")
plt.show()

#Análise de Correlação entre variáveis
coef_pearson, p_valor = pearsonr(df['CreditScore'], df['EstimatedSalary'])
coef_sperman, p_valor = spearmanr(df['CreditScore'], df['EstimatedSalary'])
print(coef_pearson)
print(p_valor)
print(coef_sperman)
print(p_valor)

#print(df['EstimatedSalary'].isnull().sum() )
gender_counts = df['Gender'].value_counts()
sizes = gender_counts.values
labels = gender_counts.index

#gráfico de pizza - prop de homens e mulheres
fig, ax = plt.subplots()
ax.pie(sizes,
       labels=labels,
       autopct='%1.1f%%',
       shadow = True,
       startangle = 90)
ax.axis('equal')
plt.title('Proporção de homens e mulheres com contas criadas no banco')
plt.show()





