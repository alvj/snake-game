import tkinter

WIDTH = 800
HEIGHT = 800
SQUARE_SIZE = 20

def main():
    canvas = create_canvas(WIDTH, HEIGHT)
    snake_positions = [[100, 100], [80, 100], [60, 100]]
    create_snake(canvas, snake_positions)

    canvas.mainloop()

def create_snake(canvas, snake_positions):
    for positions in snake_positions:
        canvas.create_rectangle(
            positions[0],
            positions[1],
            positions[0] + SQUARE_SIZE,
            positions[1] + SQUARE_SIZE,
            fill="green"
        )

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


if __name__ == "__main__":
    main()