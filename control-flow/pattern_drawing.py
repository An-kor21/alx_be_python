# pattern_drawing.py

# Prompt the user for the size of the pattern
pattern_size = int(input("Enter the size of the pattern: "))

# Initialize row counter for the while loop
row = 0

# Use while loop to handle rows
while row < pattern_size:
    # Use for loop to handle columns in each row
    for col in range(pattern_size):
        print("*", end="")
    # Move to the next line after finishing one row
    print()
    row += 1
