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
            self.add_to_target(hit, "t")
        self.direct_hit = []
        self.missed_hit = []

    def display_target(self, hits_hidden=False):
        """
        Display the user and computer target game boards.
        Hide the generated hit targets where necessary.
        """
        def hit_hidden(cell):
            if hits_hidden is True and cell == "t":
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
        return (hit not in self.direct_hit and hit not in self.missed_hit)

    def show_hit(self, hit):
        """
        Add the guess to the target if correct
        """
        if hit in self.hit_positions:
            self.direct_hit.append(hit)
            self.add_to_target(hit, "O")
        else:
            self.missed_hit.append(hit)
            self.add_to_target(hit, "x")
            
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

    def game_over(self, player_hits):
        """
        End the game when a player hits 3 targets.
        """
        return len(set(player_hits)) == self.target_hits


# GAME LOGO AND WELCOME MESSAGE
class TomaHawkGame:
    """
    Functions to launch the game play.
    """
    def parse_throw_axe(self, throw):
        """
        Parse the user's throw to be tuple of int.
        """
        return tuple(map(int, throw.split(",")))

    def throw_axe(self, target):
        """
        Get the user to 'throw' their axe by selecting a row and column.
        Validate the guess - if the guess is unique it will return
        the parsed guess. If the guess is not unique, it will print a 
        message and continue the loop.
        """
        while True:
            try:
                parsed_throw_axe = self.parse_throw_axe(
                    input("Axes ready! Enter your coordinates to take a throw: "))

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
            clear()
            print(pyfiglet.figlet_format("Welcome to Tomahawk Tactics", font = "digital"))
            print("x = miss | O = hit | t = the computer's hidden targets")
            print(f"\n{self.user_name} - this is your target: \n")
            computer_target.display_target(True)
            print("Computer's target: \n")
            user_target.display_target()

        while True:
            show_targets()
            """
            User & computer's guesses.
            User's guess is added to computer's target.
            Computer's guess is added to user's target
            """
            user_throw = self.throw_axe(computer_target) 
            computer_target.show_hit(user_throw) 

            # Check to see who won - user or computer
            if computer_target.game_over(computer_target.direct_hit):
                show_targets()
                print(f"Well done {self.user_name}! You won Tomahawk Tactics!\n")
                break

            computer_throw = user_target.get_random_hit() 
            user_target.show_hit(computer_throw) 

            if user_target.game_over(user_target.direct_hit):
                show_targets()
                print("Better luck next time. The computer won Tomahawk Tactics!")
                break

            # Clear lists for the next game iteration
            user_target.direct_hit = []
            user_target.missed_hit = []

    # ENTER NAME AND START GAME
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

        # GAME LOOP FOR PLAYING MULTIPLE ROUNDS
        while True:
            clear()
            print(pyfiglet.figlet_format("Welcome to Tomahawk Tactics", font = "digital"))
            print()
            print(f"Hello {self.user_name}! \n")
            print("""
This is Tomahawk Tactics, an axe throwing game in which you need
to hit a moving target! You will be playing against the computer - 
the winner is the player who hits their 3 targets first. \n
In order to 'throw' your axe, you need to choose 2 numbers, each
one between 0 and 3 and separate them with a comma. These are 
your coordinates for the target. The row is the first number and
the column is the second number, e.g: 0,2\n
x = miss | O = hit | t = the computer's hidden targets
        """)
            # READY TO PLAY 
            while True:
                user_input = input("Are you ready to play? (y/n): ").lower()
                if user_input == 'y':
                    print("\nGreat! Get your axe ready!")

                    computer_target = TargetBoards()
                    user_target = TargetBoards()
                    self.play_game(user_target, computer_target)

                    play_again = input("Would you like to play another round? y/n \n")
                    if play_again.lower() == "n":
                        print("\nAxes down, see you next time. Goodbye.")
                        return 
                    else:
                        break
                elif user_input == 'n':
                    print("\nAxes down, see you next time. Goodbye.")
                    return
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")


# CALLING GAME FUNCTIONS
play = TomaHawkGame()
play.run_game()
