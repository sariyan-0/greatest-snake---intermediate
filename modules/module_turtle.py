######################## module_turtle.py ########################
# This module provides a simple interface to the turtle graphics library.
import turtle
import random

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
#     t.forward(200)
# ------------------------------
#create a 36 sided polygon
# for i in range(36):
#     t.forward(20)
#     t.left(10)
# ------------------------------
# create a star art that has infinite loops
# for i in range(1000):
#     t.forward(200)
#     t.left(170)
#     t.forward(220)
#     t.left(170)
#     t.backward(260)
#     t.right(175)
# ------------------------------
# create a spiral art that has infinite loops
# t.speed(0)  # Set the turtle's speed to the maximum
# t.color("blue")  # Set the turtle's color to red
# for j in range(1000000):
#     for i in range(10):
#         t.forward(200)
#         t.left(90)
#     t.left(1)
# ------------------------------
# t.speed(0)
# lst_colors = ["red", "blue", "green", "yellow", "cyan", "magenta"]
# for j in range(72):
#     t.color(random.choice(lst_colors))
#     for i in range(10):
#         t.forward(200)
#         t.left(90)
#     t.left(5)
# ------------------------------
# create a line that rotates around the inside of itself (the value should reduce by 10 each time).
# t.speed(0)
# length = 200
# for i in range(20): 
#     t.forward(length)
#     t.left(90)
#     length = length - 10
# ------------------------------
# create a 36 sided polygon
t.speed(0)

length = 20
while length > 0:
    t.forward(length)
    t.left(5)     
    length -= 0.01




turtle.mainloop()
turtle.exitonclick()