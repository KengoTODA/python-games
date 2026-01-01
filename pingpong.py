import pgzrun
import random

WIDTH  = 360
HEIGHT = 280

class Game():
    def __init__(self):
        self.ball = Ball()
        self.left_pad = Paddle()
        self.beep = tone.create('A3', 0.5)

    def draw(self):
        screen.clear()
        screen.fill((192,192,192))
        self.ball.draw()
        self.left_pad.draw()

    def update(self):
        self.ball.update()
        self.left_pad.update()

        if (self.ball.x <= 10):
            if (self.left_pad.y-30 <= self.ball.y <= self.left_pad.y+30):
                self.ball.speed_x = -self.ball.speed_x
        if (self.ball.y <= 0):
            self.ball.speed_y = -self.ball.speed_y
        if (self.ball.x > WIDTH-10):
            self.ball.speed_x = -self.ball.speed_x
        if (self.ball.y > HEIGHT):
            self.ball.speed_y = -self.ball.speed_y

        if self.ball.x < 0:
            self.beep.play()
            self.ball = Ball()

class Paddle():
    def __init__(self):
        self.x = 10
        self.y = HEIGHT / 2
        self.speed_y = 0

    def update(self):
        self.y += self.speed_y
        if (self.y < 30):
            self.y = 30
        if (self.y > HEIGHT-30):
            self.y = HEIGHT-30

    def draw(self):
        screen.draw.rect(Rect(self.x-1, self.y-30, 3, 60), (0, 0, 0))

class Ball():
    def __init__(self):
        self.x = random.randint(100, WIDTH-10)
        self.y = random.randint(HEIGHT/5, HEIGHT*4/5)

        self.speed_x = random.choice([-2, 2])
        self.speed_y = random.choice([-2, -1, 1, 2])

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self):
        screen.draw.circle((self.x, self.y), 3, (0, 0, 0))

game = Game()

def draw():
    game.draw()

def update():
    game.update()

def on_key_down(key):
    if key == keys.UP:
        game.left_pad.speed_y = -5
    if key == keys.DOWN:
        game.left_pad.speed_y = 5

def on_key_up(key):
    if key == keys.UP or key == keys.DOWN:
        game.left_pad.speed_y = 0

pgzrun.go()
