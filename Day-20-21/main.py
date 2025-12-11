from turtle import Screen, Turtle
import time
import random
from snake import Snake
from food import Food
screen = Screen()
SCORE = 0

screen.setup(width=900, height=900)
screen.bgcolor("black")
screen.title("snakegame")
screen.tracer(0)


game_on = True

scorebord = Turtle()
scorebord.goto(0,415)
scorebord.color("white")
scorebord.hideturtle()
scorebord.write(f"Score: {SCORE}",move = False, align="center",font=("Arial",24,"normal"))

def scorebord_update():
    global SCORE
    scorebord.clear()
    SCORE +=1
    scorebord.write(f"Score: {SCORE}",move = False, align="center",font=("Arial",24,"normal"))
   
screen.update()

snake = Snake()
food = Food()

    


screen.listen()
screen.onkey(key = "w", fun = snake.setup)
screen.onkey(key = "s", fun = snake.setdown)
screen.onkey(key = "a", fun = snake.setleft)
screen.onkey(key = "d", fun = snake.setright)
# segments[0].color("red")
# segments[1].color("blue")
# segments[2].color("green")



while game_on:
    screen.update()
    snake.move_forward()
    time.sleep(.001)
    if snake.segments[0].xcor()>=450 or snake.segments[0].xcor()<=-450 or snake.segments[0].ycor()>=450 or snake.segments[0].ycor()<=-450:
        break
    if snake.segments[0].distance(food)<15:
        food.spawn_food()
        snake.grow()
        scorebord_update()
        
