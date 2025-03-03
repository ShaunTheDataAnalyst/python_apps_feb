import random  # Import the random module to generate random numbers

# Ask the user for the upper limit of the random number
# This determines the range within which the random number will be generated
top_of_range = input('Type a number: ')

# Check if the user's input is a valid number
if top_of_range.isdigit():  # isdigit() checks if the input contains only digits
    top_of_range = int(top_of_range)  # Convert the input from string to integer

    # Ensure the number is greater than 0
    if top_of_range <= 0:
        print('Please type a number larger than 0.')
        quit()  # Exit the program if the condition is not met
else:
    print('Please type a number next time.')  # Message for invalid (non-digit) input
    quit()  # Exit the program if the input is not a valid number

# Generate a random number between 0 and the user-defined upper limit (exclusive)
random_number = random.randrange(top_of_range)

# Initialize the guess counter to track the number of attempts
guesses = 0

# Start an infinite loop to keep asking the user for guesses until they get it right
while True:
    guesses += 1  # Increment the guess counter by 1 with each attempt

    # Prompt the user to guess the number
    user_guess = input('Make a guess: ')

    # Check if the guess is a valid number
    if user_guess.isdigit():
        user_guess = int(user_guess)  # Convert the guess to an integer if valid
    else:
        print('Please type a number next time.')  # Message for invalid input
        continue  # Skip the rest of the loop and ask for a new guess

    # Check if the user's guess matches the random number
    if user_guess == random_number:
        print('You got it!')  # Congratulate the user if they guessed correctly
        break  # Exit the loop since the correct guess was made
    elif user_guess > random_number:
        print('You were above the number!')  # Hint if the guess is too high
    else:
        print('You were below the number!')  # Hint if the guess is too low

# Display the total number of guesses the user took to get the correct answer
print('You got it in', guesses, 'guesses')
