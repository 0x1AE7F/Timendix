from flask import Flask, request, render_template, redirect, session, url_for
import os
import setup
import configparser
import translationManager
import db

# Run the check before importing db and translationManager to prevent errors when other these try to load empty configs
if not os.path.exists(os.path.abspath(os.path.dirname(__file__)) + "/databases"):
    setup.setup()

app = Flask(__name__, template_folder=os.path.abspath(
    os.path.dirname(__file__))+"/html")
config = configparser.ConfigParser()
config.read("app_config.ini")
app.secret_key = config['GENERAL']['flask_secret']
app.jinja_env.globals.update(init_translator=translationManager.init_translator)

translations = translationManager.init_translator()


@app.route("/")
def show_schedule():
    print(url_for('static', filename='css/custom.css', _external=True))
    return "<p>This is going to be the schedule!</p>"


@app.route("/dashboard")
def dashboard():
    if 'username' in session:
        return render_template("dashboard.html", email=email, dashboard_selected=True)
    else:
        return redirect("/login")


@app.route("/dashboard/teachers")
def dashboard_teachers():
    if 'username' in session:
        return render_template("teachers.html", email=email, teachers_selected=True)
    else:
        return redirect("/login")


@app.route("/dashboard/classes")
def dashboard_classes():
    if 'username' in session:
        return render_template("classes.html", email=email, classes_selected=True)
    else:
        return redirect("/login")


@app.route("/dashboard/logs")
def dashboard_logs():
    if 'username' in session:
        return render_template("logs.html", email=email, logs_selected=True)
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
    if db.user_exists():
        return render_template("auth.html")
    return render_template("auth.html", registration=True)


@app.route("/login", methods=["POST"])
def api_login():
    global email
    email = request.form.get("email")
    password = request.form.get("password")
    if db.user_exists():
        if db.login_user(email=email, password=password):
            session['username'] = email
            return redirect("/dashboard")
        return render_template("auth.html", wrong_password=True)
    if not db.register_user(email=email, password=password):
        return render_template("auth.html", registration=True, short_password=True)
    return redirect("login")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


app.run()
