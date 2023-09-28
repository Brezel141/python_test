import random

#List of secret words
secret_word = ["hello", "secret", "beautiful", "italy"]

#Choose a secret word
secret_word = random.choice(secret_word)

#Initialize variables
attemps = 0
max_attemps = 5
guessed_word = ""

#Print the number of letters in the secret word
print("The secret word has", len(secret_word), "letters")

while attemps < max_attemps:
    #Ask the user to guess a letter or the whole word
    guess = input("Guess a letter or the whole word: ")

    #Check if the guess is correct
    if guess == secret_word:
        guessed_word = secret_word
        break
    elif len(guess) == 1 and guess in secret_word:
        #Update the guessed word with correct letters
        guessed_word = "".join([char if char in guessed_word or char == guess else "_" for char in secret_word])
    else:
        attemps += 1
        print(f"Wrong guess. You have {max_attemps - attemps} attempts left.")

    #Display the current progress
    print("Current progress:", guessed_word)

#Provide a result message
if guessed_word == secret_word:
    print("Congratulation! U right, the word is: ", secret_word)
else:
    print("Nope, no more attemts. The secret word was: ", secret_word)    
