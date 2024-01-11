from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial",20,"normal")

#顯示分數和Game over等標記

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score=0
        self.updatescore()

    def updatescore(self):
        self.goto(0, 270)
        self.write(f"SCORE = {self.score}",True, align=ALIGNMENT,font=FONT)
        self.goto(0,250)
#        self.write("-"*300,True, align=ALIGNMENT,font=FONT)

    def addscore(self):
        self.score+=1
        self.clear()
        self.updatescore()

    def gameover(self):
        #self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER",True, align=ALIGNMENT, font=FONT)