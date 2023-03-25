# Q3. Using the tips dataset in the Plotly library, Plot a histogram for x= "sex" and y="total_bill" column in the tips dataset. Also, use the "smoker" column with the pattern_shape parameter and the "day" column with the color parameter.

import plotly.express as px
tips = px.data.tips()
fig = px.histogram(tips, x="sex", y="total_bill", color="day", pattern_shape="smoker")
fig.show()
