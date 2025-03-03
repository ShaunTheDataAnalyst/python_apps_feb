# Open the 'story.txt' file in read mode with UTF-8 encoding
with open('story.txt', 'r', encoding="utf-8") as f: 
    story = f.read()  # Read the entire file and store it in the 'story' variable

# Create an empty set to store placeholder words (e.g., <noun>, <verb>)
words = set()
start_of_word = -1  # Keeps track of where a placeholder word starts

# Define the symbols used for placeholders in the story
target_start = '<'  # Opening tag for a placeholder
target_end = '>'    # Closing tag for a placeholder

# Loop through every character in the story
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i  # Mark the position where a placeholder starts

    if char == target_end and start_of_word != -1:
        # Extract the placeholder word including < and >
        word = story[start_of_word: i + 1]  
        words.add(word)  # Add the placeholder to the set (avoiding duplicates)
        start_of_word = -1  # Reset start_of_word

# Dictionary to store user inputs for each placeholder word
answers = {}

# Ask the user to provide a word for each placeholder
for word in words:
    answer = input('Enter a word for ' + word + ': ')  # Prompt user
    answers[word] = answer  # Store the answer in the dictionary

# Replace each placeholder in the story with the user’s input
for word in words:
    story = story.replace(word, answers[word])

# Print the final, completed story with user inputs
print(story)
