import random

attempt = 0

def play(guess, inp):
    global attempt
    guess = int(guess)
    if inp < guess:
        attempt -= 1
        print(f"Too High.\nGuess again.\nYou have {attempt} attempts remaining to guess the number")
    elif inp > guess:
        attempt -= 1
        print(f"Too Low.\nGuess again.\nYou have {attempt} attempts remaining to guess the number")
    elif inp == guess:
        print(f"You won!")
        return True
    return False

def game(x):
    global attempt
    if x == "easy":
        attempt = 10
    elif x =="hard":
        attempt = 5
    num = random.randint(0,100)
    y = False
    while play(input("Make a guess "),num) != True and attempt > 0:
        print("")


    if attempt <=0:
        print(f"You ran out of attempts. You Lose\nThe number was {num}")

while input("Would you like to play a number guessing game? y/n ") != "n":
    game(input("Select your difficulty: Easy or Hard ").lower())
    print("Play again? ")
print("Goodbye")
