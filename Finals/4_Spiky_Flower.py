import turtle
import math
import numpy as np

screen = turtle.Screen()
screen_width = screen.window_width()
screen_height = screen.window_height()
screen.setworldcoordinates(-screen_width // 2, 0, screen_width // 2, screen_height)
screen.title("Spiky Flower")
screen.bgcolor("black")

def setup_turtle(color="white"):
    t = turtle.Turtle()
    t.speed(3)
    t.color(color)
    t.penup()
    return t

def polygon(n, s):
    t = setup_turtle()
    coordinates = []
    if n >= 3:
        angle = 360 / n
        for i in range(n):
            coordinates.append(t.pos())
            t.forward(s)
            t.left(angle)
        t.hideturtle()
        return coordinates

def centroid(coordinates):
    # Finding Centroid
    x = sum(coord[0] for coord in coordinates) / len(coordinates)
    y = sum(coord[1] for coord in coordinates) / len(coordinates)
    return x, y

def polygram(coordinates,order):
    t = setup_turtle(color="white")
    n = len(coordinates)
    step = math.gcd(n,order)
    for i in range(step):
        start_index = i
        current_index = start_index
        t.penup()
        t.goto(coordinates[start_index])
        t.pendown()
        next_index = (current_index + order)
        while start_index != next_index:
            next_index = (current_index + order) % n
            t.goto(coordinates[next_index])
            current_index = next_index
    t.hideturtle()

def main():
    t = setup_turtle()
    screen = turtle.Screen()
    screen.title("Polygram Drawing")
    order = 7
    n = 17
    coords = polygon(n, 100)
    t.pendown()
    polygram(coords,order)
    x, y = centroid(coords)
    r = 25
    t.penup()
    t.goto(x, y-r)
    t.pendown()
    t.color("red")
    t.circle(r)
    screen.exitonclick()

if __name__ == "__main__":
    main()
