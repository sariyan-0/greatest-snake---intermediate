######################## module_turtle.py ########################
# This module provides a simple interface to the turtle graphics library.
import turtle

screen = turtle.Screen()
turtle.hideturtle()  # Hide the turtle cursor
t = turtle.Turtle()
# ------------------------------
# t.forward(200)  # Move the turtle forward by 200 units
# t.left(90) # Move the turtle to the left
# t.forward(200)
# t.left(90)
# t.forward(200)
# t.left(90)
# t.forward(200)

# for i in range(4):
#     t.forward(200)
#     t.left(90)
# ------------------------------
# create a triangle
# for i in range(3):
#     t.forward(200)
#     t.left(60)
# ------------------------------
# create a hexagon
# for i in range(6):
#     t.forward(200)
#     t.left(60)
# ------------------------------
#create a 36 sided polygon
for i in range(36):
    t.forward(20)
    t.left(10)
# ------------------------------
turtle.mainloop()