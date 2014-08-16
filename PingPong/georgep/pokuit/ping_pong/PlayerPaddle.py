from Paddle import Paddle

__author__ = 'George'

class PlayerPaddle(Paddle):
    def __init__(self, app):
        super().__init__(app.canvas)
        self.app = app
        self.width = 50
        self.height = 200
        self.x = 5
        self.y = (self.app.h - self.height) / 2
        self.color = "blue"
        self.default = {
            'y': app.h/100
        }
        self.init()

    def render(self):
        ctx = self.ctx

        if self.y <= 0:
            self.delta_y = abs(self.delta_y/2)

        if self.y+self.height >= self.app.h:
            self.delta_y = -abs(self.delta_y/2)

        self.add_delta()
        ctx.create_rectangle(self.x, self.y, self.x + self.width, self.height + self.y, fill=self.color)

    def init(self):
        pass

    def on_key_down(self, event):
        if event.keycode == 38:
            self.delta_y = -self.default['y']

        if event.keycode == 40:
            self.delta_y = self.default['y']

    def on_key_up(self, event):
        if event.keycode == 38 or event.keycode == 40:
            self.delta_y = 0

    def add_delta(self):
        self.x += self.delta_x
        self.y += self.delta_y
