from flask import Flask
app = Flask(__name__)
@app.route('/user/<path:name>')
def user(name):
	return '<h1>Hello,%s</h1>' % name

if __name__ == '__main__':
	app.run(host='211.150.66.48',port=5000,debug=True)
