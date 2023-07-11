import utime
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_RGB565

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, pen_type=PEN_RGB565)
display.set_backlight(0.8)

WIDTH, HEIGHT = display.get_bounds()

button_a = Button(12)
button_b = Button(13)

# Set initial time
hours = 0
minutes = 0
seconds = 0
text_width = 230  # Width of the text (adjust this value based on your text size)

x = (WIDTH - text_width) // 2  # Calculate the centered x-coordinate
y = (HEIGHT - 50) // 2  # Calculate the centered y-coordinate

# Main loop
while True:

    # Limit the range of hours and minutes
    hours = hours % 24  # Limit hours to 0-23 range
    minutes = minutes % 60  # Limit minutes to 0-59 range



    # Get the current time
    current_time = utime.localtime()
    current_hours = current_time[3] + hours
    current_minutes = current_time[4] + minutes
    current_seconds = current_time[5] + seconds

    # Handle time overflow
    if current_minutes > 59:
        current_minutes = 0
        current_hours += 1

        if current_hours > 23:
            current_hours = 0

    if current_seconds > 59:
        current_seconds = 0
        current_minutes += 1

        if current_minutes > 59:
            current_minutes = 0
            current_hours += 1

            if current_hours > 23:
                current_hours = 0

    # Format the time as HH:MM:SS
    formatted_time = "{:02d}:{:02d}:{:02d}".format(current_hours, current_minutes, current_seconds)
    
    BLACK = display.create_pen(0, 0, 0)
    WHITE = display.create_pen(255, 255, 255)
    display.set_pen(WHITE)  
    display.clear()         
    display.set_pen(BLACK)

    display.text(formatted_time, x, y, 240, 6)
    # Update the display
    display.update()

    # Delay for a second
    utime.sleep(1)

    if button_a.read():
        hours += 1
        if hours > 23:
            hours = 0

    elif button_b.read():
        minutes += 1
        if minutes > 59:
            minutes = 0
