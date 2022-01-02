from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(0, -210)
        self.fillcolor('blue')

    def move_left(self):
        self.setheading(180)
        self.forward(20) if self.xcor() > -110 else self.forward(0)

    def move_right(self):
        self.setheading(0)
        self.forward(20) if self.xcor() < 120 else self.forward(0)


class Bricks:

    def __init__(self, row, column, initial_x, initial_y):
        self.collection = []
        self.row = row
        self.column = column
        self.initial_x = initial_x
        self.initial_y = initial_y
        self.brick_multiplier()

    def brick_builder(self, init_x, init_y):
        new_brick = Turtle(shape='square')
        new_brick.penup()
        new_brick.color('blue')
        new_brick.goto(init_x, init_y)
        self.collection.append(new_brick)

    def brick_multiplier(self):
        for _ in range(self.row):

            for _ in range(self.column):
                self.brick_builder(init_x=self.initial_x, init_y=self.initial_y)

                self.initial_x += 40

            self.initial_x -= 40 * self.column
            self.initial_y += 40


class Writer(Turtle):

    def __init__(self, write_x, write_y):
        super().__init__()
        self.write_x = write_x
        self.write_y = write_y
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(self.write_x, self.write_y)

    def write_score(self, score):
        self.clear()
        self.write(score, align='Center', font=('Arial', 14, 'bold'))


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0, -189)
        self.x_movement = 10
        self.y_movement = 10

    def move_ball(self):
        new_x = self.xcor() + self.x_movement
        new_y = self.ycor() + self.y_movement
        self.goto(new_x, new_y)

    def change_x(self):
        self.x_movement *= -1

    def change_y(self):
        self.y_movement *= -1
