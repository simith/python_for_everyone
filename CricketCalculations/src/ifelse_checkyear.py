#this is a program which lets you know whether you are elgible to register for a summre program

current_year=2020
min_registration_year = current_year - 100
max_registration_year = current_year

year_of_birth = input("Enter your year of birth (For eg. 1996):")

if (int(year_of_birth) < min_registration_year) or (int(year_of_birth) > max_registration_year):
    print("Your age does not look good to me")
    exit(0)

diff_year = (current_year-int(year_of_birth))

if diff_year > 20:
    print("You are eligible to register")
else:
    print("You are not eligible to register as you are only "+ str(diff_year) + " years old ")
