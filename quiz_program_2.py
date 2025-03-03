

# Print a welcome message

print("Welcome to my quiz!")

# Ask the player if they'd like to play using a prompt

playing = input(" Do you want to play? ")

# If the user didn't type yes, they don't want to play

if playing.lower() != "yes":
    quit()

# If yes, print an acknowledgement

print("Okay! Let's play :)")


# This program asks the user 5 questions about computer hardware terms.
# It keeps track of the correct answers and displays the final score.

# Initialize score to 0
score = 0

# Question 1: CPU
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Question 2: GPU
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Question 3: RAM
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Question 4: PSU
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Question 5: ROM
answer = input("What is ROM? ")
if answer.lower() == "read-only memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Print the final score
print('You got ' + str(score) + " questions correct")

# Calculate and print the percentage score
print('You got ' + str((score / 5) * 100) + "%.")