import tkinter

#  GRAPHICS CONSTANTS
# --------------------
WIDTH = 600
HEIGHT = 600
SQUARE_SIZE = 20

#   COLORS
# ------------
SNAKE_COLOR = "#07f036"
FOOD_COLOR = "#db2a16"

#  GAME CONSTANTS
# -----------------
MOVE_INCREMENT = 20
MOVES_PER_SECOND = 10
GAME_SPEED = 1000 // MOVES_PER_SECOND

# GLOBAL VARIABLES
direction = "Right"

def create_canvas(width, height):
    top = tkinter.Tk()
    top.title("Snake Game")
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
    for positions in snake_positions:
        snake_part = canvas.create_rectangle(
            positions[0],
            positions[1],
            positions[0] + SQUARE_SIZE,
            positions[1] + SQUARE_SIZE,
            fill=SNAKE_COLOR,
        )
        snake.append(snake_part)
    return snake


def create_food(canvas, food_position):
    canvas.create_rectangle(
        food_position[0],
        food_position[1],
        food_position[0] + SQUARE_SIZE,
        food_position[1] + SQUARE_SIZE,
        fill=FOOD_COLOR
    )


def update_frame(canvas, snake_positions, snake):
    if check_collisions(snake_positions):
        return
    new_snake_positions = move_snake(canvas, snake_positions, snake)
    canvas.after(GAME_SPEED, update_frame, canvas, new_snake_positions, snake)


def move_snake(canvas, snake_positions, snake):
    head_position_x = snake_positions[0][0]
    head_position_y = snake_positions[0][1]

    global direction
    if direction == "Left":
        new_head_position_x = head_position_x - MOVE_INCREMENT
        new_head_position_y = head_position_y
    elif direction == "Right":
        new_head_position_x = head_position_x + MOVE_INCREMENT
        new_head_position_y = head_position_y
    elif direction == "Up":
        new_head_position_x = head_position_x
        new_head_position_y = head_position_y - MOVE_INCREMENT
    elif direction == "Down":
        new_head_position_x = head_position_x
        new_head_position_y = head_position_y + MOVE_INCREMENT


    snake_positions = [[new_head_position_x, new_head_position_y]] + snake_positions[:-1]

    for i in range(len(snake)):
        canvas.coords(
            snake[i],
            snake_positions[i][0],
            snake_positions[i][1],
            snake_positions[i][0] + SQUARE_SIZE,
            snake_positions[i][1] + SQUARE_SIZE
        )
    
    return snake_positions


def check_collisions(snake_positions):
    head_position_x = snake_positions[0][0]
    head_position_y = snake_positions[0][1]

    return (
        head_position_x < 0 or head_position_x >= WIDTH
        or head_position_y < 0 or head_position_y >= HEIGHT
        or snake_positions[0] in snake_positions[1:]
    )


def on_key_press(key_information):
    global direction
    new_direction = key_information.keysym
    possible_directions = ["Left", "Right", "Up", "Down"]
    opposites = [["Left", "Right"], ["Right", "Left"], ["Up", "Down"], ["Down", "Up"]]
    
    if new_direction in possible_directions
    and [new_direction, direction] not in opposites:
        direction = new_direction


def main():
    canvas = create_canvas(WIDTH, HEIGHT)
    # Each list inside this list stores the x and y coordinate of a body part
    snake_positions = [[100, 100], [80, 100], [60, 100]]
    food_position = [300, 400]
    global direction
    direction = "Right"

    canvas.bind_all("<Key>", on_key_press)
    # Initialize the game
    snake = create_snake(canvas, snake_positions)
    create_food(canvas, food_position)

    update_frame(canvas, snake_positions, snake)
    canvas.mainloop()


if __name__ == "__main__":
    main()