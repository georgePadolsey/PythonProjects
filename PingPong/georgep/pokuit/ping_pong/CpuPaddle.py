from Paddle import Paddle

__author__ = 'George'

class CpuPaddle(Paddle):
    def __init__(self, app):
        super().__init__(app.canvas)
        self.app = app
        self.width = 50
        self.height = 200
        self.x = self.app.w - 5 - self.width
        self.y = (self.app.h - self.height) / 2
        self.default = {
            'y': app.h/150
        }
        self.color = "red"
        self.init()

    def update(self):

        if self.y <= 0:
            self.delta_y = abs(self.delta_y/2)

        if self.y+self.height >= self.app.h:
            self.delta_y = -abs(self.delta_y/2)

        if self.y+self.height < self.app.ball.lastNotePos['y']:
            self.delta_y = self.default['y']

        if self.y > self.app.ball.lastNotePos['y']+self.app.ball.height:
            self.delta_y = -self.default['y']

