import random
import os
op_sys = os.name
line = "----------------------------------------------------------"

# Asks the user to input the number of dice

dice_nr = input('Number of dice: \n \n')

# Jumps into a loop

while True:

    # Clears the screen

    if op_sys == "nt":
        os.system("cls")            # For Windows
    else:
        os.system('clear')          # For Linux    

    if dice_nr.isdigit():           # Checks if the input is a natural number

        # Jumps into a loop inside the loop (so the user can reroll or change the number of dice in use)

        while True:
            if dice_nr.isdigit():   # Again checks if the input is a natural number (If the user changes the number of dice in use)

                # Clears the screen

                if op_sys == "nt":
                    os.system("cls")
                else:
                    os.system('clear')
                
                dice_object = {}    # Initiates a dice object that will store the all the possible outcomes of a roll for a single die
                print("\nYou have selected", dice_nr, "dice.")  # Prints out the number of dice chosen by the user
                print(line)         # Prints a line for clearer readability
                roll_nr = random.sample(range(1, 43), int(dice_nr)) # Simulates a roll with a maximum of 43 spin for a single die
                iterator = 0        # This will be the helper that will be used as key in the dice object that stores all the die sub objects
                for roll in roll_nr:    # Iterates through the simulated spins
                    die_object = {}     # Initiates a die sub object that will store all the numbers that pop up during the spin
                    rng = range(roll)   # Gets the number of spins
                    for r in rng:       # For every single spin
                        r_side = random.randint(1, 6)   # Generates a number between 1 and 6 (just as it happens with a real die)
                        die_object[r] = r_side          # And pushes all the generated numbers from the spin into the die sub object
                    dice_object[iterator] = die_object  # Pushes the die sub object into the main dice object
                    iterator = iterator + 1             # Iterates for the next key in line

                for element in dice_object:             # For every element in the main dice object
                    size_index = len(dice_object[element]) -1   # Counts the size of the die sub object so we can grab it as the last value from a single die's last spin
                    print("Die", element + 1,": ", dice_object[element][size_index])    # Prints out the die with it's value from the point where the simulated spinning stopped
                print(line)          # Prints a line for clearer readability
                roq = input('[R]eroll, [C]hange dice quantity or [Q]uit? \n \n')  # Asks the user to input if (s)he wants to Roll again, change the number of dice or quit
                if roq.upper() == "R": 
                    continue    # The letter r/R restarts the loop which triggers a reroll
                elif roq.upper() == "C": 
                    if op_sys == "nt":  
                        os.system("cls")
                    else:
                        os.system('clear')                   
                    dice_nr = input('New number of dice: \n \n') # The letter c/C lets the user to input a new number for the dice quantity 
                    continue                                     # and sends it back to the beginning of the loop with the new amount    
                elif roq.upper() == "Q":    # The letter Q
                    # Clears the screen
                    if op_sys == "nt":
                        os.system("cls")
                    else:
                        os.system('clear')
                    print("ok Byeee")       # Says goodbye 
                    break                   # And stops the program    
                else:   # If the user inputs anything else, the program stops                   
                    if op_sys == "nt":
                        os.system("cls")
                    else:
                        os.system('clear')
                    print("That means nothing...")                
                    print("Bye")
                    break  
            else:
                # Clears the screen
                if op_sys == "nt":
                    os.system("cls")
                else:
                    os.system('clear')
                # Notifies the user that the given number is invalid
                print("Keep your numbers natural please...")
                # Asks for a new number
                dice_nr = input('Number of dice: \n \n')
                # Sends it back to the beginning of the loop
                continue
        break
    else:
        # Clears the screen
        if op_sys == "nt":
            os.system("cls")
        else:
            os.system('clear')
        # Notifies the user that the given number is invalid
        print("Keep your numbers natural please.")
        # Asks for a new number
        dice_nr = input('Number of dice: \n \n')
        # Sends it back to the beginning of the loop
        continue
