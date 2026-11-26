import math

# Header
print("========================================")
print("     ENGINEERING CALCULATION TOOL")
print("========================================")

# Take inputs from user
num_value = float(input("Enter a numerical value: "))
exponent = float(input("Enter an exponent: "))
decimal_val = float(input("Enter a decimal measurement: "))

# Perform mathematical operations
power_result = math.pow(num_value, exponent)
sqrt_result = math.sqrt(num_value)
ceil_result = math.ceil(decimal_val)
floor_result = math.floor(decimal_val)

# Display results
print("\n--- Results ---")
print(f"  Value             : {num_value}")
print(f"  Exponent          : {exponent}")
print(f"  Power (pow)       : {power_result}")
print(f"  Square Root (sqrt): {sqrt_result:.4f}")
print(f"  Decimal Value     : {decimal_val}")
print(f"  Ceil Value        : {ceil_result}")
print(f"  Floor Value       : {floor_result}")
print("========================================")