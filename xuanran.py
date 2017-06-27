from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
	return render_template('index.html')
@app.route('/user/<name>')
def user(name):
	return render_template('user.html',name=name)    #user.html在templates里

if __name__ == '__main__':
	app.run(host='211.150.66.48',port=5000,debug=True)

