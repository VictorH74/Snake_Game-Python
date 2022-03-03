from turtle import Turtle

#MAP_SIZE = 600 # num x num
#FORWARD_NUM = MAP_SIZE * 2

class Constructor(Turtle):
    def __init__(self, size):
        super().__init__()
        self.map_size = size
        self.FORWARD_NUM_Y = self.map_size * 2
        self.FORWARD_NUM_X = self.FORWARD_NUM_Y * 2
        self.STARTING_POSITION = size + size
        self.setpos(self.STARTING_POSITION, self.map_size)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.build_map()
        
        
    def build_map(self):
        
        self.pendown()
        
        self.setheading(270)
        self.forward(self.FORWARD_NUM_Y)
        self.setheading(180)
        self.forward(self.FORWARD_NUM_X)
        self.setheading(90)
        self.forward(self.FORWARD_NUM_Y)
        self.setheading(0)
        self.forward(self.FORWARD_NUM_X)
        
        self.penup()
        