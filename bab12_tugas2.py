import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pasar = pd.read_csv('Data Marketing.csv')
x = pasar['Penghasilan'].array
mean = pasar['Penghasilan'].mean()
median = pasar['Penghasilan'].median()

plt.axvline(mean, color='k', linewidth=4, linestyle='--')
plt.axvline(median, color='r', linewidth=4, linestyle='--')
sns.distplot(x)

plt.show
