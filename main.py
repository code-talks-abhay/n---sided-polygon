from turtle import Turtle, Screen

# Importing the Turtle and Screen from module turtle

tm = Turtle()
# Creating object

side = int(input("Enter the side of polygon:"))

angle = 360 / side
# Calculation of angle

for _ in range(side):
    tm.fd(50)  # To draw the side
    tm.right(angle)  # To move the turtle to required angle after drawing the side
screen = Screen()
screen.exitonclick()
# To exit after click
