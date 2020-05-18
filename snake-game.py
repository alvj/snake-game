import tkinter
from random import randint

#  GRAPHICS CONSTANTS
# --------------------
WIDTH = 800
HEIGHT = 800
SQUARE_SIZE = 40

#   COLORS
# ------------
SNAKE_COLOR = "#07f036"
FOOD_COLOR = "#db2a16"

#  GAME CONSTANTS
# -----------------
MOVES_PER_SECOND = 10
GAME_SPEED = 1000 // MOVES_PER_SECOND

# GLOBAL VARIABLES
direction = "Right"
has_moved_this_frame = False

def create_canvas(width, height):
    top = tkinter.Tk()
    top.title("Snake")
    top.resizable(False, False)

    canvas = tkinter.Canvas(
        top,
        width=width,
        height=height,
        background="#111",
        highlightthickness=0
    )
    canvas.pack()

    return canvas


def create_snake(canvas, snake_positions):
    snake = []
    for position in snake_positions:
        snake_part = canvas.create_rectangle(
            position[0],
            position[1],
            position[0] + SQUARE_SIZE,
            position[1] + SQUARE_SIZE,
            fill=SNAKE_COLOR,
        )
        snake.append(snake_part)
    return snake


def create_food(canvas, food_position):
    food = canvas.create_rectangle(
        food_position[0],
        food_position[1],
        food_position[0] + SQUARE_SIZE,
        food_position[1] + SQUARE_SIZE,
        fill=FOOD_COLOR
    )
    return food


def update_frame(canvas, snake_positions, snake, food_position, food, score):
    if check_collisions(snake_positions):
        return
    if check_food_collision(canvas, snake_positions, food_position):
        score += 1
        print(score)
        food_position = set_new_food_position(snake_positions)
        move_food(canvas, food_position, food)
        add_body_part(canvas, snake_positions, snake)
    new_snake_positions = move_snake(canvas, snake_positions, snake)
    canvas.after(GAME_SPEED, update_frame, canvas, new_snake_positions, snake, food_position, food, score)


def move_snake(canvas, snake_positions, snake):
    global has_moved_this_frame
    global direction

    head_position_x = snake_positions[0][0]
    head_position_y = snake_positions[0][1]

    if direction == "Left":
        new_head_position_x = head_position_x - SQUARE_SIZE
        new_head_position_y = head_position_y
    elif direction == "Right":
        new_head_position_x = head_position_x + SQUARE_SIZE
        new_head_position_y = head_position_y
    elif direction == "Up":
        new_head_position_x = head_position_x
        new_head_position_y = head_position_y - SQUARE_SIZE
    elif direction == "Down":
        new_head_position_x = head_position_x
        new_head_position_y = head_position_y + SQUARE_SIZE
    

    snake_positions = [[new_head_position_x, new_head_position_y]] + snake_positions[:-1]

    for i in range(len(snake)):
        canvas.coords(
            snake[i],
            snake_positions[i][0],
            snake_positions[i][1],
            snake_positions[i][0] + SQUARE_SIZE,
            snake_positions[i][1] + SQUARE_SIZE
        )

    has_moved_this_frame = False
    return snake_positions


def check_collisions(snake_positions):
    head_position_x = snake_positions[0][0]
    head_position_y = snake_positions[0][1]

    return (
        head_position_x < 0 or head_position_x >= WIDTH
        or head_position_y < 0 or head_position_y >= HEIGHT
        or snake_positions[0] in snake_positions[1:]
    )


def check_food_collision(canvas, snake_positions, food_position):
    if food_position == snake_positions[0]:
        return True
    return False


def on_key_press(key_information):
    global has_moved_this_frame
    global direction
    new_direction = key_information.keysym
    possible_directions = ["Left", "Right", "Up", "Down"]
    opposites = [["Left", "Right"], ["Right", "Left"], ["Up", "Down"], ["Down", "Up"]]

    if not has_moved_this_frame:
        if new_direction in possible_directions and [new_direction, direction] not in opposites:
            direction = new_direction
            has_moved_this_frame = True


def add_body_part(canvas, snake_positions, snake):
    snake_positions.append(snake_positions[-1])
    snake.append(canvas.create_rectangle(
        snake_positions[-1][0],
        snake_positions[-1][1],
        snake_positions[-1][0] + SQUARE_SIZE,
        snake_positions[-1][1] + SQUARE_SIZE,
        fill=SNAKE_COLOR
    ))


def set_new_food_position(snake_positions):
    while True:
        food_position = [
            # Generates a random number between 0 and the size of the window
            # Subtract SQUARE_SIZE from the width/height so it can't appear outside the window
            # Divide that by SQUARE_SIZE so we only get each column and the row
            # Multiply that by SQUARE_SIZE to get the actual coords and not the col and row
            randint(0, (WIDTH - SQUARE_SIZE) // SQUARE_SIZE) * SQUARE_SIZE,
            randint(0, (HEIGHT - SQUARE_SIZE) // SQUARE_SIZE) * SQUARE_SIZE
        ]
        if food_position not in snake_positions:
            return food_position

def move_food(canvas, food_position, food):
    canvas.coords(
        food,
        food_position[0],
        food_position[1],
        food_position[0] + SQUARE_SIZE,
        food_position[1] + SQUARE_SIZE
    )


def main():
    canvas = create_canvas(WIDTH, HEIGHT)
    # SET VARIABLES
    # Each list inside this list stores the x and y coordinate of a body part
    snake_positions = [[SQUARE_SIZE * 5, SQUARE_SIZE * 5], [SQUARE_SIZE * 4, SQUARE_SIZE * 5], [SQUARE_SIZE * 3, SQUARE_SIZE * 5]]
    food_position = set_new_food_position(snake_positions)
    score = 0
    global direction
    direction = "Right"

    # Initialize the game
    snake = create_snake(canvas, snake_positions)
    food = create_food(canvas, food_position)
    canvas.bind_all("<Key>", on_key_press)
    canvas.after(2000, update_frame, canvas, snake_positions, snake, food_position, food, score)
    canvas.mainloop()


if __name__ == "__main__":
    main()