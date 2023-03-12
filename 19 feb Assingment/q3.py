# Q3. What is App routing in Flask? Why do we use app routes?

# App routing in Flask refers to the process of mapping URLs to Python functions or views. This is done using the @app.route() decorator, which is used to define routes for the Flask application.

# Routes are used in Flask to determine what function or view should be executed when a user visits a specific URL. For example, if we define a route for the URL /about, we can map that route to a Python function or view that will generate the content for the about page.

# Here is an example of defining a route in Flask:

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is the home page'

@app.route('/about')
def about():
    return 'This is the about page'

if __name__ == '__main__':
    app.run()
# In this example, we have defined two routes using the @app.route() decorator. The first route maps the root URL (/) to the home() function, which will return the string "This is the home page". The second route maps the URL /about to the about() function, which will return the string "This is the about page".

# We use app routes in Flask to define the URL structure of our web application and to determine which function or view should be executed for each URL. By using app routes, we can create a well-organized and structured web application that is easy to navigate and understand.