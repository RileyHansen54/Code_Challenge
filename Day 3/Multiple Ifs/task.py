print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))

    if age <= 12:
        print("Tickets cost $5.")
        bill = 5

    elif age <= 18:
        print("Tickets cost $7.")
        bill = 7

    else:
        print("Tickets cost $12.")
        bill = 12

    choice = input("Would you like photos? type y/n")
    if choice == "y":
        bill += 3
        print(f"please pay ${bill}")
    else:
        print(f"please pay ${bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
