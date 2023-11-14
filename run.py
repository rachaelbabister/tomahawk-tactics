# IMPORTS
import pyfiglet
import time
import os


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
    global welcome
    welcome = pyfiglet.figlet_format("Welcome to Tomahawk Tactics", font = "digital") 
    print(logo, welcome, "\nby Rachael Babister\n")
    print("\nGame Loading...\n")
    time.sleep(2)
    run_game()


# ENTER NAME AND START GAME
def run_game():
    """
    User enters their name in order for the game rules to appear.
    Once validated, the user can then specify y/n to play the game.
    """
    while True:
        user_name = input("Enter your name: ")
        if user_name == "":
            print("You need to enter your name in order to play")
        else:
            break

    clear()
    print(welcome)
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
    while True:
        user_input = input("Are you ready to play? (y/n): ").lower()
        if user_input == 'y':
            print("Great! Get your axe ready!")
            create_target()
            return True
        elif user_input == 'n':
            print("Maybe next time. Goodbye!")
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")



# CALLING ALL FUNCTIONS
def main():
    """
    Runs all funcions
    """
    game_logo()     

main()