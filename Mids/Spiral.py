import turtle
import colorsys
def create_window():
    # Turtle Window Setup
    window = turtle.Screen()
    window.setup(800, 600)
    window.title("Colorful Spiral")
    window.bgcolor("white")
    return window
def colorful_spiral(t, sides, max_length):
    angle = 20
    current_length = 5
    hue = 0
    while current_length < max_length:
        #Change Hue
        rgb_color = colorsys.hls_to_rgb(hue, 0.5, 0.8)
        t.color(rgb_color)
        t.forward(current_length)
        t.left(angle)
        current_length += 1
        hue += 0.01
        if hue > 1:
            hue -= 1
def main():
    window = create_window()
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    t.pendown()
    colorful_spiral(t, 50, 400)
    t.penup()
    window.mainloop()
if __name__ == "__main__":
    main()