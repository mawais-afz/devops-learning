import random

def get_computer_choice():
    return random.choice(['s', 'w', 'g'])

def get_result(comp, player):
    # Returns 1 if player wins, -1 if computer wins, and 0 for draw
    if comp == player:
        return 0
    elif (comp == 's' and player == 'w') or \
         (comp == 'w' and player == 'g') or \
         (comp == 'g' and player == 's'):
        return -1
    return 1

def main():
    print("Welcome to Snake(s) Water(w) Gun(g) Game!")
    print("Enter 'q' to quit")
    
    choices = {'s': 'Snake', 'w': 'Water', 'g': 'Gun'}
    player_score = 0
    computer_score = 0
    
    while True:
        player = input("\nEnter your choice (s/w/g): ").lower()
        
        if player == 'q':
            break
            
        if player not in ['s', 'w', 'g']:
            print("Invalid choice! Please enter s, w, or g")
            continue
            
        computer = get_computer_choice()
        
        print(f"\nYou chose: {choices[player]}")
        print(f"Computer chose: {choices[computer]}")
        
        result = get_result(computer, player)
        
        if result == 0:
            print("It's a draw!")
        elif result == 1:
            print("You win!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
            
        print(f"\nScores - You: {player_score}, Computer: {computer_score}")
    
    print("\nGame Over!")
    print(f"Final Scores - You: {player_score}, Computer: {computer_score}")
    if player_score > computer_score:
        print("Congratulations! You won the game!")
    elif computer_score > player_score:
        print("Better luck next time! Computer won the game!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
