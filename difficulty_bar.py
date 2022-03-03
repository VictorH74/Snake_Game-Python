from turtle import Turtle

CONST_Y = -278

class DifficultyBar:
    def __init__(self, size):
        self.CONST_X = size * 2 + 35
        self.increase = 0
        self.color_index = 0
        self.level_bar = []
        self.colors_level = ["green", "Olive", "YellowGreen", "GreenYellow", "Goldenrod", "Orange", "DarkOrange", "DarkRed"]
        
        self.create_bar()
        
        self.first_level = self.level_bar[0]

        
    def create_bar(self):
        
        # -278 + 0
        y_position = CONST_Y + self.increase
        
        new_level = Turtle(shape="square")
        new_level.penup()
        new_level.color(self.colors_level[self.color_index])
        new_level.setpos(self.CONST_X, y_position)
        new_level.shapesize(2.0, 3.0)
        self.level_bar.append(new_level)
        
        # 0 = 20
        self.increase += 50
        self.color_index += 1
        
        
    def reset(self):
        for block_level in self.level_bar:
            block_level.goto(1000, 1000)
            
        #self.level_bar.clear()
        self.increase = 0
        self.color_index = 0
        
        self.create_bar()
        