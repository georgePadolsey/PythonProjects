from random import randint
from Entity import Entity

__author__ = 'George'

class Ball(Entity):
    def __init__(self, app):
        super().__init__(app.canvas)
        self.app = app
        self.speed = 6
        self.width = 50
        self.height = 50
        self.color = "#FF00FF"
        self.lastNotePos = {
            'x': self.x,
            'y': self.y
        }
        self.notePos = 20

        self.reset()

    def render(self):
        ctx = self.ctx

        self.check_hitbox()

        self.add_delta()
        ctx.create_oval(self.x, self.y, self.x + self.width, self.height + self.y, fill=self.color)

        if self.notePos <= 0:
            self.notePos = 20
            self.lastNotePos['x'] = self.x
            self.lastNotePos['y'] = self.y


        self.notePos -= 1

    def check_hitbox(self):

        windowWidth = self.app.w
        windowHeight = self.app.h
        x = self.x
        y = self.y
        height = self.height
        width = self.width
        playerPaddle = self.app.playerPaddle
        cpuPaddle = self.app.cpuPaddle

        if y <= 0 or y + height > windowHeight:
            self.bounce_y()

        if x <= 0:
            self.app.cpuWin()

            self.reset()

        if x + width >= windowWidth:
            self.app.playerWin()

            self.reset()

        if x + width >= cpuPaddle.x and cpuPaddle.y < y <= cpuPaddle.y + cpuPaddle.height:
            self.bounce_x(abs(y - (cpuPaddle.y + (cpuPaddle.height/2)))) # bounce with the offset the ball is from the middle of the paddle

        if x <= playerPaddle.x + playerPaddle.width and playerPaddle.y < y <= playerPaddle.y + playerPaddle.height:
            self.bounce_x(abs(y - (playerPaddle.y + (playerPaddle.height/2)))) # bounce with the offset the ball is from the middle of the paddle


    def reset(self):
        self.x = (self.app.w - self.width) / 2
        self.y = (self.app.h - self.height) / 2
        self.delta_x = randint(-1, 1) * self.speed
        self.delta_y = randint(-1, 1) * self.speed

        if self.delta_x * self.delta_y == 0:
            self.delta_x = self.speed
            self.delta_y = -self.speed

    def bounce_y(self):
        self.delta_y = -self.delta_y

    def bounce_x(self, offset):
        if self.delta_x < 0:
            self.delta_x = -self.delta_x + offset/10 + (randint(-self.speed, self.speed))/2
        else:
            self.delta_x = -self.delta_x - offset/10 - (randint(-self.speed, self.speed))/2
