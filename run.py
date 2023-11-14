# IMPORTS
import pyfiglet
import time
import os
import random


# CONSOLE CLEARING
def clear():
    """
    Clears the console, to avoid the user too much scrolling
    """
    # If the system is Mac or Linux
    if os.name == 'posix':
        os.system('clear')
    # If the system is Windows
    else:
        os.system('cls')


# GAME LOGO AND WELCOME MESSAGE
def game_logo():
    """
    Will display the game name and welcome message in ASCII Art.
    After a pause, the user will be asked to enter their name.
    """
    logo = pyfiglet.figlet_format("Tomahawk Tactics") 
    welcome = pyfiglet.figlet_format("Welcome to Tomahawk Tactics", font = "digital") 
    print(logo, welcome, "\nby Rachael Babister\n")
    print("\nGame Loading...\n")
    time.sleep(2)
    return run_game()


# ENTER NAME AND START GAME
def run_game():
    """
    User enters their name in order for the game rules to appear.
    Once validated, the user can then specify y/n to play the game.
    """
    while True:
        global user_name 
        user_name = input("Enter your name: ")
        if user_name == "":
            print("You need to enter your name in order to play")
        else:
            break

    clear()
    print(pyfiglet.figlet_format("Welcome to Tomahawk Tactics", font = "digital"))
    print()
    print(f"Hello {user_name}! \n")
    print("""
This is Tomahawk Tactics, an axe throwing game in which you need
to hit a moving target! You get 5 throws per game, and will play
against the computer who will also get 5 throws. The winner is the
player who hits 3 targets first. To select a target, imagine there
are rows (in letters) and columns (in numbers), so an example of 
your guess might look like 'C3'.
    """)

    # READY TO PLAY FUNCTION
    def ready_to_play():
        """
        User inputs whether they are ready to play or not. 
        If 'y' the game creates the target ready to play. 
        If 'n', the program stops.
        """
        while True:
            user_input = input("Are you ready to play? (y/n): ").lower()
            if user_input == 'y':
                print("\nGreat! Get your axe ready!")
                # create_target() !!!!!!!???????????????????????????????????????????????
                return True
            elif user_input == 'n':
                print("\nAxes down, see you next time. Goodbye.")
                return False
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
    return ready_to_play()              


# CREATE GAME TARGETS
class TargetBoards:
    """
    Class to create the target game boards 4 x 4 in size,
    and keep track of the hits and misses
    """
    def __init__(self):
        print("\nGetting targets ready...\n")
        time.sleep(3)
        self.size = 4
        self.target_size = [[" " for i in range(self.size)] for i in range(self.size)]
        self.target_hits = 3
        self.target_positions = []
        self.direct_hit = []
        self.missed_hit = []

    def display_target(self):
        """
        Display the user and computer target game boards
        """
        user_target = f"\n{user_name}'s Target Board:\n"
        computer_target = "\nComputer's Target Board:\n"

        for i, (user_row, computer_row) in enumerate(zip(self.target_size, self.target_size)):
            if i == 0:
                user_target += "+" + "---+" * (self.size - 1) + "\n"
                computer_target += "+" + "---+" * (self.size - 1) + "\n"

            user_target += "".join([f"| {cell}" for cell in user_row]) + "|\n"
            computer_target += "".join([f"| {cell}" for cell in computer_row]) + "|\n"

            if i == len(self.target_size) - 1:
                user_target += "+" + "---+" * (self.size - 1) + "\n"
                computer_target += "+" + "---+" * (self.size - 1) + "\n"    
   
        print(user_target + computer_target)


# CALLING ALL FUNCTIONS
def main():
    """
    Runs all funcions
    """
    user_name = game_logo()
    target_boards = TargetBoards()
    target_boards.display_target()

main()