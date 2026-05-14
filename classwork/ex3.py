class User:
    def __init__(self, first_name, last_name, mail, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.mail = mail
        self.phone = phone

    def describe_user(self):
        return f"User information: {self.first_name}, {self.last_name}, {self.mail}, {self.phone}"

    def greet_user(self):
        return f"Hello {self.first_name}, {self.last_name}"

user1 = User("Anna", "Shhh", "anna@gmail.com", "54666")
user2 = User("Lika", "Dgggg", "lika@gmail.com", "547866")
user3 = User("Lana", "YYYhh", "lana@gmail.com", "54266")

print(user1.describe_user())
print(user2.describe_user())
print(user3.greet_user())

