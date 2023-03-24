# Que 6: Use the "flights" dataset from seaborn to plot a heatmap.
import seaborn as sns
import matplotlib.pyplot as plt
fl=sns.load_dataset('flights')
print(fl)
fl1 = fl.pivot('month', 'year', 'passengers')
sns.heatmap(fl1)
plt.show()