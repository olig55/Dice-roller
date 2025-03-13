import random  

with open("dice_results.txt", "w") as file:
    file.write("Roll History:\n")  


def roll_dice():
    return random.randint(1, 6)  

def save_results(rolls):
    with open("dice_results.txt", "a") as file:  
        for num, value in rolls:
            file.write(f"Roll {num}: {value}\n")  


def read_results():
    with open("dice_results.txt", "r") as file:  
        return file.readlines()


def delete_roll(roll_number):
    with open("dice_results.txt", "r") as file:
        lines = file.readlines()

    with open("dice_results.txt", "w") as file:
        for line in lines:
            if not line.startswith(f"Roll {roll_number}:"):
                file.write(line)


def find_rolls(number):
    with open("dice_results.txt", "r") as file:
        results = [line.strip() for line in file if f": {number}" in line]
    
    if results:
        print(f"The number {number} was rolled on:")
        for result in results:
            print(result)
    else:
        print(f"The number {number} was never rolled.")


def calculate_percentages(rolls):
    roll_counts = {i: 0 for i in range(1, 7)}  
    total_rolls = len(rolls)  

    for _, value in rolls:
        roll_counts[value] += 1  

    with open("dice_results.txt", "a") as file:
        file.write("\nRoll Percentages:\n")
        for num, count in roll_counts.items():
            percentage = (count / total_rolls) * 100 if total_rolls > 0 else 0
            file.write(f"Number {num}: {percentage:.2f}%\n")
            print(f"Number {num}: {percentage:.2f}%")  


def dice_simulator():
    print("Welcome to the Dice Rolling Simulator!")  
    rolls = []  
    roll_number = 1  


    previous_rolls = read_results()
    if len(previous_rolls) > 1:
        print("Previous rolls:\n" + "".join(previous_rolls[1:]))

    while True:  
        roll = roll_dice()  
        rolls.append((roll_number, roll))  
        print(f"Roll {roll_number}: You rolled a {roll}")  
        roll_number += 1  

        again = input("Do you want to roll again? (yes/no): ").strip().lower()  
        if again == "no":  
            break  

    save_results(rolls)  
    print("Your rolls have been saved to 'dice_results.txt'.")  

    
    calculate_percentages(rolls)

    
    while True:
        ask = input("Would you like to check which roll got a specific number? (yes/no): ").strip().lower()
        if ask == "no":
            break
        try:
            number = int(input("Enter the number you want to check (1-6): "))
            find_rolls(number)
        except ValueError:
            print("Please enter a valid number.")

   
    while True:
        delete = input("Would you like to delete a roll? (yes/no): ").strip().lower()
        if delete == "no":
            break
        try:
            roll_num = int(input("Enter the roll number you want to delete: "))
            delete_roll(roll_num)
            print(f"Roll {roll_num} has been deleted.")
        except ValueError:
            print("Please enter a valid roll number.")


dice_simulator()
