from Entity import Entity

__author__ = 'George'

class Paddle(Entity):
    def render(self):

        self.update()
        ctx = self.ctx

        self.add_delta()
        ctx.create_rectangle(self.x, self.y, self.x + self.width, self.height + self.y, fill=self.color)

    def update(self):
        pass
