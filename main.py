import random
# Constants for choices
ROCK = 1
PAPER = -1
SCISSORS = 0
# Mapping user input to choices
youDict = {"r": ROCK, "p": PAPER, "s": SCISSORS}
reverseDict = {ROCK: "Rock", PAPER: "Paper", SCISSORS: "Scissor"}
# Function to determine the outcome
def determine_winner(player, opponent):
    if player == opponent:
        return "draw"
    elif (opponent == PAPER and player == ROCK) or (opponent == SCISSORS and player == PAPER) or (opponent == ROCK and player == SCISSORS):
        return "lose"
    else:
        return "win"
# Main game function
def play_game(mode, player1_name, player2_name):
    player1_score = 0
    player2_score = 0
    rounds = 0
    target_wins = 3  # Best of 5 series
    while player1_score < target_wins and player2_score < target_wins:
        if mode == "single":
            computer = random.choice([PAPER, SCISSORS, ROCK])
            youstr = input(f"{player1_name}, enter your choice (r for Rock, p for Paper, s for Scissors, q to quit): ").lower()
            if youstr == 'q':
                break
            player = youDict[youstr]
            print(f"{player1_name} chose {reverseDict[player]}\nComputer chose {reverseDict[computer]}")
            result = determine_winner(player, computer)
            if result == "win":
                print(f"{player1_name} Wins! Congrats!")
                player1_score += 1
            elif result == "lose":
                print("You Lose! Try Again!")
                player2_score += 1
            else:
                print("It's a draw!")
        
        else:  # multiplayer mode
            youstr = input(f"{player1_name}, enter your choice (r for Rock, p for Paper, s for Scissors, q to quit): ").lower()
            if youstr == 'q':
                break
            player1 = youDict[youstr]
            youstr = input(f"{player2_name}, enter your choice (r for Rock, p for Paper, s for Scissors): ").lower()
            player2 = youDict[youstr]
            print(f"{player1_name} chose {reverseDict[player1]}\n{player2_name} chose {reverseDict[player2]}")
            if player1 == player2:
                print("It's a draw!")
            elif determine_winner(player1, player2) == "win":
                print(f"{player1_name} Wins!")
                player1_score += 1
            else:
                print(f"{player2_name} Wins!")
                player2_score += 1
            
            rounds += 1
            print(f"Score after {rounds} rounds: {player1_name}: {player1_score}, {player2_name}: {player2_score}")
    print(f"\nFinal Score: {player1_name}: {player1_score}, {player2_name}: {player2_score}")
    if player1_score > player2_score:
        print(f"{player1_name} is the champion!")
    elif player2_score > player1_score:
        print(f"{player2_name} is the champion!")
    else:
        print("It's a tie!")
# Game introduction
print("Welcome to Rock-Paper-Scissors!")
while True:
    mode = input("Choose mode (single for single-player, multiplayer for two players, q to quit): ").lower()
    if mode == 'q':
        break
    elif mode in ['single', 'multiplayer']:
        player1_name = input("Enter name for Player 1: ")
        player2_name = "Computer" if mode == "single" else input("Enter name for Player 2: ")
        play_game(mode, player1_name, player2_name)
    else:
        print("Invalid mode! Please choose again.")