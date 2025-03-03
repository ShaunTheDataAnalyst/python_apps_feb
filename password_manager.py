from cryptography.fernet import import Fernet

# Function to view saved passwords

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file
        key_file.write(key)

def load_key():
file = open("key.key", "rb")
key = file.read()
file.close()
return key


master_pwd = input('What is the master password? ')
key = load_key() + mater_pwd.encode
fer = Fernet(key)

def view():
    try:
        with open('passwords.txt', 'r') as f:  # Open the file in read mode
            for line in f.readlines():         # Read each line from the file
                data = line.rstrip()           # Remove any trailing whitespace (like newlines)
                if '|' in data:                # Check if the '|' separator exists in the line
                    user, passw = data.split('|', 1)  # Split the line into user and password at the first '|'
                    print(f'Account: {user}, Password: {passw}')  # Display the account and password
                else:
                    print('Invalid entry found in file.')  # Handle any lines without proper formatting
    except FileNotFoundError:  # If the file doesn't exist, handle the error
        print('No passwords saved yet.')

# Function to add a new password
def add():
    name = input('Account Name: ')  # Prompt user for the account name
    pwd = input('Password: ')       # Prompt user for the password

    with open('passwords.txt', 'a') as f:  # Open the file in append mode to add new entries
        f.write(name + '|' + str(fer.encrypt(pwd.encode()) + '\n')  # Write the account and password, separated by '|', followed by a newline

# Main loop to handle user input
while True:
    mode = input('Would you like to add a new password or view existing ones (view/add)? Press q to quit: ').lower()  # Ask user for action
    if mode == 'q':  # If the user wants to quit
        print('Exiting password manager. Goodbye!')
        break  # Exit the loop
    elif mode == 'view':  # If the user wants to view passwords
        view()
    elif mode == 'add':   # If the user wants to add a new password
        add()
    else:
        print('Invalid mode. Please choose "view", "add", or "q" to quit.')  # Handle invalid inputs