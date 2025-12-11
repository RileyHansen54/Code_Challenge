from turtle import *
import random
screen = Screen()
import time
# screen.setup(width=2000, height=1200)
# screen.bgcolor("black")

# screen.title("My Snake game")
# i = 0
# snake = []
# ball = Turtle("circle")
# ball.color("blue")
# ball.teleport(400,400)
# ball.shape("circle")
# snakehead= Turtle()
# snakehead.shape("square")
# snakehead.color("white")
# snakehead.teleport(0,0)
# def move_up():
#     x = snakehead.xcor()
#     y = snakehead.ycor()
#     snakehead.teleport(int(x),int(y+20))
# def move_down():
#     x = snakehead.xcor()
#     y = snakehead.ycor()
#     snakehead.teleport(int(x),int(y-20))
# def move_right():
#     x = snakehead.xcor()
#     y = snakehead.ycor()
#     snakehead.teleport(int(x+20),int(y))
# def move_left():
#     x = snakehead.xcor()
#     y = snakehead.ycor()
#     snakehead.teleport(int(x-20),int(y))
    
# def setup():
#     snakehead.setheading(90)
#     time.sleep(.1)
# def setdown():
#     snakehead.setheading(270)
#     time.sleep(.1)

# def setleft():
#     snakehead.setheading(180)
#     time.sleep(.1)
# def setright(): 
#     snakehead.setheading(0)
#     time.sleep(.1)

    
    
        
    
# def move():
#     #snakehead.forward(20)
#     if snakehead.heading()==int(90):
#         move_up()
#         if len(snake)>0:
#             snake[0].hideturtle()
#             snake.pop(0)
#             add_snake()
#     elif snakehead.heading()==int(270):
#         move_down()
#         if len(snake)>0:
#             snake[0].hideturtle()
#             snake.pop(0)
#             add_snake()
#     elif snakehead.heading()==int(180):
#         move_left()
#         if len(snake)>0:
#             snake[0].hideturtle()
#             snake.pop(0)
#             add_snake()
#     elif snakehead.heading()==int(0):
#         move_right()
#         if len(snake)>0:
#             snake[0].hideturtle()
#             snake.pop(0)
#             add_snake()
    
# def add_snake():
#     x = Turtle()
#     x = snakehead.clone()
#     #x.teleport(snakehead.xcor(),snakehead.ycor())
#     snake.append(x)
# def checkpos():
#     if snakehead.pos() == ball.pos():
#         bx = 1
#         by = 1
#         while bx % 20 != 0:
#             bx = random.randint(-1000,1000)
#         while by % 20 != 0:
#             by = random.randint(-500,500)
#         ball.teleport(bx,by)
#         add_snake()
#         #addsnake
    

# screen.listen()
# screen.onkey(key = "w", fun = setup)
# screen.onkey(key = "s", fun = setdown)
# screen.onkey(key = "a", fun = setleft)
# screen.onkey(key = "d", fun = setright)



# while True:
#     move()
#     checkpos()

# screen.exitonclick()

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING = [(0,0),(-20,0),(-40,0)]

class Snake:
    def __init__(self):
        self.segments = []  
        self.create_snake()
  
    def setup(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(90)
    def setdown(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(270)
    def setleft(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(180)
    def setright(self): 
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(0)
    
    def create_snake(self): 
        for position in STARTING:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    def move_forward(self):
        for x in range(len(self.segments)-1, 0, -1):
            self.segments[x].goto(self.segments[x-1].pos())
        self.segments[0].forward(20)
        screen.update()
        time.sleep(0.1)
        
    def grow(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        self.segments.append(new_segment)