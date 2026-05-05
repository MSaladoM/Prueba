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


print('Soy bien chida!!!!!')
