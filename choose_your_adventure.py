# Get user's name
name = input('Type your name: ')
print('Welcome', name, 'to this adventure')

# First choice: Left or Right
answer = input('You are on a dirt road. It has come to an end and you can go left or right. Which way would you like to go? ')

# If the user chooses to go left
if answer == 'left':
    # Choice at the river
    answer = input('You come across a river. You can walk around it or swim across: ')
    # Determine the outcome based on the river choice
    if answer == 'swim':
        print('You swam across and were eaten by an alligator')
    elif answer == 'walk':
        print('You walked for many miles, ran out of water and you lost the game')
    else:
        print('Not a valid option. You Lose')

# If the user chooses to go right
elif answer == 'right':
    # Choice at the bridge
    answer = input('You come to a bridge, it looks wobbly. Do you want to cross it or head back? (cross/back)? ')
    if answer == 'cross':
        print('You go back and lose')
    elif answer == 'back':
        # Choice to talk to the stranger
        answer = input('You cross the bridge and meet a stranger. Do you talk to them?(yes/no) ')
        if answer == 'yes':
            print('You talk to the stranger and they give you gold. You WIN!')
        elif answer == 'no':
            print('You ignore the stranger and they are offended and you lose')
    else:
        print('Not a valid option. You Lose')

# If the initial choice is neither left nor right
else:
    print('Not a valid option. You lose')

# End the game
print('Thank you for trying,', name)