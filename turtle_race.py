import turtle  # Importing the turtle module to create the racing turtles
import time  # Importing time module to add delay after the race
import random  # Importing random module for generating random movements

# Constants for screen width and height
WIDTH, HEIGHT = 500, 500
# List of possible turtle colors
COLORS = ['red', 'green', 'orange', 'yellow', 'black', 'purple', 'pink', 'blue', 'brown', 'cyan']


def get_number_of_turtles():
    """
    Asks the user for the number of turtles (racers) to participate.
    Ensures the input is a valid number between 2 and 10.
    """
    while True:
        racers = input('Enter the number of racers (2-10): ')  # Ask user for input
        if racers.isdigit():  # Check if input is numeric
            racers = int(racers)  # Convert input to an integer
        else:
            print('Input must be numeric. Try again!')
            continue  # Restart loop if input is not a number

        if 2 <= racers <= 10:  # Check if the number is within the valid range
            return racers  # Return the valid number of racers
        else:
            print('Pick a number in range. Try again')  # Prompt user to enter a valid number


def race(colors):
    """
    Moves the turtles forward randomly until one reaches the finish line.
    Returns the color of the winning turtle.
    """
    turtles = create_turtles(colors)  # Create and position the turtles

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)  # Generate a random movement distance
            racer.forward(distance)  # Move the turtle forward

            # Get the current position of the turtle
            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:  # Check if the turtle has reached the finish line
                return colors[turtles.index(racer)]  # Return the color of the winning turtle


def create_turtles(colors):
    """
    Creates turtle objects, sets their properties, and positions them at the starting line.
    """
    turtles = []  # List to store the turtle objects
    spacingx = WIDTH // (len(colors) + 1)  # Calculate spacing for even positioning

    for i, color in enumerate(colors):  # Loop through the selected colors
        racer = turtle.Turtle()  # Create a new turtle
        racer.color(color)  # Assign a color to the turtle
        racer.shape('turtle')  # Set the turtle shape
        racer.left(90)  # Turn the turtle to face upwards
        racer.penup()  # Lift the pen to move without drawing
        # Position the turtle at the bottom of the screen
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()  # Put the pen down to start drawing the race path
        turtles.append(racer)  # Add the turtle to the list

    return turtles  # Return the list of turtles


def init_turtle():
    """
    Sets up the turtle screen with the specified width, height, and title.
    """
    screen = turtle.Screen()  # Create a screen for the race
    screen.setup(WIDTH, HEIGHT)  # Set screen size
    screen.title('Turtle Racing!')  # Set window title


# Main execution of the program
racers = get_number_of_turtles()  # Get number of racers from the user
init_turtle()  # Initialize the turtle screen

random.shuffle(COLORS)  # Shuffle the color list to randomize turtle colors
colors = COLORS[:racers]  # Select the first 'racers' number of colors

winner = race(colors)  # Start the race and get the winning turtle color
print('The winner is the turtle with color:', winner)  # Display the winner
time.sleep(5)  # Pause for 5 seconds before closing the program
