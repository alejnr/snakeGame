from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")

starting_position = [(0,0), (-20,0), (-40,0)]

for pos in starting_position:
    new_segment = Turtle(shape='square')
    new_segment.color('white')
    new_segment.goto(pos)

# turtle1 = Turtle("square")
# turtle1.color("white")
#
# turtle2 = Turtle("square")
# turtle2.color("white")
# turtle2.goto(-20, 0)
#
# turtle3 = Turtle("square")
# turtle3.color("white")
# turtle3.goto(-40, 0)



screen.exitonclick()