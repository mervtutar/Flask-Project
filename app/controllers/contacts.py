from app.models import ContactRequest

def GetContactList():
    return [
        ["Berk", "Satış", "Yüksek"],
        ["Ezgi", "İK", "Orta"],
        ["Merve", "Üretim", "Düşük"]
    ]
# veri ile ilgili şeyleri bizim için model ayarlar

def SaveContactRequest(name, email, category, priority, message):
    contactRequest = ContactRequest()
    contactRequest.name = name
    contactRequest.email = email
    contactRequest.category = category
    contactRequest.priority = priority
    contactRequest.message = message
    contactRequest.Save()
    print(contactRequest) # str methodu print olacak



