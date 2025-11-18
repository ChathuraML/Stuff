from random import randint


#Define deficulty levels
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

#Choose difficulty level
def difficulty_levels():
    answer = input("Choose a difficulty. Type 'easy' or 'hard' : ")
    if answer == "easy":
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS


#Check with user guess(high/low)
def check_guess(user_guess, original_number, level):
    if user_guess > original_number:
            print("Too high.")
            return level -1
    elif user_guess < original_number:
        print("Too low.")
        return level -1
    else:
        print(f"You got it! The answer was {original_number}")
        return 'win'

def check_input():
    while True:
        try:
            user_input = int(input("Make a guess: "))
            return user_input
        except ValueError:
            print("Invalid input, please enter a number")
            #user_input = int(input("Make a valid guess: "))

#Game logic
def game():
    print("Welcome to the Number Guesing Game!\n")

    game_over = True
    while game_over:
        print("I'm thinking of a number between 1 and 100")
        original_guessed_number = randint(1,100)
    
        difficulty_level = difficulty_levels()
        print(f"You have {difficulty_level} attempts to guess the number.\n")
        current_level = difficulty_level
        while current_level !=0:
            user_guessed = check_input()             
            current_level = check_guess(user_guessed, original_guessed_number, current_level)
            if current_level == "win":
                break
            elif current_level > 0:
                print(f"You have {current_level} attempts remaining to guess the number.\n")
            elif current_level == 0:
                print("You have run out of guesses, you lose.\n")
        
        answer = input("Do you want to play again ?(y/n): ")
        print("\n")

        if answer == "n":
            game_over=False
            print("Byeeeee!!!!")
            


game()      



