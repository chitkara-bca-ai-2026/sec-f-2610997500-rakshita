#Take input from the user
username = input("Enter your username: ")
password = input("Enter your password: ")

# Header Banner
print("========================================")
print("       PASSWORD VALIDATION REPORT")
print("========================================")

# Mask password for display
masked_password = "*" * len(password)
print(f"Username: {username}")
print(f"Password: {masked_password}")

# 2. Check validation rules
# Rule 1: Minimum 8 characters
rule_length = len(password) >= 8

# Rule 2: At least one digit (0-9)
rule_digit = any(char.isdigit() for char in password)

# Rule 3: At least one uppercase letter (A-Z)
rule_upper = any(char.isupper() for char in password)

# 3. Display Validation Rules
print("\n--- Validation Rules ---")

length_status = "[PASS]" if rule_length else "[FAIL]"
print(f"{length_status} Minimum 8 characters ({len(password)} characters)")

digit_status = "[PASS]" if rule_digit else "[FAIL]"
print(f"{digit_status} At least one digit")

upper_status = "[PASS]" if rule_upper else "[FAIL]"
print(f"{upper_status} At least one uppercase letter")

# 4. Display Final Verdict & Result
print("\n--- Result ---")
if rule_length and rule_digit and rule_upper:
    print("Password is VALID!")
    print(f"Account created successfully for {username}!")
else:
    print("Password is INVALID!")

print("========================================")