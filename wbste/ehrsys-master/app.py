from flask import Flask, redirect, url_for, render_template

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

# DOCTOR

@app.route("/doc_home")
def doc_home():
	return render_template("doc_home.html")

@app.route("/doc_prof")
def doc_prof():
	return render_template("doc_prof.html")

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