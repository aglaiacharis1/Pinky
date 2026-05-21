class User:
    def __init__(self, first_name, last_name, phone, mail):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.mail = mail

    def describe_user(self):
        return f"User information: {self.first_name}, {self.last_name}, {self.phone}, {self.mail}"

    def greet_user(self):
        return f"Hello to {self.first_name} {self.last_name}"
    
class Admin(User):
    def __init__(self, first_name, last_name, phone, mail, privileges):
        super().__init__(first_name, last_name, phone, mail)
        self.privileges = privileges

    def show_privileges(self):
        print(f"Administrator privilages for {self.first_name}")
        for privilage in self.privileges:
            print(f"{privilage}")


admin_privilages = ["can add post", "can delete post", "can ban user"]
user_1 = Admin("Anna", "KKK", "56788", "kkk@gmail.com", admin_privilages)
print(user_1.describe_user())
user_1.show_privileges()



