### Building Url Dynamically
## Variable Rule
### Jinja 2 Template Engine

### Jinja2 Template Engine
'''
{{  }} expressions to print output in html
{%...%} conditions, for loops
{#...#} this is for comments
'''

from flask import Flask,render_template,request, redirect, url_for
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST': # It is handling post request
        pass
        name=request.form['name']  
        return f'Hello {name}!'
    return render_template('form.html')  # It is handling Get request showing the form 

## Variable rule 
@app.route('/success/<int:score>')
def success(score):
    #return "The marks you got is "+ str(score)  # type cast the integer value to string to show it on webpage 

    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    return render_template('result.html',results=res)  # here we render the value to html page name as result.html


## Variable Rule
## For loops 
@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    
    exp={'score':score,"res":res}  # Here we are passing key value pair to html files

    return render_template('result1.html',results=exp)


## if condition
@app.route('/successif/<int:score>')
def successif(score):

    return render_template('result2.html',results=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html',results=score)


@app.route('/result',methods=['POST','GET'])
def result():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres',score=total_score)) # Here value is redirected to other url named as successres

if __name__=="__main__":
    app.run(debug=True)