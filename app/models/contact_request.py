class ContactRequest:
    name = ""
    email = ""
    category = ""
    priority = ""
    message = ""

    def __str__(self):
        return (f"name:{self.name} email:{self.email} category:{self.category}"
                f" priority:{self.priority} message:{self.message}")

    def Save(self):
        pass

