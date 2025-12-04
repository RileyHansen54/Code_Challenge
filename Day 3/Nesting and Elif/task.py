print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("How old are you? "))

if height >= 120:
    if age > 18:
        print("You can ride the rollercoaster for 12$")
    elif age < 18 and age >12:
        print("You can ride the rollercoaster for 7$")
    else:
        print("You can ride the rollercoaster for 5$")


else:
    print("Sorry you have to grow taller before you can ride.")
