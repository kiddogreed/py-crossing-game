from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
FINISHED = (0, 280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.shape("turtle")
        self.left(90)
        self.goto_start()

    def up(self):
        current_y = self.ycor()
        current_y += MOVE_DISTANCE
        self.goto(self.xcor(), current_y)

    def down(self):
        current_y = self.ycor()
        current_y -= MOVE_DISTANCE
        self.goto(self.xcor(), current_y)


    def goto_start(self):
        self.goto(STARTING_POSITION)

    def finished(self):
            if self.ycor() > FINISH_LINE_Y:
                return True
            else:
                return False


