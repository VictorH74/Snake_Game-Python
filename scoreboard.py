from turtle import Turtle, update

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.path = "high_score.txt"
        self.penup()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.high_score = self.read_file()
        self.setpos(0, 350)
        self.update_score()
        
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} / Maior Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
        
    def read_file(self):
        try:
            with open(self.path) as score_file:
                return int(score_file.readline())
        except:
            with open(self.path, "w") as score_file:
                score_file.write("0")
                return 0
        
        
    def reset(self):
        if self.score > self.high_score:
            with open(self.path, "w") as high_file:
                high_file.write(f"{self.score}")
            self.high_score = self.score
        self.score = 0
        self.update_score()
        
        
    def increase(self):
        self.score += 1
        self.update_score()