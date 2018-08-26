from flask import Flask, render_template

app = Flask(__name__)
@app.route("/index")
def index():
    return render_template("index.html")
	
@app.route("/political")
def political():
		return render_template("political.html")

@app.route("/man")
def man():
    return render_template("man.html")

@app.route("/writer")
def writer():
    return render_template("writer.html")

@app.route("/actor")
def actor():
    return render_template("actor.htm")

@app.route("/designer")
def designer():
    return render_template("designer.html")

if __name__ == "__main__":
    app.route(Debug=True)
