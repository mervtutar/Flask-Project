from flask import Flask, render_template, redirect, url_for, request, abort
from app.controllers import MySessionInterface
from app.controllers import UserLogin, UserLogout, GetCurrentUsername, GetContactList, SaveContactRequest

'''
render_template: HTML dosyalarını çağırmak için kullanılır.
redirect: Kullanıcıyı başka bir URL'ye yönlendirmek için kullanılır.
url_for: Flask içinde dinamik URL oluşturmak için kullanılır.
request: Kullanıcıdan gelen veri almak için kullanılır.
make_response: HTTP yanıtı oluşturmak için, response nesnesi oluştururken kullanılır.
Signer & BadSignature (itsdangerous): Verileri güvenli şekilde imzalamak ve doğrulamak için kullanılır.
'''


app = Flask(__name__, template_folder="../templates", static_folder="../static") # bu global değişken dosyanın ismini veriyor, tek nokta mevcut folderda ara, iki nokta bir üst folderda ara demektir yani bizim için app folderı
# tarayıcıdaki adresin ne olduğunu flask uygulamamıza söylemeliyiz, bu adres domain kısmından sonrasını içerir /slash sonrası
# session kullanmak içinde cookielerde oluşturulan verinin şifrelenmesini sağlamalıyız
app.secret_key = "secret key" # bu key ile session aktif hale gelecek
app.session_interface =  MySessionInterface()# flask varsayılan kendi interface i (session verilerini tarayıcıya yazan) yerine kendi oluşturduğumuz interfacei kullanacak
# Çerez (cookie) kontrol edilir.
# Eğer çerez geçerliyse, çözülerek ekrana yazdırılır.
# Eğer çerez değiştirilmişse "bad signature" hatası verilir.
# Yeni bir çerez ("Mehmet") oluşturularak tarayıcıya kaydedilir.


# views dosyasını mvc-models,views,controllers tasarım desenine dönüştüreceğiz, bu programı parçalar ve daha kolay yönetmeye yarar
# viewsda sadece kullanıcı arayüzü ilgilendiren kodlar (render_template, redirect, request.form,  bulunmalı
# veri ile ilgili şeyleri bizim için model ayarlar
# controllers view ile iletişimde olup, ondan gelen veri girişlerini yorumlar, algoritma ve iş mantığı burada çalışır




# cookielerle aynı işleve sahip olan session, cookilerin aksine veriler tarayıcı yerine sunucuda depolanır.
'''@app.route("/") # home page im olacak
def Definition():
    if 'name' in session: # session ın içinde name diye bir key var mı
        print('name', session['name']) # key i oku
    session['name'] = 'Ahmet'
    session['lastname'] = 'Ahmetoğlu'
    session['username'] = 'ahmet123'
    # session ı kullanıcının tarayıcısı (default olarak yapılır) yerine istediğimiz yerde kaydedebiliriz

    return "<html><body><h1>İlk Flask Denemesi</h1></body></html>" # return olarak html de dönebiliriz


    # return "İlk Flask denemesi" return olarak string dönebiliriz
    # return  "<html><body><h1>İlk Flask Denemesi</h1></body></html>" # return olarak html de dönebiliriz


# set FLASK_DEBUG=1 terminale bunu yazarsak development moduna geçer ve her değişiklik yaptığımızda kapatıp açmak zorunda kalmayız

@app.route("/hello") # adresimde /hello varsa bu fonksiyonu çağır
def Hello():
    return render_template("hello.html")


@app.route("/hello-admin") # adresimde /hello-admin varsa bu fonksiyonu çağır
def HelloAdmin():
    return render_template("hello_admin.html")

@app.route("/hello-user/<name>") # adresteki name i daha sonra kullanabilirz
def HelloUser(name):
    if name.lower() == "admin":
        return redirect(url_for("HelloAdmin")) # name eğer admin ise HelloAdmin fonksiyonunu çağır
    #print(name)
    return render_template("hello_user.html", username=name)

@app.route("/add/<int:number1>/<int:number2>")
def Add(number1, number2):
    calculation_result = number1 + number2 # stringleri toplar
    return render_template("add.html", number1 = number1, number2 = number2, result = calculation_result)



# değerleri parametre olarak fonksiyona iletmek yerine değerleri fonksiyona gönderip toplamlarını başka bir yöntemle alabiliriz.
# number1 ve number2 urlde argüman olarak kullanılacak, http://127.0.0.1:5000/add?number1=12&number2=13
@app.route("/add")
def Add():
    # soru işareti ile argüman gönderilmişse requestin args sözlüğü ile bunları alabiliriz
    number1 = int(request.args["number1"])
    number2 = int(request.args["number2"])
    calculation_result = number1 + number2 # stringleri toplar
    return render_template("add.html", number1 = number1, number2 = number2, result = calculation_result)


# methodun adı belirtilmemişse get dir, belirtilmişse post olur
@app.route("/login", methods=['POST', 'GET']) # get sayfayı görmek için sunucudan bilgi alır, post ise submite bastığımızda adrese gelecek olan yer sunucuya bilgi gönderir
def Login():
    if request.method == 'POST': # böyleyse user ekranına gönderelim(redirect), username i alıp HelloUser fonksiyonuna gönder
        username = request.form["username"] # form elementi login.htmlinin içinde içerisinde user name bulunuyor, bunu aldık
        return redirect(url_for("HelloUser", name=username))
    else:
        return render_template("login.html")

@app.route("/student")
def Student():
    return render_template("student.html")

@app.route("/result", methods=['POST']) # sonuçlar burada olacağı için post kullandık
def Result():
    
    #birden fazla değişken varsa ve biz html e göndermek istiyorsak teker teker parametre olarak yazmak yerine sözlük oluşturup key value olarak yazmak daha kullanışlı

    ContextData = {
    'name': request.form["name"],
    'physics': request.form["physics"],
    'mathematics': request.form["mathematics"],
    'chemistry': request.form["chemistry"],
    }
    return render_template("student_result.html", **ContextData)
    #Öğrencinin adı ve notları formdan alınır ve student_result.html sayfasına gönderilir.
   
    name = request.form["name"]
    physics = request.form["physics"]
    mathematics = request.form["mathematics"]
    chemistry = request.form["chemistry"]
    return render_template("student_result.html", name=name,
                           physics=physics,
                           mathematics=mathematics,
                           chemistry=chemistry)
'''

@app.route("/")
def Index():
    username, loginAuth = GetCurrentUsername()
    return render_template("index.html", username=username, login_auth=loginAuth)

@app.route("/contact", methods=["GET", "POST"])
def Contact():
    if request.method == "POST":
        if request.form:
            name = request.form.get("name")
            email = request.form.get("email")
            category = request.form.get("category")
            priority = request.form.get("priority")
            message = request.form.get("message")
            SaveContactRequest(name, email, category, priority, message)
            return redirect(url_for("Contact"))
    username, loginAuth = GetCurrentUsername()
    return render_template("contact.html",username=username, login_auth=loginAuth)

@app.route("/contactlist")
def ContactList():
    username, loginAuth = GetCurrentUsername()
    contactList = GetContactList()
    return render_template("contact_list.html",username=username, login_auth=loginAuth, contactList=contactList)

@app.route("/login2", methods=["GET", "POST"])
def Login():
    if request.method == "POST":
        if request.form:
            if "username" in request.form and "password" in request.form:
                username = request.form["username"]
                password = request.form["password"]
                if UserLogin(username,password):
                    return redirect(url_for("Index"))
                else:
                    return redirect(url_for("Login"))

        abort(400)
    username, loginAuth = GetCurrentUsername()
    return render_template("login2.html", username=username, login_auth=loginAuth)

@app.route("/logout")
def Logout():
    if UserLogout():
        return redirect(url_for("Index"))
