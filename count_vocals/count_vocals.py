# Define a tuple containing vowels
vowels = ("a", "e", "i", "o", "u")

# Ask the user to input a word
word = input("Enter a word: ")

# Initialize a variable for counting vowels
count = 0

# Iterate through the word and count the vowels
for letter in word:
    if letter.lower() in vowels:  # Using .lower() to consider both uppercase and lowercase vowels
        count += 1

# Print the count of vowels in the word
print("The number of vowels in the word is:", count)








