from flask import request, redirect, url_for, render_template, abort, Blueprint
from app.controllers import UserLogin, GetCurrentUsername, UserLogout

bp = Blueprint("users", __name__, template_folder="../templates", static_folder="../static")

@bp.route("/login2", methods=["GET", "POST"])
def Login():
    if request.method == "POST":
        if request.form:
            if "username" in request.form and "password" in request.form:
                username = request.form["username"]
                password = request.form["password"]
                if UserLogin(username,password):
                    return redirect(url_for("home.Index"))
                else:
                    return redirect(url_for("users.Login"))

        abort(400)
    username, loginAuth = GetCurrentUsername()
    return render_template("login2.html", username=username, login_auth=loginAuth)

#@app.route("/logout")
@bp.route("/logout")
def Logout():
    if UserLogout():
        return redirect(url_for("home.Index"))