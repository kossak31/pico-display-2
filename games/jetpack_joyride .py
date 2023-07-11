import utime
import random
from pimoroni import RGBLED, Button
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_RGB565

# Initialize Pico Display
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, pen_type=PEN_RGB565)

WIDTH, HEIGHT = display.get_bounds()

# Initialize buttons
button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)

# Game constants
SCREEN_WIDTH = WIDTH
SCREEN_HEIGHT = HEIGHT
CHARACTER_WIDTH = 8
CHARACTER_HEIGHT = 8
OBSTACLE_WIDTH = 10
OBSTACLE_HEIGHT = 40
OBSTACLE_SPEED = 1
JUMP_HEIGHT = 10

# Player character
character_x = 20
character_y = SCREEN_HEIGHT // 2

# Obstacles
obstacles = []
obstacle_gap = 200
obstacle_timer = utime.ticks_ms()

# Scoring
score = 0
high_score = 0

WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
GREEN = display.create_pen(0, 255, 0)
RED = display.create_pen(255, 0, 0)


def generate_obstacle():
    obstacle_x = SCREEN_WIDTH
    obstacle_y = random.randint(0, SCREEN_HEIGHT - obstacle_gap+200)
    obstacles.append((obstacle_x, obstacle_y))


def draw_character():
    display.set_pen(WHITE)
    display.rectangle(character_x, character_y,
                      CHARACTER_WIDTH, CHARACTER_HEIGHT)


def draw_obstacles():
    display.set_pen(RED)
    for obstacle in obstacles:
        x, y = obstacle
        display.rectangle(x, y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)


def check_collision():
    for obstacle in obstacles:
        x, y = obstacle
        if (
            character_x < x + OBSTACLE_WIDTH and
            character_x + CHARACTER_WIDTH > x and
            character_y < y + OBSTACLE_HEIGHT and
            character_y + CHARACTER_HEIGHT > y
        ):
            return True
    return False


def update_score():
    global score, high_score
    score += 1
    if score > high_score:
        high_score = score


def display_score():
    display.set_pen(GREEN)
    display.text("Score:", 5, 5, 200, 4)
    display.text(str(score) + "/" + str(high_score), 5, 40, 200, 4)


def reset_game():
    global score, character_y, obstacles
    score = 0
    character_y = SCREEN_HEIGHT // 2
    obstacles = []


# Game instructions and gameplay description
display.set_pen(WHITE)
display.text("How to Play:", 5, 10, 200, 4)
display.text("Use A or B/ X or Y button to move", 5, 70, 200, 2)
display.text("the character up or down", 5, 100, 200, 2)
display.text("Avoid the red blocks", 5, 130, 200, 2)
display.text("Score increases based on", 5, 160, 200, 2)
display.text("the distance covered", 5, 190, 200, 2)
display.update()
utime.sleep(10)


while True:
    display.set_pen(BLACK)
    display.clear()

    # Check for user input
    if button_a.read() and character_y > 0:
        character_y -= JUMP_HEIGHT
    elif button_b.read() and character_y + CHARACTER_HEIGHT < SCREEN_HEIGHT:
        character_y += JUMP_HEIGHT
    elif button_x.read() and character_y > 0:
        character_y -= JUMP_HEIGHT
    elif button_y.read() and character_y + CHARACTER_HEIGHT < SCREEN_HEIGHT:
        character_y += JUMP_HEIGHT

    # Update character position
    character_y += 1

    # Ensure character stays within screen boundaries
    if character_y < 0:
        character_y = 0
    elif character_y + CHARACTER_HEIGHT > SCREEN_HEIGHT:
        character_y = SCREEN_HEIGHT - CHARACTER_HEIGHT

    # Generate new obstacles
    if utime.ticks_diff(utime.ticks_ms(), obstacle_timer) > 1000:
        generate_obstacle()
        obstacle_timer = utime.ticks_ms()

    # Update obstacle positions
    for i, obstacle in enumerate(obstacles):
        x, y = obstacle
        x -= OBSTACLE_SPEED
        obstacles[i] = (x, y)

        # Remove obstacles that have gone off the screen
        if x + OBSTACLE_WIDTH < 0:
            obstacles.pop(i)

    # Check for collision
    if check_collision():
        reset_game()

    # Update score
    update_score()

    # Draw game elements
    draw_character()
    draw_obstacles()
    display_score()

    display.update()
    utime.sleep(0.02)
