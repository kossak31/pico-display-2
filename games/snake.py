# Import required libraries
import time
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_RGB565
import random

# Initialize Pico Display
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, pen_type=PEN_RGB565)

WIDTH, HEIGHT = display.get_bounds()

# Initialize buttons
button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)

# player variables
player_x = 5  # Start at a positive value to move right
player_y = 150
player_height = 16
direction = (1, 0)
snake = [(13, 20), (14, 20), (15, 20)]
game_over = False

# Define pen colors
WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
GREEN = display.create_pen(0, 255, 0)
RED = display.create_pen(255, 0, 0)

food_size = 8  # Size of the food in pixels
food = (
    random.randint(0, (WIDTH - food_size) // food_size),
    random.randint(0, (HEIGHT - food_size) // food_size),
)
def update_direction():
    global direction
    
    if button_a.read() and direction != (0, 1):
        direction = (0, -1)
    elif button_b.read() and direction != (0, -1):
        direction = (0, 1)
    elif button_x.read() and direction != (-1, 0):
        direction = (1, 0)
    elif button_y.read() and direction != (1, 0):
        direction = (-1, 0)

# Function to check if snake collides with itself or the boundary
def check_collision():
    head = snake[0]

    # Check if the snake hits the boundary
    if (
        head[0] < 0 or head[0] >= WIDTH or
        head[1] < 0 or head[1] >= HEIGHT
    ):
        return True

    # Check if the snake collides with itself
    if head in snake[1:]:
        return True

    return False


# Main game loop
while not game_over:
    update_direction()


    # Update snake's head position
    head = (
        (snake[0][0] + direction[0]) % (WIDTH // 8),
        (snake[0][1] + direction[1]) % (HEIGHT // 8)
    )


    # Check if the snake eats the food
    if head == food:
        food = (
            random.randint(0, (WIDTH - food_size) // food_size),
            random.randint(0, (HEIGHT - food_size) // food_size),
        )
    else:
        # Remove the tail if the snake doesn't eat food
        snake.pop()
    # Check for collision
    if check_collision():
        game_over = True

    # Add the new head to the snake
    snake.insert(0, head)

    # Clear the display
    display.set_pen(BLACK)
    display.clear()

    # Draw the snake
    display.set_pen(WHITE)
    for segment in snake:
        display.rectangle(segment[0] * 8, segment[1] * 8, 8, 8)

    # Draw the food
    display.set_pen(RED)
    display.rectangle(food[0] * 8, food[1] * 8, 8, 8)

 # Draw arrows indicating movement near buttons
    display.set_pen(GREEN)
    # Arrow up for Button A (top-left)
    display.triangle(5, 0, 9, 5, 1, 5)

    # Arrow down for Button B (bottom-left)
    display.triangle(5, HEIGHT, 9, HEIGHT - 5, 1, HEIGHT - 5)

    # Arrow right for Button X (top-right)
    display.triangle(WIDTH - 5, 10, WIDTH - 10, 15, WIDTH - 10, 5)
    
    # Arrow left for Button Y (bottom-right)
    display.triangle(WIDTH - 10, HEIGHT - 15, WIDTH - 5, HEIGHT - 20, WIDTH - 5, HEIGHT - 5)
    




    # Update the display
    display.update()

    # Delay to control the speed of the game
    time.sleep(0.2)  # Adjust this value to change the game speed
