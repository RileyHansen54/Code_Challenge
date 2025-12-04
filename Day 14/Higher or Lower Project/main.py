import game_data
import art
import random


def new(xx, yy):
    while xx == yy:
        yy = random.choice(data)
    return yy
def followers(A, B):
    while True:
        try:
            x = input("Who has more followers? Type 'A' or 'B': ").lower()
            break
        except x != 'a' or x != 'b':
            print("try again ")
    if x == 'a':
        if A["follower_count"] > B["follower_count"]:
            return 1
        else:
            return 0
    else:
        if A["follower_count"] < B["follower_count"]:
            return 1
        else:
            return 0

print(art.logo)
data = game_data.data
def game():
    A = random.choice(data)
    B = A
    B = new(A,B)
    score = 0
    while True:
        print(f"Compare A: {A["name"]} a {A["description"]} from {A["country"]}")
        print(art.vs)
        print(f"Compare B: {B["name"]} a {B["description"]} from {B["country"]}")
        val = followers(A,B)
        if val == 1:
            score +=1
            print("\n" * 20)
            print(art.logo)
            print(f"You're right! Current score: {score}")
        elif val == 0:
            print("\n" * 20)
            print(art.logo)
            print(f"You're wrong... Final score: {score}")
            exit()
        for x in range (0, len(data)-1):
            if data[x] == A:
                data.pop(x)
        A = B
        B = new(A,B)
game()




