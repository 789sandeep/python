# Que 2: Load the "fmri" dataset using the load_dataset function of seaborn. Plot a line plot using x ="timepoint" and y = "signal" for different events and regions.

import seaborn as sns
fm=sns.load_dataset('fmri')
sns.lineplot(x=fm.timepoint,y=fm.signal)
sns.lineplot(x=fm.event,y=fm.region)