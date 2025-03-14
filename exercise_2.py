# Get integer input
user_integer = int(input("Enter an integer: "))

# Get decimal (float) input
user_decimal = float(input("Enter a decimal number: "))

# Get string input
user_text = input("Enter a string: ")

# Display formatted output using old-style formatting
print("Formatted Output using old-style formatting:")
print("Integer: %d" % user_integer)
print("Decimal: %.2f" % user_decimal)
print("String: %s" % user_text)

# Display formatted output using f-strings (modern approach)
print("Formatted Output using f-strings:")
print(f"Integer: {user_integer}")
print(f"Decimal: {user_decimal:.2f}")  # Format decimal to two decimal places
print(f"String: {user_text}")