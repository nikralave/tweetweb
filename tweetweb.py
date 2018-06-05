import os
from flask import Flask, redirect, render_template, request
from search import search


app = Flask(__name__)

@app.route("/")
def get_index():
     return render_template("index.html")
     

@app.route("/results")
def get_results():
    topic = request.args.get("search")
    results = search(topic, 10)
    return render_template("results.html", tweets=results)

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)