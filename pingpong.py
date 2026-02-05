import random
import turtle

WIDTH = 360
HEIGHT = 280
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2


class Game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Ping Pong")
        self.screen.setup(WIDTH, HEIGHT)
        self.screen.screensize(WIDTH, HEIGHT)
        self.screen.bgcolor("lightgray")
        self.screen.tracer(0)
        self.screen.listen()
        self.screen.getcanvas().winfo_toplevel().resizable(False, False)
        self.remove_scrollbars()

        self.ball = Ball()
        self.left_pad = Paddle()
        self.bind_keys()

    def bind_keys(self):
        self.screen.onkeypress(self.on_up_press, "Up")
        self.screen.onkeyrelease(self.on_up_release, "Up")
        self.screen.onkeypress(self.on_down_press, "Down")
        self.screen.onkeyrelease(self.on_down_release, "Down")

    def remove_scrollbars(self):
        canvas = self.screen.getcanvas()
        if not hasattr(canvas, "hscroll"):
            return

        def hide_scrollbars():
            canvas.hscroll.grid_forget()
            canvas.vscroll.grid_forget()

        hide_scrollbars()
        canvas.adjustScrolls = hide_scrollbars

    def update(self):
        self.ball.update()
        self.left_pad.update()

        if self.ball.x <= self.left_pad.x + 5:
            if self.left_pad.y - 30 <= self.ball.y <= self.left_pad.y + 30:
                self.ball.speed_x = -self.ball.speed_x
        if self.ball.y <= -HALF_HEIGHT + 3:
            self.ball.speed_y = -self.ball.speed_y
        if self.ball.x >= HALF_WIDTH - 3:
            self.ball.speed_x = -self.ball.speed_x
        if self.ball.y >= HALF_HEIGHT - 3:
            self.ball.speed_y = -self.ball.speed_y

        if self.ball.x < -HALF_WIDTH:
            self.ball = Ball()

    def on_up_press(self):
        self.left_pad.speed_y = 5

    def on_up_release(self):
        if self.left_pad.speed_y > 0:
            self.left_pad.speed_y = 0

    def on_down_press(self):
        self.left_pad.speed_y = -5

    def on_down_release(self):
        if self.left_pad.speed_y < 0:
            self.left_pad.speed_y = 0

    def run(self):
        self.update()
        self.screen.update()
        self.screen.ontimer(self.run, 16)


class Paddle:
    def __init__(self):
        self.x = -HALF_WIDTH + 12
        self.y = 0
        self.speed_y = 0
        self.shape = turtle.Turtle()
        self.shape.hideturtle()
        self.shape.penup()
        self.shape.shape("square")
        self.shape.color("black")
        self.shape.shapesize(stretch_wid=3, stretch_len=0.2)
        self.shape.goto(self.x, self.y)
        self.shape.showturtle()

    def update(self):
        self.y += self.speed_y
        # Keep the paddle on the screen.
        if self.y < -HALF_HEIGHT + 30:
            self.y = -HALF_HEIGHT + 30
        if self.y > HALF_HEIGHT - 30:
            self.y = HALF_HEIGHT - 30
        self.shape.goto(self.x, self.y)


class Ball:
    def __init__(self):
        self.x = random.randint(-40, HALF_WIDTH - 10)
        self.y = random.randint((-HEIGHT * 2) // 5, (HEIGHT * 2) // 5)

        self.speed_x = random.choice([-2, 2])
        self.speed_y = random.choice([-2, -1, 1, 2])
        self.shape = turtle.Turtle()
        self.shape.hideturtle()
        self.shape.penup()
        self.shape.shape("circle")
        self.shape.color("black")
        self.shape.shapesize(stretch_wid=0.3, stretch_len=0.3)
        self.shape.goto(self.x, self.y)
        self.shape.showturtle()

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.shape.goto(self.x, self.y)

def main():
    game = Game()
    game.run()
    turtle.mainloop()


if __name__ == "__main__":
    main()
