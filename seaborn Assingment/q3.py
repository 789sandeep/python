# Que 3: Load the "titanic" dataset using the load_dataset function of seaborn. Plot two box plots using x =
# 'pclass', y = 'age' and y = 'fare'.
import seaborn as sns
ti=sns.load_dataset('titanic')
ti.head()
sns.boxplot(x =ti.pclass, y =ti.age )
sns.boxplot(x =ti.pclass,  y = ti.fare)