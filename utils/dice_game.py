from random import randint
from datetime import datetime

class DiceGame:
    def __init__(self, username):
        self.username = username
        self.win = 0
        self.top_scores = []
        self.total_points = 0

    def load_score(self):
        try:
            with open("top_scores.txt", "r") as file:
                self.top_scores = [line.strip() for line in file]
        except FileNotFoundError:
            print("Top scores file not found.")


    def save_scores(self):
        try:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open("top_scores.txt", "a") as file:
                file.write(f"{self.username}: {self.total_points}, Date: {current_time}\n")
            print("Score saved successfully.")
        except Exception as e:
            print(f"Error saving score: {e}")

             
    def play_stage(self):
        stage_points = 0

        print("Starting Dice Game...")
        for i in range(3):
            cpu = randint(1, 6)
            user = randint(1, 6)
            print()
            print(f"cpu: {cpu}")
            print(f"user: {user}")
            if user > cpu:
                self.win += 1
                stage_points += 1
                print("You win! You earned 1 point")
            elif user < cpu:
                print("You lose! You didn't earn a point")
            else:
                print("It's a tie")

        self.total_points += stage_points

        print("\nTotal wins in this stage:", stage_points)
        print("Total points so far:", self.total_points)
        
    def play_game(self):
        while True:
            while self.win < 2:
                self.play_stage()

                if self.win == 1:
                    print("\n")
                    self.total_points += 0
                    self.save_scores()
                    

                    print("Returning to the menu.")
                    self.total_points = 0
                    self.menu()

            print("You can proceed to the next stage")
            choice = input("Would you like to continue? [y or any character]: ").lower()
            if choice != "y":
                self.save_scores()  
                print("Exiting the game.")
                self.menu()
            else:
                self.win = 0  


    def show_top_scores(self):
        try:
            with open("top_scores.txt", "r") as file:
                scores = []
                for line in file:
                    parts = line.strip().split(":", 1)  
                    if len(parts) == 2:  
                        username = parts[0]
                        score_with_date = parts[1]
                        score, date = score_with_date.split(", Date:")
                        scores.append((username, int(score), date))
                
            
                sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
                
                
                print("Top 10 Highest Scores:")
                for i, (username, score, date) in enumerate(sorted_scores[:10], start=1):
                    print(f"{i}. Username: {username}, Score: {score}, Date: {date}")
    
                self.menu()
                    
        except FileNotFoundError:
            print("Top scores file not found.")

    def logout(self):
        print("Logging out...")
        exit()

    def menu(self):
        print("Menu:")
        print("1. Start Game")
        print("2. Show top scores")
        print("3. Log out")

        choice = input("Enter your choice, or leave it blank to cancel: ")
        if choice == "1":
            self.win = 0  
            self.play_game()
        elif choice == "2":
            self.show_top_scores()
        elif choice == "3":
            self.logout()
        else:
            exit()


