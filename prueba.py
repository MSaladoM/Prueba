import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar datos
df = sns.load_dataset('iris')

# Vista general
print(df.head(), "\n")
print(df.info(), "\n")
print(df.describe(), "\n")
print(df['species'].value_counts(), "\n")
print(df['sepal_width'].mean())

# Visualizaciones
sns.pairplot(df, hue='species', diag_kind='kde')
plt.show()

plt.figure(figsize=(10,6))
sns.boxplot(data=df.drop('species', axis=1))
plt.title('Distribución de características')
plt.show()

plt.figure(figsize=(8,5))
sns.heatmap(df.drop('species', axis=1).corr(), annot=True, cmap='coolwarm')
plt.title('Matriz de correlación')
plt.show()