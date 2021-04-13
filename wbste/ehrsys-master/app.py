from flask import Flask, redirect,g,request, url_for, session, render_template
#from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
import os

# initialization of flask
app = Flask(__name__)

# for using flak-session
app.secret_key = os.urandom(24)

# adding encryption key
app.secret_key = os.urandom(24)

# comfiguring database values
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "newuser"
app.config["MYSQL_PASSWORD"] = "Ninad2452"
app.config["MYSQL_DB"] = "ehrsystem"

# initializing database as db
db = MySQL(app)


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


# login page
@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		session.pop("user", None)
		uid = request.form["userid"]
		pswd = request.form["pass"]
		table = request.form["table"]
		cur = db.connection.cursor()
		query = f"select * from login_{table} where user_id={uid}"
		cur.execute(query)
		usernamess = cur.fetchall()
		try:
			if usernamess[0][1] == pswd:
				session["user"] = request.form["userid"]
				return redirect(url_for("redirecting", table=table))
			else:
				return "password incorrect"
		except Exception as e:
				return("invalid username",e)
	return render_template("login.html")


# redirecting after logging in
@app.route("/redirecting/<table>")
def redirecting(table):
    if table == "patient":
        return redirect("/pat_home")
    elif table == "doctor":
        return redirect("/doc_home")
    elif table == "receptionist":
        return redirect("/rep_home.html")
    elif table == "pathologist":
        return redirect("/path_home.html")
    else:
        return "please login"


# Sign Up
@app.route("/signup")
def signup():
    return render_template("signup.html")

# checking and initialising user
@app.before_request
def before_request():
    g.user = None

    if "user" in session:
        g.user = session["user"]


# logout
@app.route("/logout")
def logout():
    if g.user:
        session.pop("user", None)
        return redirect(url_for("login"))
    return "you are already logged out"


# -------------------------------------------------------------------------------------------------------------------------

@app.route("/signup_doc")
def signup_doc():
	return render_template("signup_doc.html")

@app.route("/signup_patho")
def signup_patho():
	return render_template("signup_patho.html")

@app.route("/signup_recep")
def signup_recep():
	return render_template("signup_recep.html")

# DOCTOR

# Doctor's home
@app.route("/doc_home")
def doc_home():
    if g.user:
        curser = db.connection.cursor()
        query = f"select * from doctor where dr_id={g.user}"
        result = curser.execute(query)
        userdetail = curser.fetchall()
        return render_template("doc_home.html", userinfo=userdetail)
    return "please login first"

# Doctor Profile
@app.route("/doc_prof")
def doc_prof():
    if g.user:
        curser = db.connection.cursor()
        query = f"select * from doctor where dr_id={g.user}"
        result = curser.execute(query)
        userdetail = curser.fetchall()
        return render_template("doc_prof.html", userinfo=userdetail)
    return "please login first"


# -------------------------------------------------------------------------------------------------------------------------


@app.route("/doc_addpat")
def doc_addpat():
	return render_template("doc_addpat.html")

@app.route("/doc_patlist")
def doc_patlist():
	return render_template("doc_patlist.html")

@app.route("/doc_appoint")
def doc_appoint():
	return render_template("doc_appoint.html")

@app.route("/doc_session")
def doc_session():
	return render_template("doc_session.html")

# PATIENT

@app.route("/pat_home")
def pat_home():
	return render_template("pat_home.html")

@app.route("/pat_prof")
def pat_prof():
	return render_template("pat_prof.html")

@app.route("/pat_session")
def pat_session():
	return render_template("pat_session.html")

@app.route("/pat_appoint")
def pat_appoint():
	return render_template("pat_appoint.html")

@app.route("/pat_report")
def pat_report():
	return render_template("pat_report.html")

@app.route("/pat_plan")
def pat_plan():
	return render_template("pat_plan.html")

@app.route("/pat_med")
def pat_med():
	return render_template("pat_med.html")

# PATHOLOGIST
@app.route("/path_home")
def path_home():
	return render_template("path_home.html")

@app.route("/path_prof")
def path_prof():
	return render_template("path_prof.html")

@app.route("/path_addpat")
def path_addpat():
	return render_template("path_addpat.html")

@app.route("/path_addrep")
def path_addrep():
	return render_template("path_addrep.html")

@app.route("/path_patlist")
def path_patlist():
	return render_template("path_patlist.html")

# RECEPTIONIST

@app.route("/rep_home")
def rep_home():
	return render_template("rep_home.html")

@app.route("/rep_prof")
def rep_prof():
	return render_template("rep_prof.html")

@app.route("/rep_addpat")
def rep_addpat():
	return render_template("rep_addpat.html")

@app.route("/rep_appoint")
def rep_appoint():
	return render_template("rep_appoint.html")



if __name__ == "__main__":
	app.run(debug = True)