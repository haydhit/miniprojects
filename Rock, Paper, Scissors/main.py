import random

def get_choices():
    player_choice = input("Enter a choice (Rock, Paper, Scissors: ")
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player} & Computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "Rock":
        if computer == "Scissors":
            return "Rock smashes Scissors! Player wins!"
        else:
            return "Paper covers Rock! Computer wins!"
        
    elif player == "Paper":
        if computer == "Rock":
            return "Paper covers Rock! Player wins!"
        else:
            return "Scissors cuts Paper! Computer wins!"
        
    elif player == "Scissors":
        if computer == "Paper":
            return "Scissors cuts Paper! Player wins!"
        else:
            return "Rock smashes Scissors! Computer wins!"
        
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)