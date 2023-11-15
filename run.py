# IMPORTS
import pyfiglet
import time
import os
from random import randrange


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


# CREATE GAME TARGET BOARDS
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
        self.hit_positions = []
        for i in range(self.target_hits):
            hit = self.random_hit()
            self.hit_positions.append(hit)
            #self.add_to_state(hit, "0")
        self.direct_hit = []
        self.missed_hit = []

    def display_target(self, hits_hidden=False):
        """
        Display the user and computer target game boards.
        Also hides the generated hit targets where necessary.
        """
        def hit_hidden(cell):
            if hits_hidden is True and cell == "0":
                return " "
            return cell    

        # Create Target Grid
        target = ""
        for i, row in enumerate(self.target_size):
            if i == 0:
                target += "+" + "---+" * (self.size - 1) + "\n"
                
            target += "".join([f"| {hit_hidden(cell)}" for cell in user_row]) + "|\n"
            
            if i == len(self.target_size) - 1:
                target += "+" + "---+" * (self.size - 1) + "\n"
                
        print(target)

    def random_hit(self):
        """
        Generate a random hit on the target board.
        """ 
        row = randrange(self.size)
        col = randrange(self.size)
        return (row, col)

    def unique_random_hit(self):
        """
        Generate a random hit that hasn't already been chosen.
        """
        while True:
            hit = self.random_hit()
            if hit not in self.hit_positions:
                return hit    


# GAME LOGO AND WELCOME MESSAGE
class TomaHawkGame:
    """
    Functions to launch the game play.
    """
    def throw_axe(self, target):



    def run_game(self):
        """
        Will display the game name and welcome message in ASCII Art.
        After a pause, the user will be asked to enter their name.
        """
        logo = pyfiglet.figlet_format("Tomahawk Tactics") 
        welcome = pyfiglet.figlet_format("Welcome to Tomahawk Tactics", font = "digital") 
        print(logo, welcome, "\nby Rachael Babister\n")
        print("\nGame Loading...\n")
        time.sleep(2)

        # ENTER NAME AND START GAME
        """
        User enters their name in order for the game rules to appear.
        Once validated, the user can then specify y/n to play the game.
        """
        while True:
            self.user_name = input("Enter your name: ")
            if self.user_name == "":
                print("You need to enter your name in order to play")
            else:
                break

        clear()
        print(pyfiglet.figlet_format("Welcome to Tomahawk Tactics", font = "digital"))
        print()
        print(f"Hello {self.user_name}! \n")
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
                    return True
                elif user_input == 'n':
                    print("\nAxes down, see you next time. Goodbye.")
                    return False
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
        return ready_to_play()


# CALLING ALL FUNCTIONS
def main():
    """
    Runs all funcions
    """
    play = TomaHawkGame()
    play.run_game()
    target_boards = TargetBoards()
    target_boards.display_target()

main()