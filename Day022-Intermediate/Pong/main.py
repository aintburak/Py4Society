from turtle import Turtle, Screen


def setScreen(screen: Screen):
    """Adjust the screen of the pong game"""
    screen.bgcolor('black')
    screen.setup(800, 600)
    screen.title("Pong")
    screen.tracer(0)


def refreshScreen(screen: Screen):
    """Refresh the screen of the pong game"""
    screen.update()


def moveUp(paddle) -> None:
    newY = paddle.ycor() + 20
    paddle.goto(paddle.xcor, newY)


def moveDown(paddle) -> None:
    newY = paddle.ycor() - 20
    paddle.goto(paddle.xcor, newY)


def main():
    """"main function"""

    isGameOn = True

    screen = Screen()
    setScreen(screen)

    paddle = Turtle()
    paddle.shape('square')
    paddle.color('white')
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(350, 0)
    screen.listen()
    screen.onkey(lambda: moveUp(paddle), "Up")
    screen.onkey(lambda: moveDown(paddle), "Down")

    while isGameOn:
        screen.update()

    screen.exitonclick()


if __name__ == "__main__":
    main()
