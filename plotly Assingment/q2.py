# Q2. Using the tips dataset in the Plotly library, plot a box plot using Plotly express.

import plotly.graph_objects as go
import seaborn as sns
tip=sns.load_dataset('tips')
fig=go.Figure(data=[go.Box(x=tip.total_bill)])
fig.show()