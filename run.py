import pyfiglet

# Game logo and welcome message
def game_logo():
    """
    Will display the game name and welcome message in ASCII Art.
    """
    logo = pyfiglet.figlet_format("Tomahawk Tactics") 
    welcome = pyfiglet.figlet_format("Welcome to Tomahawk Tactics", font = "digital" ) 
    print(logo, welcome)
    print("Game Loading...")


def main():
    """
    Run all funcions
    """
    game_logo()     

main()