# Import required libraries
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_RGB565

# Initialize Pico Display
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, pen_type=PEN_RGB565)

# Initialize buttons
button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)

# player variables
player_x = 5
player_y = 150
player_height = 16


# Define pen colors
WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
GREEN = display.create_pen(0, 255, 0)
RED = display.create_pen(255, 0, 0)

# Define the Dot class


class Dot:
    def __init__(self, x, y, size, disabled=False):
        self.x = x
        self.y = y
        self.size = size
        self.disabled = disabled


# Create dot objects
dot1 = Dot(10, 10, 16)
dot2 = Dot(10, 30, 16)
dot3 = Dot(10, 60, 16)
dot4 = Dot(30, 90, 16)
dot5 = Dot(30, 120, 16)
dot6 = Dot(30, 140, 16)
dot7 = Dot(60, 90, 16)
dot8 = Dot(60, 120, 16)
dot9 = Dot(60, 140, 16)

dots = [dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8, dot9]

# Main game loop
while True:
    display.set_pen(BLACK)
    display.clear()

    # Draw green rectangle (PLAYER)
    display.set_pen(GREEN)
    display.rectangle(player_x, player_y, player_height, player_height)

    # Draw dots
    for dot in dots:
        if not dot.disabled:
            display.set_pen(RED)
            display.rectangle(dot.x, dot.y, dot.size, dot.size)
        else:
            display.set_pen(BLACK)
            display.rectangle(dot.x, dot.y, dot.size, dot.size)

    # Collision detection and dot disabling
    for dot in dots:
        if (player_x + player_height > dot.x and player_x < dot.x + dot.size and player_y + player_height > dot.y and player_y < dot.y + dot.size):
            dot.disabled = True
            display.set_pen(GREEN)
            display.rectangle(player_x, player_y, player_height, player_height)

    # Button controls for playersaur movement
    if button_a.read():
        player_y -= 2
    elif button_b.read():
        player_y += 2
    elif button_x.read():
        player_x -= 2
    elif button_y.read():
        player_x += 2

    # Update the display
    display.update()
