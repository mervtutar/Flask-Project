from flask import Flask
from .controllers import MySessionInterface
from .views import home, users, contacts

# duruma göre farklı app ler oluşturup import edebiliriz
def create_app():
    app = Flask(__name__, template_folder="templates",static_folder="static")
    app.config.from_pyfile("config.py")
    #app.secret_key = "secret key"  # bu key ile session aktif hale gelecek
    app.session_interface = MySessionInterface()

    if app.config["VERSION"] == "1.0.1":
        pass
    if app.config["VERSION"] == "1.0.2":
        pass

    app.register_blueprint(home.bp)
    app.register_blueprint(users.bp)
    app.register_blueprint(contacts.bp)

    '''# viewsdaki fonksiyonları çağırıyoruz
    @app.route("/")
    def Index():
        return _Index()


    @app.route("/login2" , methods=["GET", "POST"])
    def Login():
        return _Login()

    @app.route("/logout")
    def Logout():
        return _Logout()

    @app.route("/contact", methods=["GET", "POST"])
    def Contact():
        return _Contact()

    @app.route("/contactlist")
    def ContactList():
        return _ContactList()'''

    return app



