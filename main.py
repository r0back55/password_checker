# Checking the strength of the password

password = input("Enter new password: ")


def password_history():
    with open("./used_passwords.txt", "r") as file_read:
        lines = file_read.readlines()
    return lines


# List of the last 10 passwords
pass_history = password_history()

for element in pass_history:
    element.strip("\n")

    while element in pass_history:
        print("Password used not so long ago.")
        password = input("Enter new password: ")
    else:
        if len(pass_history) == 10:
            pass_history.pop(0)
            pass_history.append(password + "\n")

            with open("./used_passwords.txt", "w") as file:
                used_passwords = file.writelines(pass_history)
        else:
            pass_history.append(password + "\n")
            with open("./used_passwords.txt", "w") as file:
                used_passwords = file.writelines(pass_history)

# List of common weak passwords
common_passwords = [
    "123456", "password", "123456789", "12345678", "12345", "1234567", "qwerty", "abc123", "password1", "letmein"
]

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

# Check if the password is common
is_common_password = password in common_passwords

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
if is_common_password:
    strength = "Weak (Common Password)"
elif conditions_met == 5:
    strength = "Strong"
elif conditions_met >= 3:
    strength = "Medium"
else:
    strength = "Weak"

# Final feedback
print(f"Password strength: {strength}")
if strength.startswith("Weak"):
    print("Weak Password. Issues with:")
    if is_common_password:
        print("- Password is too common and easily guessable.")
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
