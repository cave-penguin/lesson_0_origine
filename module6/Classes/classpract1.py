class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Class of user with login and password
    """

    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password


if __name__ == "__main__":
    database = Database()
    while True:
        choice = int(input("Hello! Choose an action: \n1 - Enter\n2 - Registration\n"))
        if choice == 1:
            login = input("Enter login: ")
            password = input("Enter password: ")
            if login in database.data:
                if password == database.data[login]:
                    print(f"Login completed, Welcome {login}")
                    break
                else:
                    print("Invalid password")
            else:
                print("User not found")
        if choice == 2:
            user = User(
                input("Enter login: "),
                password := input("Enter password: "),
                password1 := input("Confirm password: "),
            )
            if password != password1:
                print("Passwords should be the same, try again.")
                continue
            database.add_user(user.username, user.password)

