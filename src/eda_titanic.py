import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("outputs", exist_ok=True)

print("Carregando dataset Titanic...")
titanic = sns.load_dataset("titanic")

print("\nInformações gerais:\n ")
print(titanic.info())
print("\nValores nulos por coluna:\n ")
print(titanic.isnull().sum())

titanic['age'] = titanic['age'].fillna(titanic['age'].mean())
titanic['embarked'] = titanic['embarked'].fillna(titanic['embarked'].mode()[0])
titanic.dropna(subset=['deck'], inplace=True)

print("\nEstatisticas descritivas:\n")
print(titanic.describe(include='all'))

print("\nInsights iniciais:\n")
print(f"Total de passageiros: {len(titanic)}")
print(f"Taxa de sobrevivência: {titanic['survived'].mean()*100:.2f}%")
print(f"Média de idade: {titanic['age'].mean():.2f} anos")
print(f"Maior grupo de embarque: {titanic['embarked'].mode()[0]}")

sns.countplot(data=titanic, x='sex', hue='survived')
plt.title('Sobreviventes por Gênero')
plt.savefig("outputs/sobreviventes_por_genero.png")
plt.close()

# Gráfico 2
sns.histplot(titanic['age'], bins=20, kde=True)
plt.title('Distribuição das Idades')
plt.savefig("outputs/distribuicao_idades.png")
plt.close()

print("\n📊 Gráficos salvos na pasta 'outputs' com sucesso!")