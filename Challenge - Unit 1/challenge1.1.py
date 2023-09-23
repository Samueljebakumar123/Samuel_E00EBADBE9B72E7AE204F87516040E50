def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Replace 'your_year' with the year you want to check
your_year =int(input("Enter a year:"))
if is_leap_year(your_year):
    print(f"{your_year} is a leap year.")
else:
    print(f"{your_year} is not a leap year.")