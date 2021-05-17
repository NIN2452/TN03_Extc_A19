from flask import Flask, redirect,g,request, url_for, session, render_template
from flask_mysqldb import MySQL
from flask import flash
import os
import MySQLdb


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

# -------------------------------------------------------------------------------------------------------------------------

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

# -------------------------------------------------------------------------------------------------------------------------

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
				flash("Incorrect Password")
				return redirect(url_for("login"))
		except:
				flash("Invalid username")
				return redirect(url_for("login"))
	return render_template("login.html")


# redirecting after logging in
@app.route("/redirecting/<table>")
def redirecting(table):
    if table == "patient":
        return redirect("/pat_home")
    elif table == "doctor":
        return redirect("/doc_home")
    elif table == "receptionist":
        return redirect("/rep_home")
    elif table == "pathologist":
        return redirect("/path_home")
    else:
        return "please login"

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
		flash("You have logged out successfully")
		return redirect(url_for("login"))
	return "you are already logged out"


# -------------------------------------------------------------------------------------------------------------------------

# Sign Up Patient
@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        email=request.form['email']
        fname=request.form['fname']
        lname=request.form['lname']
        gender=request.form['gender']
        dob=request.form['birthday']
        phone=request.form['phone']
        address=request.form['add']
        city=request.form['city']
        state=request.form['state']
        country=request.form['country']
        relname=request.form['relaname']
        relaphone=request.form['relaphone']
        pswd=request.form['psw']
        curser = db.connection.cursor()
        query = f"insert into patient(p_fname, p_lname,P_email, p_add, p_city, p_state, p_country, p_phone, p_gend,p_dob, p_relaname, p_relaphone) values('{fname}','{lname}','{email}','{address}','{city}','{state}','{country}',{phone},'{gender}','{dob}','{relname}',{relaphone})"
        curser.execute(query)
        db.connection.commit()
        query2=f"insert into login_patient(user_password) values('{pswd}')"
        curser.execute(query2)
        db.connection.commit()
        curser.close()
        return "registered successfully"
    else:
        return render_template("signup.html")

#Doctor Signup
@app.route("/signup_doc", methods=["POST", "GET"])
def signup_doc():
    if request.method=='POST':
        email=request.form['email']
        fname=request.form['fname']
        lname=request.form['lname']
        gender=request.form['gender']
        dob=request.form['birthday']
        phone=request.form['phone']
        address=request.form['add']
        city=request.form['city']
        state=request.form['state']
        country=request.form['country']
        degree=request.form['degree']
        specs=request.form['specialization']
        visiting=request.form['visiting']
        pswd=request.form['pass']
        curser = db.connection.cursor()
        query=f"insert into doctor(dr_fname, dr_lname, dr_email, dr_add, dr_city, dr_state, dr_country, dr_phone, dr_gend, dr_dob, dr_degree, dr_specializatn, dr_visiting) values('{fname}','{lname}','{email}','{address}','{city}','{state}','{country}',{phone},'{gender}','{dob}','{degree}','{specs}','{visiting}')"
        curser.execute(query)
        db.connection.commit()
        query2=f"insert into login_doctor(user_password) values('{pswd}')"
        curser.execute(query2)
        db.connection.commit()
        curser.close()
        return "registered successfully"
    else:
        return render_template("signup_doc.html")

	
@app.route("/signup_patho", methods=["POST", "GET"])
def signup_patho():
    if request.method=='POST':
        labname=request.form['labname']
        email=request.form['email']
        phone=request.form['phone']
        add=request.form['add']
        city=request.form['city']
        state=request.form['state']
        country=request.form['country']
        pswd=request.form['psw']
        u=request.form.getlist('utils')
        util=",".join(u)
        utils=util+", etc."
        curser = db.connection.cursor()
        query=f"insert into pathologist(path_name,path_email,path_add,Path_city,path_state,path_country, path_phone,Path_util) values('{labname}','{email}','{add}','{city}','{state}','{country}',{phone},'{utils}')"
        curser.execute(query)
        db.connection.commit()
        query2=f"insert into login_pathologist(user_password) values('{pswd}')"
        curser.execute(query2)
        db.connection.commit()
        curser.close()
        return "registered successfully"
    else:
        return render_template("signup_patho.html")

@app.route("/signup_recep", methods=["POST", "GET"])
def signup_recep():
    if request.method=='POST':
        hname=request.form['hname']
        email=request.form['email']
        phone=request.form['phone']
        add=request.form['add']
        city=request.form['city']
        state=request.form['state']
        country=request.form['country']
        pswd=request.form['psw']
        curser = db.connection.cursor()
        query=f"insert into receptionist(hos_name,rec_email,hos_add,hos_city,hos_state,hos_country,rec_phone) values('{hname}','{email}','{add}','{city}','{state}','{country}',{phone})"
        curser.execute(query)
        db.connection.commit()
        query2=f"insert into login_receptionist(user_password) values('{pswd}')"
        curser.execute(query2)
        db.connection.commit()
        curser.close()
        return "registered successfully"
    else:
	    return render_template("signup_recep.html")

# -------------------------------------------------------------------------------------------------------------------------

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

# Doctor add patient
@app.route("/doc_addpat", methods=["POST", "GET"])
def doc_addpat():
    if g.user:
        if request.method == "POST":
            ses_num=request.form["ses_num"]
            pat_id = request.form["pid"]
            prob = request.form["prob"]
            path_id=request.form["pathid"]
            curser = db.connection.cursor()
            query = f"insert into session(ses_num, p_id, dr_id, path_id, problem, status) values({ses_num}, {pat_id}, {g.user}, {path_id}, '{prob}', 'Active');"
            curser.execute(query)
            db.connection.commit()
            curser.close()
            return redirect(url_for("doc_patlist"))
        else:
            curser = db.connection.cursor()
            query = f"select * from doctor where dr_id={g.user}"
            result = curser.execute(query)
            userdetail = curser.fetchall()
            return render_template("doc_addpat.html", userinfo=userdetail)
    return "please login first"

# doctor patient list
@app.route("/doc_patlist")
def doc_patlist():
    if g.user:
        curser = db.connection.cursor()
        query = f"select distinct p.p_fname,p.p_lname,p.p_phone,p.p_email,p.p_add from patient p, session s,doctor d where p.p_id=s.p_id and s.dr_id=d.dr_id and d.dr_id={g.user}"
        result = curser.execute(query)
        output = curser.fetchall()
        return render_template("doc_patlist.html", userinfo=output)
    return "please login first"

# Doctor appointments
@app.route("/doc_appoint")
def doc_appoint():
    if g.user:
        curser = db.connection.cursor()
        query = f"select distinct p.p_fname,p.p_lname,p.p_phone,p.p_email,s.problem, a.appoint_date,a.appoint_time,s.status from patient p, session s,doctor d, appointment a where p.p_id=s.p_id and s.dr_id=d.dr_id and d.dr_id=a.dr_id and d.dr_id={g.user} order by 6,7"
        result = curser.execute(query)
        userdetail = curser.fetchall()
        return render_template("doc_appoint.html", appointments=userdetail)
    return "please login first"

# Doctor session
@app.route("/doc_session")
def doc_session():
    if g.user:
        curser = db.connection.cursor()
        query = f"select distinct p.p_fname,p.p_lname,p.p_phone,p.p_email,s.problem,s.status from patient p, session s,doctor d where p.p_id=s.p_id and s.dr_id=d.dr_id and d.dr_id={g.user}"
        result = curser.execute(query)
        userdetail = curser.fetchall()
        return render_template("doc_session.html", sess=userdetail)
    return "please login first"



# -------------------------------------------------------------------------------------------------------------------------

# PATIENT

# patient home page
@app.route("/pat_home")
def pat_home():
    if g.user:
        curser = db.connection.cursor()
        query = f"select * from patient where p_id={g.user}"
        result = curser.execute(query)
        userdetail = curser.fetchall()
        return render_template("pat_home.html", userinfo=userdetail)
    return "please login first"

# patient  profile page
@app.route("/pat_prof")
def pat_prof():
    if g.user:
        curser = db.connection.cursor()
        query = f"select * from patient where p_id={g.user}"
        result = curser.execute(query)
        userdetail = curser.fetchall()
        return render_template("pat_prof.html", userinfo=userdetail)
    return "please login first"


# patient session
@app.route("/pat_session")
def pat_session():
    if g.user:
        curser = db.connection.cursor()
        query = f"select d.dr_fname,d.dr_lname,d.dr_phone,s.problem,s.ses_num,s.status from patient p, session s,doctor d where p.p_id=s.p_id and s.dr_id=d.dr_id and p.p_id={g.user}"
        result = curser.execute(query)
        userdetail = curser.fetchall()
        return render_template("pat_session.html", userinfo=userdetail)
    return "please login first"


# patient appointments
@app.route("/pat_appoint")
def pat_appoint():
    if g.user:
        curser = db.connection.cursor()
        query = f"select distinct  d.dr_fname,d.dr_lname,d.dr_phone,d.dr_email, a.appoint_date,a.appoint_time from patient p, doctor d, appointment a  where p.p_id=a.p_id  and d.dr_id=a.dr_id and p.p_id={g.user}"
        result = curser.execute(query)
        userdetail = curser.fetchall()
        return render_template("pat_appoint.html", userinfo=userdetail)
    return "please login first"

#patient report
@app.route("/pat_report")
def pat_report():
    if g.user:
        curser = db.connection.cursor()
        query = f"select p_fname, p_lname, test_name, date from patient pat,report r where pat.p_id=r.p_id and pat.p_id={g.user}"
        result = curser.execute(query)
        userdetail = curser.fetchall()
        return render_template("pat_report.html", userinfo=userdetail)
    return "Please Login First"

#Diet and Exercise
@app.route("/pat_plan")
def pat_plan():
    if g.user:
        curser = db.connection.cursor()
        query = f"select p_fname, p_lname, Dietitian_Name, food from patient pat, diet d where pat.p_id=d.pat_id and pat.p_id={g.user}"
        result = curser.execute(query)
        userdetail = curser.fetchall()
        return render_template("pat_plan.html", userinfo=userdetail)
    return "Please Login First"

#Prescription
@app.route("/pat_med")
def pat_med():
    if g.user:
        curser = db.connection.cursor()
        query = f"select p_fname, p_lname, disease, Drug_name, Date, Time from patient pat, prescription pres where pat.p_id=pres.pat_id and pat.p_id={g.user}"
        result = curser.execute(query)
        userdetail = curser.fetchall()
        return render_template("pat_med.html", userinfo=userdetail)
    return "Please Login First"

# -------------------------------------------------------------------------------------------------------------------------


# PATHOLOGIST

#pathologist home
@app.route("/path_home")
def path_home():
    if g.user:
        curser = db.connection.cursor()
        query = f"select * from pathologist where path_id={g.user}"
        result = curser.execute(query)
        userdetail = curser.fetchall()
        return render_template("path_home.html", userinfo=userdetail)
    return "please login first"

#pathologist profile
@app.route("/path_prof")
def path_prof():
    if g.user:
        curser = db.connection.cursor()
        query = f"select * from pathologist where path_id={g.user}"
        result = curser.execute(query)
        userdetail = curser.fetchall()
        return render_template("path_prof.html", userinfo=userdetail)
    return "please login first"

#pathologist add patient
@app.route("/path_addpat")
def path_addpat():
    if g.user:
        curser = db.connection.cursor()
        query = f"select * from pathologist where path_id={g.user}"
        result = curser.execute(query)
        userdetail = curser.fetchall()
        return render_template("path_addpat.html", userinfo=userdetail)
    return "please login first"

@app.route("/path_addrep")
def path_addrep():
	return render_template("path_addrep.html")

#pathologist patient list
@app.route("/path_patlist")
def path_patlist():
    if g.user:
        curser = db.connection.cursor()
        query = f"select distinct p.p_fname,p.p_lname,p.p_phone,p.p_email,p.p_add from patient p, session s, pathologist pa where p.p_id=s.p_id and s.path_id=pa.path_id and pa.path_id={g.user}"
        result = curser.execute(query)
        userdetail = curser.fetchall()
        return render_template("path_patlist.html", userinfo=userdetail)
    return "please login first"

# -------------------------------------------------------------------------------------------------------------------------

# RECEPTIONIST

#receptionist home
@app.route("/rep_home")
def rep_home():
    if g.user:
        curser = db.connection.cursor()
        query = f"select * from receptionist where rec_id={g.user}"
        result = curser.execute(query)
        userdetail = curser.fetchall()
        return render_template("rep_home.html", userinfo=userdetail)
    return "please login first"


#receptionist profile
@app.route("/rep_prof")
def rep_prof():
    if g.user:
        curser = db.connection.cursor()
        query = f"select * from receptionist where rec_id={g.user}"
        result = curser.execute(query)
        userdetail = curser.fetchall()
        return render_template("rep_prof.html", userinfo=userdetail)
    return "please login first"

@app.route("/rep_addpat")
def rep_addpat():
	return render_template("rep_addpat.html")

#receptionist appointments
@app.route("/rep_appoint")
def rep_appoint():
    if g.user:
        curser = db.connection.cursor()
        query = f"select d.dr_fname, d.dr_lname, p.p_fname, p.p_lname, a.appoint_date,a.appoint_time from appointment a,  doctor d, recep_doc_rel rdr, patient p where a.dr_id=d.dr_id and d.dr_id=rdr.dr_id and a.dr_id=d.dr_id and p.p_id=a.p_id and rdr.rec_id={g.user}"
        result = curser.execute(query)
        userdetail = curser.fetchall()
        return render_template("rep_appoint.html", userinfo=userdetail)
    return "please login first"

# -------------------------------------------------------------------------------------------------------------------------



if __name__ == "__main__":
	app.run(debug = True)