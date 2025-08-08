from flask import Flask, request, render_template
from util.harvester import searchRecords
import asyncio

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def home():
    if request.method == 'POST':
        term = request.form.get("term")
        numResults = request.form.get("numResults")
        records = searchRecords(request.form.get("term"), request.form.get("numResults"))
        return render_template("searchPage.html", results = records, term = term,  numResults = numResults)
    return render_template("searchPage.html", results = [], term = "business", numResults = "5")

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()