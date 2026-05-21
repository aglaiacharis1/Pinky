class User:
    def __init__(self, first_name, last_name, phone, mail):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.mail = mail
        self.login_attempts = 0

    def describe_user(self):
        return f"User information: {self.first_name}, {self.last_name}, {self.phone}, {self.mail}"

    def greet_user(self):
        return f"Hello to {self.first_name} {self.last_name}"
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_1 = User("Anna", "KKK", "56788", "kkk@gmail.com")
user_2 = User("Nina", "JJJJ", "8477", "lll@gmail.com")
user_3 = User("Lana", "MMM", "84762", "mmm@gmail.com")

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(f"Increment attempts: {user_1.login_attempts}")
user_1.reset_login_attempts()
print(f"Reset attempts: {user_1.login_attempts}")
