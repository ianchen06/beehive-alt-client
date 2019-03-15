import json

from flask import Flask, render_template

app = Flask(__name__)
db = json.load(open('./data.json'))

@app.route("/")
def hello():
    return render_template('index.html', title="HOME", products=db[:10])
