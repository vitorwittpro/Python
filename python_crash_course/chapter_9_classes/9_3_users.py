class User:
    def __init__(self, first_name, last_name, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()}, | {self.email} | {self.phone}")


    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}")


user1 = User('Vitor', 'Hugo', 'h.vitor@examle.com', '9123451234')
user2 = User('Carsen', 'Magnus', 'm.carsen', '999292929')

user1.describe_user()
user2.describe_user()

user1.greet_user()
user2.greet_user()