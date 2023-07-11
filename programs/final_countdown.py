import utime
import random
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_RGB565

# Initialize Pico Display
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, pen_type=PEN_RGB565)

WIDTH, HEIGHT = display.get_bounds()

# Initialize buttons
button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)

WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)

# Countdown variables
countdown_minutes = 0
countdown_seconds = 58
countdown_running = False

# Display screen before countdown
display.set_pen(WHITE)
display.text("Countdown Timer", 5, 10, 200, 4)
display.text("Press Button A to increase seconds", 5, 120, 200, 2)
display.text("Press Button B to decrease seconds", 5, 150, 200, 2)
display.text("Press Button X or Y to start", 5, 180, 200, 2)
display.update()
utime.sleep(2)




while True:
    display.set_pen(BLACK)
    display.clear()

    # Check for user input
    if button_a.read():
        countdown_seconds += 1
    elif button_b.read():
        countdown_seconds -= 1
    elif button_x.read() or button_y.read():
        countdown_running = True

    if countdown_seconds > 59:
        countdown_seconds = 0
        countdown_minutes += 1
            


      # Display countdown time
    display.set_pen(WHITE)
    display.text(f"Countdown: {countdown_minutes:02d}:{countdown_seconds:02d}", 10, 50, 200, 6)
    # Countdown logic
    if countdown_running:
        display.set_pen(WHITE)
        display.text("Countdown running...", 10, 150, 200, 4)

        if countdown_minutes > 0 or countdown_seconds > 0:
            countdown_seconds -= 1
            if countdown_seconds < 0:
                countdown_minutes -= 1
                countdown_seconds = 59
        else:
            countdown_running = False
            display.set_pen(BLACK)
            display.clear()
            display.set_pen(WHITE)
            display.text("It's the final countdown!!", 10, 100, 200, 6)
            display.update()
            break

    display.update()
    utime.sleep(1)  # Adjust the delay as needed


