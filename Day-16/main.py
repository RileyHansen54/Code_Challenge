# from turtle import *
# import another_module
# print(another_module.another_variable)

# def move_forward():
#     timmy.forward(100)
# timmy = Turtle()
# timmy.shape("turtle")
# myscreen = Screen()

# myscreen.exitonclick()

# myscreen.listen()
# myscreen.onkey(move_forward, 'w')  # Pass the function, don't call it
# myscreen.exitonclick()



# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.speed("fastest")  # Makes movement smoother
# myscreen = Screen()

# # Enable listening for key presses
# myscreen.listen()

# # Movement controls (WASD)
# myscreen.onkey(lambda: timmy.forward(30), 'w')   # Move forward
# myscreen.onkey(lambda: timmy.backward(30), 's')  # Move backward
# myscreen.onkey(lambda: timmy.left(90), 'a')      # Turn left
# myscreen.onkey(lambda: timmy.right(90), 'd')     # Turn right

# # Bonus: Clear screen with 'c'
# myscreen.onkey(lambda: timmy.clear(), 'c')

# myscreen.exitonclick()



from prettytable import PrettyTable

table = PrettyTable()
print(table)

table.add_column("Pokemon", ["Charmander","Squirtle","Bulbasaur"])
table.add_column("Type", ["Fire","Water","Earth"])
print(table)

print(table.align)

table.align = "l"
print(table)
print(table.align)

