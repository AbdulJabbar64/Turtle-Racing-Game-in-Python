from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.title("Turtle Race Game")
screen.setup(width=700, height=600)
user_bat = screen.textinput(title='Make Your Bat', prompt="Which turtle will win the race? Enter Color")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_position = [-200, -120, -40, 40, 120, 200]
all_turtles = []

for turtle_index in range(0, 6):
    tim = Turtle(shape='turtle')
    tim.turtlesize(3)
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-310, y=y_position[turtle_index])
    all_turtles.append(tim)

if user_bat:
    is_race_on = True
while is_race_on:
    for turtl in all_turtles:
        if turtl.xcor() > 300:
            is_race_on = False
            winning_color = turtl.pencolor()
            if winning_color == user_bat:
                print(f"You've Win! the {winning_color} turtle is winner!")
            else:
                print(f"You've lost! the {winning_color} turtle is winner!")

        ran_distance = random.randint(0,10)
        turtl.fd(ran_distance)

screen.exitonclick()