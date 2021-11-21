from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 20, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        with open('record_score.txt', 'r') as file:
            self.max_score = int(file.read())
        self.penup()
        self.goto(0,270)
        self.ht()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score : {self.score} Max score : {self.max_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score +=1
        self.update_scoreboard()

    def reset_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score
            with open('record_score.txt', 'w') as file:
                file.write(f'{self.max_score}')
        self.score = 0
        self.update_scoreboard()


