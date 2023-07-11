from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_RGB565
from pimoroni import RGBLED

# Initialize PicoGraphics and set up the display
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, pen_type=PEN_RGB565, rotate=0)
# Set the display backlight to a brightness level of 0.8
display.set_backlight(0.8)

# Initialize RGBLED
led = RGBLED(6, 7, 8)

# Get the width and height of the display
WIDTH, HEIGHT = display.get_bounds()

# Change the font:
display.set_font("bitmap8")

# Create a pen for black color
BLACK = display.create_pen(0, 0, 0)

# Turn off the LED by setting its RGB values to 0 ,0 ,0
# Turn on the LED with white light
led.set_rgb(255, 255, 255)

# Create a pen for white color
WHITE = display.create_pen(255, 255, 255)

# Set the pen color to white
display.set_pen(WHITE)

# Clear the display with the white color
display.clear()

# Set the pen color to black
display.set_pen(BLACK)

# Display ASCII text at position (10, 10) with font size 240 and line height 2
display.text("\"!#$%&'()*+,-./:;<=>?[\]{|}~^_`\n0123456789\n@ABCDEFGHIJKLMNOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz", 10, 10, 240, 2)

# Update the display to show the changes
display.update()
