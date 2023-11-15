# IMPORTS
import pyfiglet
import time
import os
from random import randrange


# CONSOLE CLEARING
def clear():
    """
    Clear the console, to avoid the user too much scrolling
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
            self.add_to_target(hit, "0")
        self.direct_hit = []
        self.missed_hit = []

    def display_target(self, hits_hidden=False):
        """
        Display the user and computer target game boards.
        Hide the generated hit targets where necessary.
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
                
            target += "".join([f"| {hit_hidden(cell)}" for cell in row]) + "|\n"
            
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

    def validate_throw(self, hit):
        """
        Validate the throw 'hits' the target
        """
        if len(hit) != 2:
            return False
        if hit[0] < 0 or hit[0] > self.size - 1:
            return False
        if hit[1] < 0 or hit[1] > self.size - 1:
            return False
        return True   

    def unique_throw(self, hit):
        """
        Ensure the guess is unique
        """
        return (hit not in self.target_hit and hit not in self.target_not_hit)

    def show_hit(self, hit):
        """
        Add the guess to the target if correct
        """
        if hit in self.hit_positions:
            self.direct_hit.append(hit)
            self.add_to_target(hit, "O")
        else:
            self.missed_hit.append(hit)
            self.add_to_target(hit, "X")
            
    def add_to_target(self, hit, letter):
        """
        Add a letter on the target board
        """
        self.target_size[hit[0]][hit[1]] = letter

    def get_random_hit(self):
        """
        Generate a random position not guessed before
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
        """
        Get the user to 'throw' their axe by selecting a row and column.
        Validate the guess - if the guess is unique it will return
        the parsed guess. If the guess is not unique, it will print a 
        message and continue the loop.
        """
        while True:
            try:
                parsed_throw_axe = self.parse_throw_axe()
                input("Throw your first axe! Enter your 2 chosen numbers: ")

                if target.validate_throw(parsed_throw_axe) is True:
                    if target.unique_throw(parsed_throw_axe):
                        return parsed_throw_axe
                    print("This has been guessed already. Try again!")
                else:
                    print("You missed the target! Try again.")
            except ValueError:
                pass                

    def play_game(self, user_target, computer_target):
        """
        Set the game up against the computer, ready to play
        """
        def show_targets():
            """
            Show the target boards
            """
            print("Computer's Target: \n")
            computer_target.display_target(True)
            print(f"{self.user_name}'s Target: \n")
            user_target.display_target()



    def run_game(self):
        """
        Display the game name and welcome message in ASCII Art.
        User asked to enter their name.
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
player who hits 3 targets first. To select a target, please select
2 numbers between 0 and 3 and separate them with a comma. 
For example, 0,2
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
    Run all funcions
    """
    play = TomaHawkGame()
    play.run_game()

main()