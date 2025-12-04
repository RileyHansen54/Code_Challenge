print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the roller coaster")
else:
    print(f"You need to be {120-height} more inches to ride the roller coaster")
