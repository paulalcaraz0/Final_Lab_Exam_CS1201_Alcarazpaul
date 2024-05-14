from utils.dice_game import DiceGame


class UserManager:
    def __init__(self):
        self.user_accounts = {}

    def load_users(self):
        try:
            with open("user_accounts.txt", "r") as file:
                for line in file:
                    username, password = line.strip().split(":")
                    self.user_accounts[username] = {"password": password}
        except FileNotFoundError:
            print("User accounts file not found.")

    def save_users(self, username, password):
        try:
            with open("user_accounts.txt", "a") as file:
                file.write(f"{username}:{password}\n")
            print("User account saved successfully.")
        except Exception as e:
            print(f"Error saving user account: {e}")

    def validate_username(self):
        user = input("Enter username (must be at least 4 characters): ")
        if len(user) < 4:
            print("Username must be at least 4 characters!")
            return False
        return user

    def validate_password(self):
        pass_word = input("Input password (must be at least 8 characters): ")
        if len(pass_word) < 8:
            print("Password must be at least 8 characters!")
            return False
        return pass_word

    def register(self):
        print("**Register**")
        username = self.validate_username()
        password = self.validate_password()
        if username and password:
            self.user_accounts[username] = {"password": password}
            self.save_users(username, password)
            print("Register Successfully!!")

    def login(self):
        print("LOG-IN")
        user = input("Enter username: ")
        password = input("Enter password: ")
        if user in self.user_accounts and self.user_accounts[user]["password"] == password:
            print("Sign in successful")
            dice_game_instance = DiceGame(user)  # Create an instance of DiceGame
            dice_game_instance.menu() 
        else:
            print("Invalid username or password")
