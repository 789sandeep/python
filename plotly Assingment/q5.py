# Q5. What is Distplot? Using Plotly express, plot a distplot.

# Distplot is a visualization tool that combines a histogram with a kernel density estimate (KDE) plot. It provides a way to visualize the distribution of a single numerical variable, by showing the frequency of values in bins and the density of values across the range of the variable

import plotly.express as px
tips = px.data.tips()
fig = px.histogram(tips, x="total_bill", nbins=20, marginal="rug", opacity=0.7, color="sex")
fig.update_layout(title="Distplot of Total Bill by Gender")
fig.show()


