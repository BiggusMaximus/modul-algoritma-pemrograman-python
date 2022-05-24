import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


pasar = pd.read_csv('Data Marketing.csv')

fig, axis = plt.subplots(2, 2, figsize=(12, 7))
sns.boxplot(y='Penghasilan', x='Nama Hari', data=pasar, ax=axis[0, 0])
sns.lineplot(y='Penghasilan', x='Nama Hari', data=pasar, ax=axis[0, 1])
sns.scatterplot(y='Penghasilan', x='Nama Hari', data=pasar, ax=axis[1, 0])
sns.barplot(y='Penghasilan', x='Nama Hari', data=pasar, ax=axis[1, 1])
plt.show()