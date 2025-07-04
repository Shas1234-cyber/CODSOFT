#  Rock-Paper-Scissors Game
#  User Input: Prompt the user to choose rock, paper, or scissors.
#  Computer Selection: Generate a random choice (rock, paper, or scissors) for
#  the computer.
#  Game Logic: Determine the winner based on the user's choice and the
#  computer's choice.
#  Rock beats scissors, scissors beat paper, and paper beats rock.
#  Display Result: Show the user's choice and the computer's choice.
#  Display the result, whether the user wins, loses, or it's a tie.
#  Score Tracking (Optional): Keep track of the user's and computer's scores for
#  multiple rounds.
#  Play Again: Ask the user if they want to play another round.
#  User Interface: Design a user-friendly interface with clear instructions and
#  feedback.


import random
def rock_paper_scissors():
    print("------------------------")
    print("Rock-Paper-Scissors Game")
    print("------------------------")
    
    user_score = 0
    computer_score = 0
    
    while True:
        print(f"\nScore: You {user_score} - {computer_score} Computer")
        print("\nChoose:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        
        # User input:
        while True:
            try:
                user_choice = int(input("\nEnter choice (1-3): "))
                if 1 <= user_choice <= 3:
                    break
                print("Please enter 1, 2, or 3!")
            except ValueError:
                print("Invalid input! Enter a number.")
        
        choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
        user_weapon = choices[user_choice]
        
        # Computer selection
        computer_choice = random.randint(1, 3)
        computer_weapon = choices[computer_choice]
        
        print(f"\nYou chose: {user_weapon}")
        print(f"Computer chose: {computer_weapon}")
        
        # Game logic:
        if user_choice == computer_choice:
            print("\nIt's a tie!")
        elif (user_choice == 1 and computer_choice == 3) or \
             (user_choice == 2 and computer_choice == 1) or \
             (user_choice == 3 and computer_choice == 2):
            print("\nYou win!")
            user_score += 1
        else:
            print("\nComputer wins!")
            computer_score += 1
        
        # Play again:
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("\nFinal Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print("You won the game!")
            elif user_score < computer_score:
                print("Computer won the game.")
            else:
                print("Game ended in a tie.")
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    rock_paper_scissors()
