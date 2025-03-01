from flask import request, redirect, url_for, render_template, abort, Blueprint
from app.controllers import SaveContactRequest, GetCurrentUsername, GetContactList

bp = Blueprint("contacts", __name__, template_folder="../templates", static_folder="../static")

@bp.route("/contact", methods=["GET", "POST"])
def Contact():
    if request.method == "POST":
        if request.form:
            name = request.form.get("name")
            email = request.form.get("email")
            category = request.form.get("category")
            priority = request.form.get("priority")
            message = request.form.get("message")
            SaveContactRequest(name, email, category, priority, message)
            return redirect(url_for("contacts.Contact"))
    username, loginAuth = GetCurrentUsername()
    return render_template("contact.html",username=username, login_auth=loginAuth)

@bp.route("/contactlist")
def ContactList():
    username, loginAuth = GetCurrentUsername()
    contactList = GetContactList()
    return render_template("contact_list.html",username=username, login_auth=loginAuth, contactList=contactList)