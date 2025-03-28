import board
import digitalio
import picomo
import time
from math import cos, radians, sin
from adafruit_turtle import Color, turtle
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
import displayio

# Default Values
GRAND_RAYON = 100
PETIT_RAYON = 17
RAYON_STYLO = 50
SPEED = 1
ADJUSTED_SPEED = SPEED / 100
# Variables to modify with buttons
variables = ["GRAND_RAYON", "PETIT_RAYON", "RAYON_STYLO", "SPEED"]
values = [GRAND_RAYON, PETIT_RAYON, RAYON_STYLO, SPEED]
selected_var = 0  # Start with first variable selected

# Colors for each variable
colors = {
    "GRAND_RAYON": Color.RED,     # Red for Big Circle
    "PETIT_RAYON": Color.GREEN,   # Green for Small Circle
    "RAYON_STYLO": Color.PINK,    # Pink for Pen Radius
    "SPEED": Color.ORANGE         # Orange for Speed
}

# Setup Display
turtle_display = turtle(board.DISPLAY)  # Create turtle object for drawing

# Draw Spirograph Class
class Spinograph:
    def __init__(self, turtle):
        self.turtle = turtle
        self.draw_circle()

    def draw_circle(self):
        """Draws the large reference circle"""
        self.turtle.pencolor(Color.GRAY)
        self.turtle.penup()
        self.turtle.goto(0, -values[0])  # GRAND_RAYON
        self.turtle.pendown()
        self.turtle.circle(values[0])
        self.turtle.penup()

    def goto(self, angle):
        """Moves to the correct spirograph position"""
        x0 = (values[0] - values[1]) * sin(angle)  # GRAND_RAYON - PETIT_RAYON
        y0 = (values[0] - values[1]) * cos(angle)
        beta = angle * values[0] / values[1]  # Rotation of small circle
        x = x0 - values[2] * sin(angle - beta)  # RAYON_STYLO
        y = y0 - values[2] * cos(angle - beta)
        self.turtle.goto(x, y)

# Initialize Spirograph
s = Spinograph(turtle_display)
s.goto(0)
turtle_display.pendown()

# Button Handling Loop
i = 0
while True:
    i += 1

    # Set the turtle color based on the selected variable
    selected_color = colors[variables[selected_var]]

    # Change the pen color of the turtle
    turtle_display.pencolor(selected_color)

    # Draw the spirograph with updated pen color
    s.goto(radians(i))

    # Check button presses
    picomo.update()

    # Increase or decrease the selected variable
    if picomo.buttons["sw_up"].fell:  # Increase selected variable
        values[selected_var] += 5
        print(f"Increased {variables[selected_var]}: {values[selected_var]}")

    if picomo.buttons["sw_down"].fell:  # Decrease selected variable
        values[selected_var] = max(5, values[selected_var] - 5)  # Prevent negative values
        print(f"Decreased {variables[selected_var]}: {values[selected_var]}")

    # Switch between variables on left or right button press
    if picomo.buttons["sw_left"].fell:  # Switch variable left
        selected_var = (selected_var - 1) % len(variables)
        print(f"Selected Variable: {variables[selected_var]}")

    if picomo.buttons["sw_right"].fell:  # Switch variable right
        selected_var = (selected_var + 1) % len(variables)
        print(f"Selected Variable: {variables[selected_var]}")

    if picomo.buttons["sw_mid"].fell:  # Reset to defaults
        turtle_display.penup()
        turtle_display.clear()
        turtle_display.pendown()
        print("Clear drawing")

    time.sleep(ADJUSTED_SPEED)  # Small delay to avoid multiple detections
