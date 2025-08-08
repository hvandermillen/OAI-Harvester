from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def home():
    if request.method == 'POST':
        return render_template("searchPage.html", results = ["a","b","c"])
    return render_template("searchPage.html", results = [])

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()