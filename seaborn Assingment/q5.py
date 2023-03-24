# Que 5: Use the "iris" dataset from seaborn to plot a pair plot. Use the hue parameter for the "species" column
# of the iris dataset.
import seaborn as sns
ir=sns.load_dataset('iris')
print(ir)
sns.pairplot(ir,hue='species')