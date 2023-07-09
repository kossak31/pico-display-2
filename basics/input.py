from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_RGB565

# Initialize PicoGraphics and set up the display
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, pen_type=PEN_RGB565, rotate=0)
# Set the display backlight to a brightness level of 0.8
display.set_backlight(0.8)



# Get the width and height of the display
WIDTH, HEIGHT = display.get_bounds()

# Change the font:
display.set_font("bitmap8")

# Create a pen for black color
BLACK = display.create_pen(0, 0, 0)


# Create a pen for white color
WHITE = display.create_pen(255, 255, 255)

# Set the pen color to white
display.set_pen(WHITE)

# Clear the display with the white color
display.clear()

# Set the pen color to black
display.set_pen(BLACK)

# Prompt the user to enter their name and display a greeting
name = input("Please enter your name: ")
display.text("Hello, " + name + "!", 10, 10, 240, 2)

# To display the entered name immediately after the user inputs it, you can remove the display.update() line.
display.update()

# Prompt the user to enter their age
age = input("Please enter your age: ")
age = int(age)  # Convert the input to an integer

# Check if the age is greater than or equal to 18 and display the appropriate message
if age >= 18:
    display.text("You are an adult.", 10, 30, 240, 2)
else:
    display.text("You are a minor.", 10, 70, 240, 2)


# Update the display to show the changes
display.update()
