from turtle import *
import turtle as t

t.colormode(255)
timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")
timmy.speed(0)
timmy.pensize(40)
x = 1
# dummy = Turtle()
# dummy.shape("square")
# dummy.color("red")


def flip(t):
    t.right(90)
    t.forward(10)
    t.right(90)
def square(t):
    t.forward(500)
    for i in range(0 , 4):
        t.forward(1000)
        t.right(90)
def hypno(t,x):
    t.color("blue")
    for i in range(0,1000):
        x += (x/400)
        t.forward(x)
        t.right(3.14159265)
        t.pensize(x+1)
    flip(t)
    t.color("red")
    for i in range(0,1500):
        t.left(3.14159265)
        t.forward(x)
        x -= (x/400)
        timmy.pensize(x)

    flip(t)
    hypno(t,x)
    
from colors import colors
import random


rgb = {'r':{"num":0,"neg": 0},'g':{"num":0,"neg": 0},'b':{"num":0,"neg": 0}}
color = colors
def sequential_color(x):
    val = random.choice(list(x.keys()))
    for key in x:
        if key == val:
            if x[key]["neg"] == 1:
                x[key]["num"] = int((x[key]["num"] - 2.5)%255)
                if x[key]["num"] == 0: 
                    x[key]["neg"] = 0      
            elif x[key]["neg"] == 0:
                x[key]["num"] = int((x[key]["num"] + 2.5)%255)
                if x[key]["num"] == 225: 
                    x[key]["neg"] = 1        
    clr = (rgb['r']["num"],rgb['g']["num"],rgb['b']["num"])
    return clr
    
    
def random_walk(t,size):
    
    num = 0
    t.goto(0,0)
    while True:
        t.color(sequential_color(rgb))
        move_list = ["L","R","U","D"]
        x = t.xcor()
        y = t.ycor()
        choice = random.choice(move_list)
        if choice == "L" and x >-1100:
            t.goto(x-random.randint(5,size),y)
        elif choice == "R" and x < 1100:
            t.goto(x+random.randint(5,size),y)
        elif choice == "U" and y < 755:
            t.goto(x,y+random.randint(5,size))
        elif choice == "D" and y > -755:
            t.goto(x,y-random.randint(5,size))
        if x > 1500 or y >1000:
            t.goto(0,0)
        
def scr(t):
    t.teleport(-1280,700)
    t.color(sequential_color(rgb))
    x = t.xcor()
    y = t.ycor()
    while y> -700:
        while x < 1280:
            t.forward(420)
            x = t.xcor()
            t.color(sequential_color(rgb))
        y = t.ycor()
        t.goto(x,y-40)
        t.right(180)
        while x > -1280:
            t.forward (420)
            x = t.xcor()
            t.color(sequential_color(rgb))
        t.right(180)
        y = t.ycor()
        t.goto(x,y-40)
    
    #t.teleport(-1260,-710)
    x = t.xcor()
    y = t.ycor()
    t.left(90)
    while x < 1260:
        
        while y < 710:
            t.forward(710)
            y = t.ycor()
            t.color(sequential_color(rgb))
        x = t.xcor()
        t.goto(x+40,y)
        t.right(180)
        while y > -710:
            t.forward (710)
            y = t.ycor()
            t.color(sequential_color(rgb))
        t.right(180)
        x = t.xcor()
        t.goto(x+40,y)
    t.right(90)
    return
        
    
color_num = 0  
while True:
    #square(dummy)
    #hypno(timmy,1)
    random_walk(timmy,255)
    # scr(timmy)
    # scr(timmy)
    # scr(timmy)
    # scr(timmy)
    # scr(timmy)
    # scr(timmy)

    
    timmy.screen.mainloop()
    


