rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
choices = [rock , paper , scissors]
pick = input("Choose Rock Paper or Scissor\n")
Rand = random.choice(choices)


if pick == "Rock":
    print(rock)
    print(Rand)
    if Rand == rock:
        print("\nTie")
    elif Rand == paper:
        print("\nYou Lose")
    else:
        print("\nYou Win")
elif pick == "Paper":
    print(paper)
    print(Rand)
    if Rand == paper:
        print("\nTie")
    elif Rand == scissors:
        print("\nYou Lose")
    else:
        print("\nYou Win")
elif pick == "Scissors":
    print(scissors)
    print(Rand)
    if Rand == scissors:
        print("\nTie")
    elif Rand == rock:
        print("\nYou Lose")
    else:
        print("\nYou Win")
else:
    print("Wrong Choice")
