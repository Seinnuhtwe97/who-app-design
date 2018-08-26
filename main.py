from flask import Flask, render_template, url_for

myapp = Flask(__name__)

@myapp.route("/")
def hello():
    return render_template("index.html")


@myapp.route("/man")
def man():
    return render_template("man.html")


@myapp.route("/writer")
def writer():
    return render_template("writer.html")


@myapp.route("/actor")
def actor():
    return render_template("actor.html")


@myapp.route("/designer")
def designer():
return render_template("designer.html")
if __name__ == "__main__":
    myapp.route(Debug=True)
