from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1, 1)
        self.penup()
        self.color("purple")
        self.random_position()
        
    def random_position(self):
        x = random.randint(-240, 240)
        y = random.randint(-240, 240)
        
        self.setpos(x, y)
        
    def refresh(self):
        self.clear()
        self.random_position()