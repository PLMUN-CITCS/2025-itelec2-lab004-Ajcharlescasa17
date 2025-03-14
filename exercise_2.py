"""
Laboratory #04 - Guided Coding Exercise
Topic: Input, Output, and Text Formatting in Python
"""

# Step 1: Get user input
user_integer = int(input("Enter an integer: "))  # Convert input to integer
user_decimal = float(input("Enter a decimal number: "))  # Convert input to float
user_text = input("Enter a string: ")  # Input remains a string

# Step 2: Display formatted output using old-style formatting (% operator)
print("\nFormatted Output using old-style formatting:")
print("Integer: %d" % user_integer)
print("Decimal: %.2f" % user_decimal)  # Format to 2 decimal places
print("String: %s" % user_text)

# Step 3: Display formatted output using f-strings (modern approach)
print("\nFormatted Output using f-strings:")
print(f"Integer: {user_integer}")
print(f"Decimal: {user_decimal:.2f}")  # Format to 2 decimal places
print(f"String: {user_text}")