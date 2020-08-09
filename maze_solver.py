"""#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

import turtle
import time
import sys

wn = turtle.Screen()
wn.bgcolor("purple")
wn.setup(1300,700)


class Maze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class End(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

class sprite(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("turtle")
        self.color("black")
        self.setheading(270)
        self.penup()
        self.speed(0)


    def spriteDown(self):
        if (self.heading() == 270):
            x_walls = round(sprite.xcor(),0)
            y_walls = round(sprite.ycor(),0)
            if (x_walls, y_walls) in finish:
                print("Finished")
                endProgram()
            if (x_walls +24, y_walls) in walls:
                if(x_walls, y_walls -24) not in walls:
                    self.forward(24)
                else:
                    self.right(90)
            else:
                self.left(90)
                self.forward(24)


    def spriteleft(self):
        if (self.heading() == 0):
            x_walls = round(sprite.xcor(),0)
            y_walls = round(sprite.ycor(),0)
            if (x_walls, y_walls) in finish:
                print("Finished")
                endProgram()
            if (x_walls, y_walls +24) in walls:
                if(x_walls +24, y_walls) not in walls:
                    self.forward(24)
                else:
                    self.right(90)
            else:
                self.left(90)
                self.forward(24)


    def spriteUp(self):
        if (self.heading() == 90):
            x_walls = round(sprite.xcor(),0)
            y_walls = round(sprite.ycor(),0)
            if (x_walls, y_walls) in finish:
                print("Finished")
                endProgram()
            if (x_walls -24, y_walls ) in walls:
                if (x_walls, y_walls + 24) not in walls:
                    self.forward(24)
                else:
                    self.right(90)
            else:
                self.left(90)
                self.forward(24)

    def spriteRight(self):
        if (self.heading() == 180):

            x_walls = round(sprite.xcor(),0)
            y_walls = round(sprite.ycor(),0)
            if (x_walls, y_walls) in finish:
                print("Finished")
                endProgram()
            if (x_walls, y_walls -24) in walls:
                if (x_walls - 24, y_walls) not in walls:
                    self.forward(24)
                else:
                    self.right(90)
            else:
                self.left(90)
                self.forward(24)


def endProgram():
    wn.exitonclick()
    sys.exit()


grid = [
"++++++++++++++++++++++++++++++++++++++++++++++",
"+ s             +                            +",
"+  ++++++++++  +++++++++++++  +++++++  ++++  +",
"+           +                 +        +     +",
"+  +++++++  +++++++++++++  +++++++++++++++++++",
"+  +     +  +           +  +                 +",
"+  +  +  +  +  +  ++++  +  +  +++++++++++++  +",
"+  +  +  +  +  +  +     +  +  +  +        +  +",
"+  +  ++++  +  ++++++++++  +  +  ++++  +  +  +",
"+  +     +  +              +           +  +  +",
"+  ++++  +  ++++++++++++++++  +++++++++++++  +",
"+     +  +                    +              +",
"++++  +  ++++++++++++++++++++++  ++++++++++  +",
"+  +  +                    +     +     +  +  +",
"+  +  ++++  +++++++++++++  +  ++++  +  +  +  +",
"+  +  +     +     +     +  +  +     +     +  +",
"+  +  +  +++++++  ++++  +  +  +  ++++++++++  +",
"+                       +  +  +              +",
"++++  +  +  ++++++++++  +  +  +  +++++++++++++",
"+++++++++++++++++++++++e++++++++++++++++++++++",
]

def setupMaze(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            character = grid[y][x]
            screen_x = -588 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "+":
                maze.goto(screen_x, screen_y)
                maze.stamp()
                walls.append((screen_x, screen_y))

            if character == "e":
                end.goto(screen_x, screen_y)
                end.stamp()
                finish.append((screen_x, screen_y))

            if character == "s":
                sprite.goto(screen_x, screen_y)

maze = Maze()
sprite = sprite()
end = End()
walls =[]
finish = []

setupMaze(grid)

while True:
        sprite.spriteRight()
        sprite.spriteDown()
        sprite.spriteleft()
        sprite.spriteUp()

        time.sleep(0.02)
