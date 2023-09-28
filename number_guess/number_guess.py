import random

# Create a loop to allow the user to play multiple times
while True:
    # Generate a random number between 1 and 6 (simulate rolling a die)
    random_number = random.randint(1, 6)
    
    # Ask the user to guess the number
    guess = int(input("Guess the number on the die (from 1 to 6): "))
    
    # Check if the guess is correct and provide feedback
    if guess == random_number:
        print("Congratulations! You guessed the number.")
    else:
        print(f"Sorry, the number was {random_number}.")
    
    # Ask the user if they want to play again
    response = input("Do you want to play again? (y/n): ")
    
    # If the response is not "y" exit the loop to end the game
    if response.lower() != "y":
        break
