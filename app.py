from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("hello.html")

@app.route('/about')
def about():
    return render_template("by.html")





