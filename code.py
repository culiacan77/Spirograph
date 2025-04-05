import time
from math import cos, radians, sin

import board
import picomo
import terminalio
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label
from adafruit_turtle import Color, turtle

VALUE_INCREMENT = const(5)
MIN_VALUE = const(5)


class Value:

    def __init__(self, name, value, color, min_value, max_value, step):
        self.name = name
        self.value = value
        self.color = color
        self.min_value = min_value
        self.max_value = max_value
        self.step = step

    def increment(self):
        self.value = min(self.value + self.step, self.max_value)

    def decrement(self):
        self.value = max(self.value - self.step, self.min_value)


grand_rayon = Value("GRAND_RAYON", 100, Color.RED, 5, 200, 5)
petit_rayon = Value("PETIT_RAYON", 17, Color.GREEN, 5, 200, 5)
rayon_stylo = Value("RAYON_STYLO", 50, Color.PINK, 5, 200, 5)
speed = Value("SPEED", 1, Color.ORANGE, 1, 5, 1)

variables = [
    grand_rayon,
    petit_rayon,
    rayon_stylo,
    speed,
]

# Variables to modify with buttons
selected_var = 0  # Start with first variable selected


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
        self.turtle.goto(0, -grand_rayon.value)
        self.turtle.pendown()
        self.turtle.circle(grand_rayon.value)
        self.turtle.penup()

    def goto(self, angle):
        """Moves to the correct spirograph position"""
        x0 = (grand_rayon.value - petit_rayon.value) * sin(angle)
        y0 = (grand_rayon.value - petit_rayon.value) * cos(angle)
        beta = angle * grand_rayon.value / petit_rayon.value  # Rotation of small circle
        x = x0 - rayon_stylo.value * sin(angle - beta)
        y = y0 - rayon_stylo.value * cos(angle - beta)
        self.turtle.goto(x, y)


# Initialize Spirograph
s = Spinograph(turtle_display)
s.goto(0)
turtle_display.pendown()

# Button Handling Loop
i = 0

font1 = bitmap_font.load_font("fonts/luRS12.bdf")
font2 = terminalio.FONT
# text_area = label.Label(terminalio.FONT, text=text)
variable_name_area = label.Label(font2)
variable_name_area.x = 20
variable_name_area.y = 50
variable_name_area.scale = 2

variable_value_area = label.Label(font2)
variable_value_area.x = 20
variable_value_area.y = 75
variable_value_area.scale = 2

board.DISPLAY.root_group.append(variable_name_area)
board.DISPLAY.root_group.append(variable_value_area)

variable_name_area.text = f"{variables[selected_var].name}"
variable_value_area.text = f"{variables[selected_var].value}"

while True:
    i += 1

    # Set the turtle color based on the selected variable
    selected_color = variables[selected_var].color

    # Change the pen color of the turtle
    turtle_display.pencolor(selected_color)

    # Draw the spirograph with updated pen color
    s.goto(radians(i))

    # Check button presses
    picomo.update()

    # Increase or decrease the selected variable
    if picomo.buttons["sw_up"].fell:  # Increase selected variable
        v = variables[selected_var]
        v.increment()
        variable_value_area.text = f"{v.value}"

    if picomo.buttons["sw_down"].fell:  # Decrease selected variable
        v = variables[selected_var]
        v.decrement()
        variable_value_area.text = f"{v.value}"

    # Switch between variables on left or right button press
    if picomo.buttons["sw_left"].fell:  # Switch variable left
        selected_var = (selected_var - 1) % len(variables)
        v = variables[selected_var]
        variable_name_area.text = f"{v.name}"
        variable_value_area.text = f"{v.value}"

    if picomo.buttons["sw_right"].fell:  # Switch variable right
        selected_var = (selected_var + 1) % len(variables)
        v = variables[selected_var]
        variable_name_area.text = f"{v.name}"
        variable_value_area.text = f"{v.value}"

    if picomo.buttons["sw_mid"].fell:  # clear screen
        turtle_display.penup()
        turtle_display.clear()
        turtle_display.pendown()

    time.sleep(speed.value / 100)  # Small delay to avoid multiple detections
