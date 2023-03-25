# Q1. Load the "titanic" dataset using the load_dataset function of seaborn. Use Plotly express to plot a scatter plot for age and fare columns in the titanic dataset.

import plotly.graph_objects as go
import seaborn as sns
fig=go.Figure()
ti=sns.load_dataset('titanic')
fig.add_trace(go.Scatter(x=ti.age,y=ti.fare,mode='markers'))
fig.show()