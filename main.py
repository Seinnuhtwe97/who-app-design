from flask import Flask, render_template

app = Flask(__name__)
@myapp.route("/index")
def index():
    return render_template("index.html")
	
@myapp.route("/political")
def political():
		return render_template("political.html")

@myapp.route("/man")
def man():
    return render_template("man.html")

@myapp.route("/writer")
def writer():
    return render_template("writer.html")

@myapp.route("/actor")
def actor():
    return render_template("actor.htm")

@myapp.route("/designer")
def designer():
    return render_template("designer.html")

if __name__ == "__main__":
    app.route(Debug=True)
