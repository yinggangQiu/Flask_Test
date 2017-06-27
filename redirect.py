from flask import Flask
from flask import redirect

app = Flask(__name__)
@app.route('/')
def index():
	return redirect('http://www.baidu.com')

if __name__ == '__main__':
	app.run(host='211.150.66.48',port=5000,debug=True)
