import random
import time

# List of mathematical operators to use in problems
OPERATORS = ['+', '-', '*']
# Minimum and maximum values for numbers in problems
MIN_OPERAND = 3
MAX_OPERAND = 12
# Total number of math problems to generate
TOTAL_PROBLEMS = 10

# Function to generate a random math problem
def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)  # Random left number
    right = random.randint(MIN_OPERAND, MAX_OPERAND)  # Random right number
    operator = random.choice(OPERATORS)  # Randomly select an operator

    expr = str(left) + '' + operator + '' + str(right)  # Create math expression as a string
    answer = eval(expr)  # Calculate the answer
    return expr, answer  # Return the problem and answer

wrong = 0  # Counter for wrong answers
input('Press enter to start: ')  # Wait for user to start
print('------------------')

start_time = time.time()  # Record the start time

# Loop through the number of problems
for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()  # Generate a new problem
    while True:  # Keep asking until the user gets it right
        guess = input('Problem #' + str(i + 1) + ':' + ' ' + expr + '= ')  # Ask the user for input
        if guess == str(answer):  # If the answer is correct, move to the next question
            break
        wrong += 1  # If incorrect, increase the wrong answer count

end_time = time.time()  # Record the end time
total_time = round(end_time - start_time, 2)  # Calculate the total time taken

print('------------------')
print('Nice work! You finished in', total_time, 'seconds!')  # Display completion message
