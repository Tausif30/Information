import turtle

def setup_turtle(color="black"):
    t = turtle.Turtle()
    t.speed(0)
    t.color(color)
    t.pensize(1)
    return t

def koch_curve(t, level, size):
    t.pendown()
    if level == 0:
        t.forward(size)
    else:
        segment = size / 3
        # Treat each segment as a smaller curve
        t.pendown()
        koch_curve(t, level-1, segment)
        t.left(60)
        koch_curve(t, level-1, segment)
        t.right(120)
        koch_curve(t, level-1, segment)
        t.left(60)
        koch_curve(t, level-1, segment)

def koch_snowflake(t, level, size):
    #Center the snowflake
    t.penup()
    t.backward(size/2)
    t.left(90)
    t.forward(size/3)
    t.right(90)
    t.pendown()
    #3 Curves for snowflakes
    for i in range(3):
        koch_curve(t, level, size)
        t.right(120)

def main():
    screen = turtle.Screen()
    screen.title("Koch Flake")
    t = setup_turtle()
    s = 500
    #t.penup()
    #t.backward(s/2)
    #koch_curve(t, 3, s)
    koch_snowflake(t, 0, s)
    screen.exitonclick()

if __name__ == "__main__":
    main()