# Que 4: Use the "diamonds" dataset from seaborn to plot a histogram for the 'price' column. Use the hue parameter for the 'cut' column of the diamonds dataset.

import seaborn as sns
dia=sns.load_dataset('diamonds')
sns.relplot(x=dia.table,y=dia.color ,data=dia, hue='cut')