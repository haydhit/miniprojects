def get_choices():
    player1_choice = input("P1 - Enter a choice (Rock, Paper, Scissors: ")
    options = ["Rock", "Paper", "Scissors"]
    player2_choice = input("P2 - Enter a choice (Rock, Paper, Scissors: ")
    choices = {"player1": player1_choice, "player2": player2_choice}
    return choices

def check_win(player1, player2):
    print(f"You chose {player1} & Player 2 chose {player2}")
    if player1 == player2:
        return "It's a tie!"
    elif player1 == "Rock":
        if player2 == "Scissors":
            return "Rock smashes Scissors! Player wins!"
        else:
            return "Paper covers Rock! Computer wins!"
        
    elif player1 == "Paper":
        if player2 == "Rock":
            return "Paper covers Rock! Player wins!"
        else:
            return "Scissors cuts Paper! Computer wins!"
        
    elif player1 == "Scissors":
        if player2 == "Paper":
            return "Scissors cuts Paper! Player wins!"
        else:
            return "Rock smashes Scissors! Computer wins!"
        
choices = get_choices()
result = check_win(choices["player1"], choices["player2"])
print(result)