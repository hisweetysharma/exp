from flask import Flask, render_template


app = Flask(__name__,template_folder='template')


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template('Home.html')

@app.route('/date')
def xdate():
	"""Return a friendly HTTP greeting."""
	x = time.strftime("%d/%m/%Y")
	
	return x


@app.route('/time')
def xtime():
	"""Time"""
	return 'time'



if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)
