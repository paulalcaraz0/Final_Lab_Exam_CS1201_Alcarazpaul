# import dice_game
# from datetime import datetime

# class Score:
#     def load_score(self):
#         try:
#             with open("top_scores.txt", "r") as file:
#                 self.top_scores = [line.strip() for line in file]
#         except FileNotFoundError:
#             print("Top scores file not found.")


#     def save_scores(self):
#         try:
#             current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#             with open("top_scores.txt", "a") as file:
#                 file.write(f"{self.username}: {self.total_points}, Date: {current_time}\n")
#             print("Score saved successfully.")
#         except Exception as e:
#             print(f"Error saving score: {e}")


import os
from datetime import datetime

class Score:
    def __init__(self):
        self.username = None
        self.total_points = None

    def load_score(self):
        try:
            with open("top_scores.txt", "r") as file:
                self.top_scores = [line.strip() for line in file]
        except FileNotFoundError:
            print("Top scores file not found.")

    def save_scores(self, folder_path):
        try:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # Create the folder if it doesn't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            # Save user.txt
            with open(os.path.join(folder_path, "user.txt"), "w") as user_file:
                user_file.write(f"Username: {self.username}\nTotal Points: {self.total_points}")
            # Save score.txt
            with open(os.path.join(folder_path, "score.txt"), "a") as score_file:
                score_file.write(f"Username: {self.username}\nTotal Points: {self.total_points}\nDate: {current_time}\n")
            print("Score saved successfully.")
        except Exception as e:
            print(f"Error saving score: {e}")

    def open_folder(self, folder_path):
        try:
            # Change the current working directory to the folder_path
            os.chdir(folder_path)
            print(f"Opened folder: {folder_path}")

            # List the contents of the folder
            contents = os.listdir()
            print("Contents of the folder:")
            for item in contents:
                print(item)

        except FileNotFoundError:
            print(f"Folder not found: {folder_path}")
        except Exception as e:
            print(f"Error opening folder: {e}")

