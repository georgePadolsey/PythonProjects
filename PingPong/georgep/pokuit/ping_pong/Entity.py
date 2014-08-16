__author__ = 'George'

class Entity:
    def __init__(self, ctx):
        self.ctx = ctx
        self.x = 0
        self.y = 0
        self.height = 0
        self.width = 0
        self.color = "white"
        self.delta_x = 0
        self.delta_y = 0

    def render(self):
        ctx = self.ctx

        self.add_delta()
        ctx.create_rectangle(self.x, self.y, self.x + self.width, self.height + self.y, fill=self.color)

    def init(self):
        pass

    def add_delta(self):
        self.x += self.delta_x
        self.y += self.delta_y
