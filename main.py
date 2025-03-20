import random # allows you to use the functions from Python's built-in random module, which is used to generate random numbers.
#Open the file "dice_results.txt" in write mode ('w'), which will create the file if it doesn't exist, 
# and write the header "Roll History:" to it.
with open("dice_results.txt", "w") as file:
    file.write("Roll History:\n")  


# Define a function named roll_dice that simulates rolling a dice.
def roll_dice():
    # This function returns a random number between 1 and 6 (inclusive), simulating a dice roll.
    return random.randint(1, 6)  

# Define a function named save_results that takes a list of rolls and saves them to the file.
def save_results(rolls):
    # Open the file "dice_results.txt" in append mode ('a'), meaning new data will be added to the end of the file.
    with open("dice_results.txt", "a") as file:
        # Loop through each item in the rolls list, where each item is a tuple containing the roll number and value.
        for num, value in rolls:
            # Write each roll's number and value to the file in the format "Roll X: Y", where X is the roll number and Y is the result.
            file.write(f"Roll {num}: {value}\n")  

# Define a function named read_results that reads and returns the contents of the file.
def read_results():
    # Open the file "dice_results.txt" in read mode ('r') to fetch its contents.
    with open("dice_results.txt", "r") as file:
        # Read all lines from the file and return them as a list of strings.
        return file.readlines()

# Define a function named delete_roll that deletes a specific roll based on its number.
def delete_roll(roll_number):
    # Open the file "dice_results.txt" in read mode ('r') to get the current contents of the file.
    with open("dice_results.txt", "r") as file:
        # Read all lines from the file and store them in a list called 'lines'.
        lines = file.readlines()

    # Open the file again in write mode ('w') to overwrite the file with the updated contents.
    with open("dice_results.txt", "w") as file:
        # Loop through each line in the 'lines' list.
        for line in lines:
            # If the line doesn't start with the specific roll number to delete, write it back to the file.
            if not line.startswith(f"Roll {roll_number}:"):
                file.write(line)

# Define a function named find_rolls that finds and prints the rolls that resulted in a specific number.
def find_rolls(number):
    # Open the file "dice_results.txt" in read mode ('r') to search for specific roll numbers.
    with open("dice_results.txt", "r") as file:
        # Search for lines containing the specific number, stripping extra whitespace from the lines.
        results = [line.strip() for line in file if f": {number}" in line]
    
    # If there are any results that match the number, print the dates and times they were rolled.
    if results:
        print(f"The number {number} was rolled on:")
        # Loop through each matching result and print it.
        for result in results:
            print(result)
    else:
        # If no results are found, inform the user that the number was never rolled.
        print(f"The number {number} was never rolled.")

# Define a function named calculate_percentages that calculates the percentage of each dice roll outcome.
def calculate_percentages(rolls):
    # Create a dictionary with keys as numbers from 1 to 6, initializing each count to 0.
    roll_counts = {i: 0 for i in range(1, 7)}
    # Calculate the total number of rolls by getting the length of the rolls list.
    total_rolls = len(rolls)

    # Loop through each roll in the rolls list.
    for _, value in rolls:
        # Increment the count for the rolled number in the roll_counts dictionary.
        roll_counts[value] += 1  

    # Open the file "dice_results.txt" in append mode ('a') to write the calculated percentages at the end.
    with open("dice_results.txt", "a") as file:
        file.write("\nRoll Percentages:\n")  # Write a header for the percentages section.
        # Loop through each dice number (1-6) and its count in the roll_counts dictionary.
        for num, count in roll_counts.items():
            # Calculate the percentage for each number. If there were no rolls, the percentage is set to 0.
            percentage = (count / total_rolls) * 100 if total_rolls > 0 else 0
            # Write the calculated percentage for each number to the file.
            file.write(f"Number {num}: {percentage:.2f}%\n")
            # Print the calculated percentage to the screen.
            print(f"Number {num}: {percentage:.2f}%")  

# Define the main function of the dice simulator.
def dice_simulator():
    # Print a welcome message for the dice rolling simulator.
    print("Welcome to the Dice Rolling Simulator!")  
    rolls = []  # Initialize an empty list to store the rolls.
    roll_number = 1  # Set the starting roll number to 1.

    # Read the previous rolls from the file.
    previous_rolls = read_results()
    # If there are previous rolls, print them, excluding the header line.
    if len(previous_rolls) > 1:
        print("Previous rolls:\n" + "".join(previous_rolls[1:]))

    # Start a loop to continuously ask the user if they want to roll the dice.
    while True:
        # Simulate rolling the dice by calling the roll_dice function.
        roll = roll_dice()
        # Append the roll number and the roll value to the rolls list.
        rolls.append((roll_number, roll))
        # Print the result of the current roll to the screen.
        print(f"Roll {roll_number}: You rolled a {roll}")
        roll_number += 1  # Increment the roll number.

        # Ask the user if they want to roll again.
        again = input("Do you want to roll again? (yes/no): ").strip().lower()
        if again == "no":  # If the user says "no", break the loop and stop rolling.
            break  

    # Save the rolls to the file.
    save_results(rolls)  
    # Print a confirmation message that the rolls have been saved.
    print("Your rolls have been saved to 'dice_results.txt'.")  

    # Calculate and print the percentages of each dice number.
    calculate_percentages(rolls)

    # Start a loop to allow the user to check which rolls resulted in a specific number.
    while True:
        # Ask the user if they want to check for a specific number.
        ask = input("Would you like to check which roll got a specific number? (yes/no): ").strip().lower()
        if ask == "no":  # If the answer is "no", break the loop.
            break
        try:
            # Ask the user to enter a number between 1 and 6.
            number = int(input("Enter the number you want to check (1-6): "))
            # Call the find_rolls function to display the rolls that resulted in the chosen number.
            find_rolls(number)
        except ValueError:  # If the user enters something other than a valid number.
            print("Please enter a valid number.")  # Inform the user to enter a valid number.

    # Start a loop to allow the user to delete a specific roll.
    while True:
        # Ask the user if they want to delete a roll.
        delete = input("Would you like to delete a roll? (yes/no): ").strip().lower()
        if delete == "no":  # If the answer is "no", break the loop.
            break
        try:
            # Ask the user for the roll number they want to delete.
            roll_num = int(input("Enter the roll number you want to delete: "))
            # Call the delete_roll function to remove the specified roll from the file.
            delete_roll(roll_num)
            # Print a message confirming the roll has been deleted.
            print(f"Roll {roll_num} has been deleted.")
        except ValueError:  # If the user enters something other than a valid number.
            print("Please enter a valid roll number.")  # Inform the user to enter a valid roll number.

# Call the dice_simulator function to start the dice simulation process.
dice_simulator()
