from tkinter import *
from tkinter.font import Font
from Ball import Ball
from CpuPaddle import CpuPaddle
from PlayerPaddle import PlayerPaddle


class PingPong:
    i = 1

    def __init__(self, master):
        self.master = master

        # make it cover the entire screen
        self.w, self.h = root.winfo_screenwidth(), root.winfo_screenheight()
        master.overrideredirect(1)

        geometry = "%dx%d+0+0" % (self.w, self.h)
        master.geometry(geometry)

        self.canvas = Canvas(master, width=self.w, height=self.h)

        master.title("My first Game!")

        master.bind("<KeyPress>", self.onKeyDown)

        master.bind("<KeyRelease>", self.onKeyUp)

        self.canvas.pack()

        self.playerPaddle = PlayerPaddle(self)

        self.cpuPaddle = CpuPaddle(self)

        self.ball = Ball(self)

        self.playerScore = 0

        self.cpuScore = 0

        self.master.after(0, self.render)

    def onKeyDown(self, event):
        self.playerPaddle.on_key_down(event)

        # # ESC Key
        if event.keycode == 27:
            self.exit()

    def onKeyUp(self, event):
        self.playerPaddle.on_key_up(event)

    def exit(self):
        self.master.quit()

    def writeScore(self):
        helvetica = Font(family='Helvetica', size=36, weight= 'bold')
        self.canvas.create_text(self.w/6, self.h/6, text=self.playerScore, fill="blue", font=helvetica)
        self.canvas.create_text(self.w/6*5, self.h/6, text=self.cpuScore, fill="red", font=helvetica)

    def cpuWin(self):
        self.cpuScore += 1

    def playerWin(self):
        self.playerScore += 1

    def render(self):
        self.canvas.delete("all")

        self.writeScore()

        self.playerPaddle.render()

        self.cpuPaddle.render()

        self.ball.render()

        self.master.after(12, self.render)

        self.i += 1



root = Tk()

app = PingPong(root)

root.mainloop()
