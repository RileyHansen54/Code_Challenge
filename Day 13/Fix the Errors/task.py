
try:
    age = int(input("How old are you?"))
except ValueError:
    age = int(input("You have typed in a invalid age. please type in your answer with a numerical symbol 1-100 or 1000 if your yoda"))
if age > 18:
    print(f"You can drive at age {age}.")
