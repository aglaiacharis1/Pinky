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

user_1 = User("Anna", "KKK", "56788", "kkk@gmail.com")
user_2 = User("Nina", "JJJJ", "8477", "lll@gmail.com")
user_3 = User("Lana", "MMM", "84762", "mmm@gmail.com")

print(user_1.describe_user())
print(user_1.greet_user())

print(user_2.describe_user())
print(user_2.greet_user())

print(user_3.describe_user())
print(user_3.greet_user())