import tkinter

WIDTH = 600
HEIGHT = 600
SQUARE_SIZE = 20
MOVE_INCREMENT = 20

#   COLORS
# ------------
SNAKE_COLOR = "#07f036"
FOOD_COLOR = "#db2a16"


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

def move_snake(canvas, snake_positions, snake):
    head_position_x = snake_positions[0][0]
    head_position_y = snake_positions[0][1]
    new_head_position_x = head_position_x + MOVE_INCREMENT
    new_head_position_y = head_position_y

    snake_positions = [[new_head_position_x, new_head_position_y]] + snake_positions[:-1]

    for i in range(len(snake)):
        canvas.coords(
            snake[i],
            snake_positions[i][0],
            snake_positions[i][1],
            snake_positions[i][0] + SQUARE_SIZE,
            snake_positions[i][1] + SQUARE_SIZE
        )
    canvas.after(100, move_snake, canvas, snake_positions, snake)


def main():
    canvas = create_canvas(WIDTH, HEIGHT)
    # Each list inside this list stores the initial x and y values for the snake body parts
    snake_positions = [[100, 100], [80, 100], [60, 100]]
    food_position = [300, 400]
    snake = create_snake(canvas, snake_positions)
    create_food(canvas, food_position)

    move_snake(canvas, snake_positions, snake)
    canvas.mainloop()

if __name__ == "__main__":
    main()