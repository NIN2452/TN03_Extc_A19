from flask import Flask, redirect, url_for, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("intro.html")

@app.route("/about")
def about():
	return render_template("about-us.html")

@app.route("/contact")
def contact():
	return render_template("contact.html")

@app.route("/services_patho")
def services_patho():
	return render_template("services_patho.html")

@app.route("/services_doc")
def services_doc():
	return render_template("services_doc.html")

@app.route("/services_recep")
def services_recep():
	return render_template("services_recep.html")

@app.route("/services_pat")
def services_pat():
	return render_template("services_pat.html")


@app.route("/login")
def login():
	return render_template("login.html")


@app.route("/signup")
def signup():
	return render_template("signup.html")

@app.route("/signup_doc")
def signup_doc():
	return render_template("signup_doc.html")

@app.route("/signup_patho")
def signup_patho():
	return render_template("signup_patho.html")

@app.route("/signup_recep")
def signup_recep():
	return render_template("signup_recep.html")



if __name__ == "__main__":
	app.run(debug = True)