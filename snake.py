from turtle import Turtle

STARTING_X_POSITION = 0

MOVE_DISTANCE = 20

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        x_position = STARTING_X_POSITION
        
        for _ in range(8):
            new_segment = Turtle(shape="circle") 
            new_segment.color("green")
            new_segment.penup()
            new_segment.setposition(x_position, 0)
            
            x_position -= 20
            
            self.segments.append(new_segment)
            

    def move(self):
        for seg_num in range(len(self.segments)-1 ,0 , -1): # -> "step= -1" INDICAR QUE É UM FOR EM FORMA DECRESCENTE. Ex.:(i--)
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            
            self.segments[seg_num].setpos(new_x, new_y)
        
        self.head.forward(MOVE_DISTANCE)
        
        
    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            
    
    def down_s2(self):
        self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
           