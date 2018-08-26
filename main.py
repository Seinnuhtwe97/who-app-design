from flask import Flask, render_template, url_for

myapp = Flask(__name__)

@myapp.route("/")
def home():
    return render_template("index.html")


@myapp.route("/")
def home():
    return render_template("political.html")



@myapp.route("/")
def home():
    return render_template("man.html")


@myapp.route("/")
def home():
    return render_template("writer.html")


@myapp.route("/")
def home():
    return render_template("actor.html")


@myapp.route("/")
def home():
    return render_template("designer.html")

if __name__ =="__main__":
    myapp.run(debug=True)
