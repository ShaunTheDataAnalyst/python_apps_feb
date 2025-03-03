import random

# Constants for game settings
MAX_LINES = 3  # Maximum number of lines a player can bet on
MAX_BET = 100  # Maximum bet per line
MIN_BET = 1    # Minimum bet per line

ROWS = 3  # Number of rows in the slot machine
COLS = 3  # Number of columns in the slot machine

# Dictionary storing the number of each symbol available
symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

# Dictionary storing the payout value of each symbol
symbol_values = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}

# Function to check if the player won
def check_winnings(columns, lines, bet, values):
    winnings = 0  # Stores total winnings
    winning_lines = []  # Stores which lines won

    # Loop through each line the player is betting on
    for line in range(lines):
        symbol = columns[0][line]  # Get the first symbol in the line
        for column in columns:
            symbol_to_check = column[line]  # Check the same row across all columns
            if symbol != symbol_to_check:
                break  # If symbols don't match, break out of the loop
        else:
            # If all symbols match in a line, calculate winnings
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)  # Store the winning line number

    return winnings, winning_lines  # Return total winnings and winning lines

# Function to generate a random slot machine spin
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []  # List of all available symbols
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):  # Add each symbol to the list based on its count
            all_symbols.append(symbol)

    columns = [[] for _ in range(cols)]  # Create empty columns for slot machine

    for i in range(cols):
        column = []
        current_symbols = all_symbols[:]  # Copy the symbol list to modify locally

        for _ in range(rows):
            value = random.choice(current_symbols)  # Randomly pick a symbol
            current_symbols.remove(value)  # Remove chosen symbol to avoid duplicates
            column.append(value)  # Add symbol to the current column

        columns[i] = column  # Assign the generated column to its position

    return columns  # Return the completed slot machine columns

# Function to print the slot machine layout
def print_slot_machine(columns):
    for row in range(len(columns[0])):  # Loop through rows
        for i, column in enumerate(columns):  # Loop through columns
            if i != len(columns) - 1:
                print(column[row], end='|')  # Print symbol with a separator
            else:
                print(column[row], end='|')  # Print last symbol in the row
        print()  # Move to the next row

# Function to get deposit amount from the player
def deposit():
    while True:
        amount = input('What would you like to deposit? $')  # Ask for deposit amount
        if amount.isdigit():  # Ensure input is a valid number
            amount = int(amount)
            if amount > 0:  # Ensure deposit is greater than zero
                return amount  # Return the deposit amount
            else:
                print('Amount must be greater than 0')
        else:
            print('Please enter a number')

# Function to get the number of lines the player wants to bet on
def get_number_of_lines():
    while True:
        lines = input(f'Enter the number of lines to bet on (1-{MAX_LINES}): ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines  # Return valid number of lines
            else:
                print('Enter a valid number of lines')
        else:
            print('Please enter a number')

# Function to get the bet amount per line
def get_bet():
    while True:
        amount = input('What would you like to bet on each line? $')  # Ask for bet
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount  # Return valid bet amount
            else:
                print(f'Amount must be between ${MIN_BET} - ${MAX_BET}')
        else:
            print('Please enter a number')

# Function to handle spinning the slot machine
def spin(balance):
    lines = get_number_of_lines()  # Get number of lines to bet on

    while True:
        bet = get_bet()  # Get bet amount per line
        total_bet = bet * lines  # Calculate total bet

        if total_bet > balance:  # Check if player has enough balance
            print(f'Insufficient funds! You only have ${balance}.')
        else:
            break  # Exit loop if bet is valid

    print(f'You are betting ${bet} on {lines} lines. Total bet: ${total_bet}')
    print(f'Current balance: ${balance}')

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)  # Spin the slot machine
    print_slot_machine(slots)  # Display the slot machine output
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)  # Check for winnings

    print(f'You won ${winnings}')  # Display winnings
    print(f'You won on lines:', *winning_lines)  # Show winning lines

    return winnings - total_bet  # Return net result of the spin

# Main function to run the game
def main():
    balance = deposit()  # Get deposit from the player

    while True:
        print(f'Current balance is ${balance}')  # Display balance
        answer = input('Press enter to play (q to quit).')  # Ask if player wants to continue
        if answer == 'q':  # Quit if player enters 'q'
            break

        balance += spin(balance)  # Perform a spin and update balance

    print(f'You are left with ${balance}')  # Show final balance

# Run the game
main()
