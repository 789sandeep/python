# Q5. What function is used in Flask for URL Building? Write a Python code to demonstrate the working of the
# url_for() function.

# The url_for() function is used in Flask for URL building. This function generates a URL for the specified endpoint (i.e., view function) with the values of any specified arguments.

# Here's an example of how the url_for() function works in Flask:

from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is the home page'

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/contact')
def contact():
    return 'This is the contact page'

if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('home'))  # Output: '/'
        print(url_for('about'))  # Output: '/about'
        print(url_for('contact'))  # Output: '/contact'