import turtle
import random
import math


def create_window():
    # Turtle Window Setup
    window = turtle.Screen()
    window.setup(800, 600)
    window.title("Generalized Circumscribed Circle")
    window.bgcolor("white")
    return window


def polygon(n, t, side_length):
    # To collect the coordinates
    coordinates = []
    # Polygon Drawing Function
    if n >= 3:
        angle = 360 / n
        for i in range(n):
            coordinates.append(t.pos())
            t.forward(side_length)
            t.left(angle)
        return coordinates


def centroid(coordinates):
    # Finding Centroid
    x = sum(coord[0] for coord in coordinates) / len(coordinates)
    y = sum(coord[1] for coord in coordinates) / len(coordinates)
    return x, y


def radius_from_centroid(coordinates):
    # Calculate radius as distance between centroid and first vertex
    cen_x, cen_y = centroid(coordinates)
    x, y = coordinates[0]
    return math.dist((x, y), (cen_x, cen_y))


def main():
    window = create_window()
    t = turtle.Turtle()
    t.speed(0)
    for i in range(3,13):
        n = i #Change this to get different polygons
        t.penup()
        t.goto(random.randint(-300, 300), random.randint(-250, 250))
        t.pendown()
        random_angle = random.randint(0, 360)
        t.setheading(random_angle)
        side_length = random.randint(30, 150)
        t.color("blue")
        coordinates = polygon(n, t, side_length)
        x, y = coordinates[0]
        t.penup()
        radius = radius_from_centroid(coordinates)
        # Go to first vertex
        t.goto(x, y)
        # Calculate interior angle for rotation
        interior_angle = (n - 2) * 180 / n
        exterior_angle = 360/n
        rotation = exterior_angle - 90 + interior_angle/2
        t.setheading(random_angle - rotation)
        t.pendown()
        t.color("red")
        t.circle(radius)
        t.penup()
    window.mainloop()


if __name__ == "__main__":
    main()