import curses
import random
from curses import wrapper
import time

# Function to display the start screen
def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr('Welcome to the Speed Typing Test!')  # Display welcome message
    stdscr.addstr('\nPress any key to begin!')  # Prompt user to start
    stdscr.refresh()
    stdscr.getkey()  # Wait for key press to proceed

# Function to display the text, current input, and WPM
def display_text(stdscr, target, current, wpm=0):
    stdscr.clear()  # Clear the screen before updating
    stdscr.addstr(target)  # Display target text
    stdscr.addstr(1, 0, f'WPM: {wpm}')  # Show words per minute

    # Loop through each character typed by the user
    for i, char in enumerate(current):
        correct_char = target[i]  # Get the correct character
        color = curses.color_pair(1) if char == correct_char else curses.color_pair(2)  # Set color based on correctness
        stdscr.addstr(0, i, char, color)  # Display typed character with color

    stdscr.refresh()  # Refresh screen to update changes

# Function to load a random line from the text file
def load_text():
    with open('wpm_text.txt', 'r') as f:
        lines = f.readlines()  # Read all lines from file
        return random.choice(lines).strip()  # Select a random line and remove whitespace

# Function to handle the typing test
def wpm_test(stdscr):
    target_text = load_text()  # Load a random text for the test
    current_text = []  # List to store user's input
    wpm = 0  # Initialize WPM to zero
    start_time = None  # Start time will be set when the user starts typing
    stdscr.nodelay(True)  # Enable non-blocking input (no waiting for keypress)

    while True:
        # Start calculating WPM only after first key press
        if start_time:
            time_elapsed = max(time.time() - start_time, 1)  # Calculate elapsed time
            wpm = round((len(current_text) / (time_elapsed / 60)) / 5)  # WPM formula

        display_text(stdscr, target_text, current_text, wpm)  # Update screen with text and WPM

        # Check if user has completed the text
        if ''.join(current_text) == target_text:
            stdscr.nodelay(False)  # Disable non-blocking input
            break  # End test

        try:
            key = stdscr.getkey()  # Get user input
        except:
            continue  # Ignore errors and continue loop

        if ord(key) == 27:  # If Escape key is pressed, exit test
            break
        if key in ('KEY_BACKSPACE', '\b', '\x7f'):  # Handle backspace
            if len(current_text) > 0:
                current_text.pop()  # Remove last character
        elif len(current_text) < len(target_text):  # Only allow input up to target text length
            if start_time is None:  # Start timer on first key press
                start_time = time.time()
            current_text.append(key)  # Add typed character to list

# Main function to initialize colors and start the program
def main(stdscr):
    # Set up color pairs for text display
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Correct text color
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)  # Incorrect text color
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Default text color

    start_screen(stdscr)  # Show the welcome screen

    while True:
        wpm_test(stdscr)  # Run the typing test
        stdscr.addstr(2, 0, 'You completed the task! Press any key to continue.')  # Display completion message
        key = stdscr.getkey()  # Wait for user input

        if ord(key) == 27:  # If Escape key is pressed, exit program
            break

wrapper(main)  # Start the program
