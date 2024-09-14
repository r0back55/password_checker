# Checking the strength of the password

password = input("Enter new password: ")

# Prompt user to customize special characters
custom_special_characters = input("Enter allowed special characters (leave empty for default set): ")
if not custom_special_characters:
    custom_special_characters = "!@#$%^&*()-+?_=,<>/"

# Initialize result variables
digit_count = 0
has_upper_case = False
has_lower_case = False
has_special_char = False

# Minimum digit requirement
min_digits = 2

# Check conditions in one loop
for char in password:
    if char.isdigit():
        digit_count += 1
    elif char.isupper():
        has_upper_case = True
    elif char.islower():
        has_lower_case = True
    elif char in custom_special_characters:
        has_special_char = True

# Checking the length after the loop
is_valid_length = len(password) >= 8
has_min_digits = digit_count >= min_digits

# Count the number of conditions met
conditions_met = 0
if is_valid_length:
    conditions_met += 1
if has_min_digits:
    conditions_met += 1
if has_upper_case:
    conditions_met += 1
if has_lower_case:
    conditions_met += 1
if has_special_char:
    conditions_met += 1

# Determine password strength based on the number of conditions met
if conditions_met == 5:
    strength = "Strong"
elif conditions_met >= 3:
    strength = "Medium"
else:
    strength = "Weak"

# Final feedback
print(f"Password strength: {strength}")
if strength == "Weak":
    print("Weak Password. Issues with:")
    if not is_valid_length:
        print("- Password should be at least 8 characters long.")
    if not has_min_digits:
        print(f"- Password should contain at least {min_digits} digits.")
    if not has_upper_case:
        print("- Password should contain at least one uppercase letter.")
    if not has_lower_case:
        print("- Password should contain at least one lowercase letter.")
    if not has_special_char:
        print(f"- Password should contain at least one special character from the set: {custom_special_characters}.")
elif strength == "Medium":
    print("Password is acceptable but could be improved.")
