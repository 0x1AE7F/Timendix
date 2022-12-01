from flask import Flask, request, render_template, redirect, session, url_for
import os
import db

path = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder=path+"/html")

app.secret_key = os.urandom(128)
email = ""

@app.route("/")
def show_schedule():
    print(url_for('static', filename='css/custom.css', _external=True))
    return "<p>This is going to be the schedule!</p>"

@app.route("/dashboard")
def dashboard():
    if 'username' in session:
        return render_template("dashboard.html", email = email, dashboard_selected=True)
    else:
        return redirect("/login")
@app.route("/dashboard/teachers")
def dashboard_teachers():
    if 'username' in session:
        return render_template("teachers.html", email = email, teachers_selected=True)
    else:
        return redirect("/login")
@app.route("/dashboard/classes")
def dashboard_classes():
    if 'username' in session:
        return render_template("classes.html", email = email, classes_selected=True)
    else:
        return redirect("/login")
@app.route("/dashboard/logs")
def dashboard_logs():
    if 'username' in session:
        return render_template("logs.html", email = email, logs_selected=True)
    else:
        return redirect("/login")
@app.route("/dashboard/settings")
def dashboard_settings():
    if 'username' in session:
        return render_template("settings.html", email=email, settings_selected=True)
    else:
        return redirect("/login")







@app.route("/test")
def test():
    return render_template("dashboard.html", email=email, dashboard_selected=True)









@app.route("/login")
def login():
    if db.user_exists(): return render_template("auth.html", title="Please log in to continue", btn_text="LOGIN")
    return render_template("auth.html", title="Please register to continue", btn_text="REGISTER")
@app.route("/login", methods=["POST"])
def api_login():
    global email
    email = request.form.get("email")
    password = request.form.get("password")
    if db.user_exists():
        if db.login_user(email=email, password=password):
            session['username'] = email
            return redirect("/dashboard")
        else:
            return render_template("auth.html", title="Please log in to continue", error_msg="Incorrect Login Credentials!", btn_text="LOGIN")
    else:
        if not db.register_user(email=email, password=password):
            return render_template("auth.html", title="Please register to continue", error_msg="Password must be atleast 8 Characters long!", btn_text="REGISTER")
        else:
            return redirect("login")
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")
    
    
if __name__ == "__main__":
    app.run()
