#this is a program which lets you know whether you are elgible to register for a summre program

year_of_birth = input("Enter your year of birth:")
current_year=2020
diff_year = (current_year-int(year_of_birth))

if diff_year > 20:
    print("You are eligible to register")
else:
    print("You are not eligible to register as you are only "+ str(diff_year) + " years old ")
