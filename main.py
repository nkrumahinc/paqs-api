import requests
import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>HELLO</h1><p>Hello hello how low</p><p>With the lights out, it's less dangerous</p>"

app.run(host="0.0.0.0")