# Initialize variables
count = 1
max_count = 100
div_3 = 3
div_5 = 5

# Start a loop to iterate from 1 to 100
while count <= max_count:
    if count % div_3 == 0 and count % div_5 == 0:
        # Check if the number is divisible by both 3 and 5
        print("FizzBuzz")
    elif count % div_3 == 0:
        # Check if the number is divisible by 3
        print("Fizz")
    elif count % div_5 == 0:
        # Check if the number is divisible by 5
        print("Buzz")
    else:
        # If none of the conditions are met, print the number itself
        print(count)
    
    # Increment the count for the next iteration
    count += 1
