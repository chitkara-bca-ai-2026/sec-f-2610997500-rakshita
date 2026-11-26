print("=" * 40)
print("       CALENDAR VERIFICATION SYSTEM")
print("=" * 40)

year = int(input("Enter year: "))

if year <= 0:
    print("Error: Year must be a positive integer greater than 0.")
else:
    if year % 400 == 0:
        leap_year = True
        reason = "Divisible by 400"
    elif year % 100 == 0:
        leap_year = False
        reason = "Century year not divisible by 400"
    elif year % 4 == 0:
        leap_year = True
        reason = "Divisible by 4 and not a century year"
    else:
        leap_year = False
        reason = "Not divisible by 4"

    if leap_year:
        status = "LEAP YEAR"
        feb_days = 29
        total_days = 366
    else:
        status = "COMMON YEAR"
        feb_days = 28
        total_days = 365

    print("\n" + "-" * 40)
    print("Year:", year)
    print("Status:", status)
    print("Days in Year:", total_days)
    print("Days in February:", feb_days)
    print("Reason:", reason)
    print("-" * 40)