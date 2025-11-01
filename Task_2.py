# Program: Number Pyramid Pattern
# Author: Gagan Chandra (Original Work)
# Objective: Generate a pyramid-shaped number pattern using loops.

def number_pyramid():
    print("🔢 Welcome to the Number Pyramid Generator!")
    rows = int(input("Enter the number of rows: "))

    print("\nHere’s your pyramid:\n")
    for i in range(1, rows + 1):
        # Print leading spaces
        for j in range(rows - i):
            print(" ", end="")

        # Print numbers in sequence
        for k in range(1, i + 1):
            print(k, end=" ")

        # Move to the next line
        print()

# Run the program
number_pyramid()
