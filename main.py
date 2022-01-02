import time
from turtle import Screen
from ui import Paddle, Bricks, Writer, Ball
# from ball import Ball


screen = Screen()
screen.title('Breakout')
screen.bgcolor('#30475E')
screen.tracer(0)

screen.setup(width=400, height=500)

paddle = Paddle()

# Screen events for moving paddle
screen.listen()
screen.onkey(paddle.move_left, 'Left')
screen.onkey(paddle.move_right, 'Right')

# Creating ball
ball = Ball()
breaker = Bricks(5, 9, -160, 20)
print(len(breaker.collection))

# Score board
score = 0
score_writer = Writer(40, 210)
score_writer.write_score(score=f"Score: {score}")


# Life counting
total_life = 5
life_line = Writer(-80, 210)
life_line.write_score(f'{"🤍" * total_life}')

game_end = False

first_round = True

while not game_end:
    time.sleep(0.1)

    # Tracking collision with bricks
    for single_brick in breaker.collection:

        if ball.distance(single_brick) < 25:
            single_brick.goto(0, 600)
            score += 10
            score_writer.write_score(f'Score: {score}')
            # changing y direction of ball
            ball.change_y()

    # Tracking ball collision with boundaries.

    if ball.xcor() > 170 or ball.xcor() < -170:
        ball.change_x()
    elif ball.ycor() > 230:
        ball.change_y()

    if score == len(breaker.collection)*10:
        # Clearing elements form the screen
        for brick in breaker.collection:
            brick.goto(300, 500)
        ball.goto(600, 500)
        paddle.goto(300, 500)

        # writing comments
        life_line.goto(0, 0)
        life_line.write_score('Yey you won the game')

        score_writer.goto(0, -20)
        score_writer.write_score(f"Your Score: {score}")


    # Tracking collision with lower boundary
    if ball.ycor() < -210 and total_life != 1:
        paddle.goto(0, -210)
        ball.goto(0, -189)

        # decreasing life
        total_life -= 1
        life_line.write_score(f'{"🤍" * total_life}')

        time.sleep(1)
    elif ball.ycor() < -210 and total_life == 1:
        # Ending game if player has no more life
        game_end = True

        ball.goto(300, 500)
        paddle.goto(300, 500)

        for brick in breaker.collection:
            brick.goto(300, 500)

        life_line.goto(0, 0)
        life_line.write_score('GAME OVER')

        score_writer.goto(0, -20)
        score_writer.write_score(f"Your Score: {score}\nYor loose")

    # Tracking collision with paddle
    if ball.distance(paddle) <= 35 and not first_round:
        ball.change_y()

    first_round = False

    ball.move_ball()
    screen.update()


screen.exitonclick()
