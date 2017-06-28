from flask import Flask,session,redirect,url_for,flash
from flask import render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route("/hello")
def index():
   user = {'nickname':'QYG'}
   posts = [
       {
           'author':{'nickname':'John'},
           'body':'Beautiful day in Portland'
       },
       {
           'author':{'nickname':'Susan'},
           'body':'The Avengers movie was so cool!'
       }
   ]
   return render_template('index.html',
                          title='home',
                          user=user,
                          posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
