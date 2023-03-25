# Q4. Using the iris dataset in the Plotly library, Plot a scatter matrix plot, using the "species" column for the color parameter.
import plotly.express as px
iris = px.data.iris()
fig = px.scatter_matrix(iris, dimensions=["sepal_length","sepal_width", "petal_length", "petal_width"], color="species")
fig.show()
