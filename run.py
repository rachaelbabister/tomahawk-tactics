import pyfiglet
import time

# Game logo and welcome message
def game_logo():
    """
    Will display the game name and welcome message in ASCII Art.
    After a pause, the user will be asked to enter their name.
    """
    logo = pyfiglet.figlet_format("Tomahawk Tactics") 
    welcome = pyfiglet.figlet_format("Welcome to Tomahawk Tactics", font = "digital" ) 
    print(logo, welcome, "\nby Rachael Babister\n")
    print("\nGame Loading...\n")
    time.sleep(2)
    run_game()


def run_game():
    """
    User enters their name in order for the game rules to appear.
    Once validated, the user can then specify y/n to play the game.
    """
    while True:
        user_name = input("Enter your name:\n")
        if user_name == "":
            print("You need to enter your name in order to play")
        else:
            break

    print(f"Hello {user_name}!")
    print("""
    This is Tomahawk Tactics, an axe throwing game in which you need
    to hit a moving target! You get 5 throws per game, and will play
    against the computer who will also get 5 throws. The winner is the
    player who hits 3 targets first. To select a target, imagine there
    are rows (in letters) and columns (in numbers), so an example of 
    your guess might look like 'C3'.
    """)


def main():
    """
    Runs all funcions
    """
    game_logo()     

main()