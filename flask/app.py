from flask import Flask
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/") # Maps the root URL ("/") to this function
def welcome():
    return "Welcome to this best Flask course.This should be an amazing course"

@app.route("/index")
def index():
    return "Welcome to the index page"

# this is the starting point of the entire app or any .py file
if __name__=="__main__":
    app.run(debug=True) # debug=Trure will start the server each time while saving the web page