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



# Main game loop
while True:
    display.set_pen(BLACK)
    display.clear()

    # Draw green rectangle (PLAYER)
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
