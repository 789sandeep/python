# Q2. Create a simple Flask application to display ‘Hello World!!’. Attach the screenshot of the output in
# Jupyter Notebook.

# I'm sorry, as an AI language model, I do not have the capability to attach screenshots in Jupyter Notebook. However, I can provide you with the code to create a simple Flask application to display 
# from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!!'

if __name__ == '__main__':
    app.run()
# In this code, we import the Flask class from the flask module and create an instance of the Flask class called app. We then define a route with the @app.route() decorator that maps the root URL (/) to the hello_world() function. The hello_world() function simply returns the string "Hello World!!".

# Finally, we run the application with the app.run() method. When we run this code, we should see "Hello World!!" displayed in the browser when we navigate to http://localhost:5000/.
