print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

def Pizza (x):
    if pepperoni == "Y":
        x += 2
    else:
        x = x

    if extra_cheese == "Y":
        x += 1
    else:
        x = x
    return x



if size == "S":
    bill = 15
    bill = Pizza(bill)


elif size == "M":
    bill = 20
    bill = Pizza(bill)
else:
    bill = 25
    bill = Pizza(bill)

print(f"your total is {bill}")

