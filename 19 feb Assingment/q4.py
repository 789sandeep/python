# Q4. Create a “/welcome” route to display the welcome message “Welcome to ABC Corporation” and a “/”
# route to show the following details:
# Company Name: ABC Corporation
# Location: India
# Contact Detail: 999-999-9999


# Sure! Here's an example of how you can create two routes /welcome and / in Flask to display the welcome message and company details respectively:

from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return 'Welcome to ABC Corporation'

@app.route('/')
def company_details():
    return 'Company Name: ABC Corporation<br>Location: India<br>Contact Detail: 999-999-9999'

if __name__ == '__main__':
    app.run()
# In this example, we define two routes using the @app.route() decorator. The first route maps the URL /welcome to the welcome() function, which will return the string "Welcome to ABC Corporation". The second route maps the root URL (/) to the company_details() function, which will return the company details in the format of an HTML string.

# When we run this code, we can visit http://localhost:5000/welcome to see the welcome message, and http://localhost:5000/ to see the company details. The output in the browser for the /welcome route will be "Welcome to ABC Corporation" and the output for the / route will be:

# yaml
# Copy code
# Company Name: ABC Corporation
# Location: India
# Contact Detail: 999-999-9999
# Note that we use the <br> HTML tag to add line breaks between each detail in the company_details function. This makes the output easier to read in the browser.