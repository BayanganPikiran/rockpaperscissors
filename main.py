import random
from art import icons


plays = ["r", "p", "s"]




computer_play = random.choice(plays)

andre_rules = False
while not andre_rules:
    game_over = False
    while not game_over:
        print("Welcome to everyone's favorite game, 'Rock, Paper, Scissors'!")
        user_play = input("Type 'r' for rock, 'p' for paper, and 's' for scissors: ").lower()

        if user_play == "r" or user_play == "p" or user_play == "s":
            if user_play == "r":
                print(f"You play 'rock'\n{icons[0]}")
                if computer_play == "r":
                    print(f"Computer plays 'rock'.\n{icons[0]}\nYou draw.")
                elif computer_play == "p":
                    print(f"Computer plays 'paper'.\n{icons[1]}\nYou lose.")
                elif computer_play == "s":
                    print(f"Computer plays 'scissors'.\n{icons[2]}\nYou win.")
                game_over = True
            elif user_play == "p":
                print(f"You play paper.\n{icons[1]}")
                if computer_play == "r":
                    print(f"Computer plays 'rock'.\n{icons[0]}\nYou win.")
                elif computer_play == "p":
                    print(f"Computer plays 'paper'.\n{icons[1]}\nYou draw.")
                elif computer_play == "s":
                    print(f"Computer plays 'scissors'.\n{icons[2]}\nYou lose.")
                game_over = True
            elif user_play == "s":
                print(f"You play scissors.\n{icons[2]}")
                if computer_play == "r":
                    print(f"Computer plays 'rock'.\n{icons[0]}\nYou lose.")
                elif computer_play == "p":
                    print(f"Computer plays 'paper'.\n{icons[1]}\nYou win.")
                elif computer_play == "s":
                    print(f"Computer plays 'scissors'.\n{icons[2]}\nYou draw.")
                game_over = True
        else:
            print("You entered an invalid option. Please try again.")
    play_more = input("Would you like to play again? Type 'y' for yes, or 'n' for no: ")
    if play_more == "n":
        print("You are a weakling. Run away!")
        andre_rules = True
    else:
        print("Bring on some more!")


