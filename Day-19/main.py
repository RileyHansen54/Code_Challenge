from turtle import Turtle, Screen
import time
import random
#timmy = Turtle()
screen = Screen()

# def move_forwards():
#     timmy.forward(10)
# def move_backwards():
#     timmy.forward(-10)
# def move_right():
#     timmy.right(15)
# def move_left():
#     timmy.left(15)
# def clear():
#     timmy.clear()
#     timmy.penup()
#     timmy.home()
#     timmy.pendown()

# screen.listen()
# screen.onkey(key = "w", fun = move_forwards)
# screen.onkey(key = "s", fun = move_backwards)
# screen.onkey(key = "a", fun = move_left)
# screen.onkey(key = "d", fun = move_right)
# screen.onkey(key = "c", fun = clear)
#COME BACK TO THIS AND MAKE AI TURTLE
screen.setup(width=1000,height = 800)
user_bet = screen.textinput(title="Make your bet",prompt = "which turtle will win the race? Enter a color: ")
#timmy.goto(-380,380)
colors = ["red","green","blue","yellow","orange","purple","black","pink"]
turtles = []
y = 380
for i in range(0,8):
   turtles.append(Turtle(shape="turtle"))
   turtles[i].color(colors[i])
   turtles[i].penup()
   time.sleep(1)
   turtles[i].goto(-380,y)
   turtles[i].pendown()

   y -= 95

while True:
    choice = random.randint(0,7)
    speed = random.randint(5,40)
    turtles[choice].forward(speed)
    if turtles[choice].xcor() > 380:
        print(f"{colors[choice]} Won!!!")
        break
        
if colors[choice] == user_bet:
    print("You bet correctly you win!") 
else:
    print("you lost!")   

screen.exitonclick()  