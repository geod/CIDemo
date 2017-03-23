from flask import Flask
import flask
from wraparoundcounter import WrapAroundCounter


app = Flask(__name__)
app.debug = True

wac = WrapAroundCounter(10)

@app.route('/')
def hello_world():
    return 'Hello, World!!'


@app.route('/counter/<argument>')
def counter(argument):
    #incremented = wac.increment(int(argument))
    incremented = wac.increment(argument)
    return flask.jsonify({'incremented' : incremented})

if __name__ == "__main__":
    app.run()
