from flask import Flask,render_template
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)


@app.route("/") # Maps the root URL ("/") to this function
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index")
def index():
    return render_template('index.html') # used to render the index html page , it first goes to folder name of templates of current directory and search for .html file 


@app.route('/about') # name of route must be unique and by defalut it is HTPP get request
def about():
    return render_template('about.html')


# this is the starting point of the entire app or any .py file
if __name__=="__main__":
    app.run(debug=True) # debug=Trure will start the server each time while saving the web page