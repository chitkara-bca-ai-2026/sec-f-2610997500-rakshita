print("=" * 40)
print("       ONLINE ACCOUNT REGISTRATION")
print("=" * 40)

username = input("Enter your username: ")
password = input("Enter your password: ")

length_check = len(password) >= 8
digit_check = any(char.isdigit() for char in password)
uppercase_check = any(char.isupper() for char in password)

print("\n" + "=" * 40)
print("       PASSWORD VALIDATION REPORT")
print("=" * 40)

print("Username:", username)
print("Password:", "*" * len(password))

print("\n--- Validation Rules ---")

if length_check:
    print(f"[PASS] Minimum 8 characters ({len(password)} characters)")
else:
    print(f"[FAIL] Minimum 8 characters ({len(password)} characters)")

if digit_check:
    print("[PASS] At least one digit")
else:
    print("[FAIL] At least one digit")

if uppercase_check:
    print("[PASS] At least one uppercase letter")
else:
    print("[FAIL] At least one uppercase letter")

print("\n--- Result ---")

if length_check and digit_check and uppercase_check:
    print("Password is VALID!")
    print(f"Account created successfully for {username}!")
else:
    print("Password is INVALID!")

print("=" * 40)