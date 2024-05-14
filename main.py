from utils.user_manager import UserManager
from utils.dice_game import DiceGame

def main():
    user_manager = UserManager()

    user_manager.load_users()
    while True:
        print("Welcome to game Dice Roll")
        print("""1. Register
2. Log-In
3. Exit""")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            user_manager.register()
        elif choice == 2:
            user_manager.login()
        elif choice == 3:
            print("Exiting the game.")
            exit()
        else:
            print("Invalid choice. Try again.")
            main()

if __name__ == "__main__":
    main()


