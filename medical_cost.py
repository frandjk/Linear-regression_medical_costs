import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['figure.figsize'] = [8, 8]
plt.rcParams['font.size'] = 14
plt.rcParams['font.weight'] = 'bold'
plt.style.use('seaborn-whitegrid')

df = pd.read_csv('insurance.csv')
df.head(10)

sns.lmplot(x = 'bmi', y = 'charges', data = df, aspect = 2, height = 6)
plt.xlabel('Body Mass Index')
plt.ylabel('Insurance Charges')
plt.title('Charge vs. BMI')

df.describe()
df.isnull().sum()


f = plt.figure(figsize = (14,6))
ax = f.add_subplot(121)
sns.scatterplot(x = 'age',y='charges',data = df,palette = 'magma',hue = 'smoker',ax=ax)
ax.set_title('Scatter plot of Charges vs age')

ax = f.add_subplot(122)
sns.scatterplot(x = 'bmi',y = 'charges',data = df,palette = 'viridis',hue = 'smoker')
ax.set_title('Scatter plot of Charges vs BMI')

