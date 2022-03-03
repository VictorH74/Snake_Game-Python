import turtle
from difficulty_bar import DifficultyBar
from map import Constructor
from food import Food
from scoreboard import ScoreBoard
from snake import Snake
import time

screen_width = 1400
screen_height = 800
x_position = 300

image = "img.gif"


screen = turtle.Screen()
#screen.addshape(image)
#turtle.shape(image)
screen.title("Snake Game")
screen.bgcolor('black')
screen.setup(screen_width, screen_height)
screen.tracer(0)


colors_level = ["Olive", "YellowGreen", "GreenYellow", "Goldenrod", "Orange", "DarkOrange", "DarkRed"]


snake = Snake()
snake_2 = Snake()
food = Food()
pedro = Constructor(x_position)
leitao = ScoreBoard()
barra_dificuldade = DifficultyBar(x_position)

no_repeat = 0

def had_collision():
    
    if snake.head.xcor() > x_position * 2 - 20 or snake.head.xcor() < (x_position * 2) * -1 + 20:
        return True
    elif snake.head.ycor() > x_position-10 or snake.head.ycor() < (x_position - 10) * -1:
        return True
    else:
        return False
    

def check_level():
    global no_repeat
    
    if leitao.score < 10:      
        time.sleep(0.08)
 
    elif leitao.score < 15:
        time.sleep(0.07)
        for segment in snake.segments:
            segment.color(colors_level[0])
        if no_repeat != 1:
            barra_dificuldade.create_bar()
        no_repeat = 1
            
    elif leitao.score < 20:
        time.sleep(0.06)
        for segment in snake.segments:
            segment.color(colors_level[1])
        if no_repeat != 2:
            barra_dificuldade.create_bar()
        no_repeat = 2
        
    elif leitao.score < 25:
        time.sleep(0.05)
        for segment in snake.segments:
            segment.color(colors_level[2])
        if no_repeat != 3:
            barra_dificuldade.create_bar()
        no_repeat = 3
        
    elif leitao.score < 30:
        time.sleep(0.04)
        for segment in snake.segments:
            segment.color(colors_level[3])
        if no_repeat != 4:
            barra_dificuldade.create_bar()
        no_repeat = 4
        
    elif leitao.score < 45:
        time.sleep(0.03)
        for segment in snake.segments:
            segment.color(colors_level[4])
        if no_repeat != 5:
            barra_dificuldade.create_bar()
        no_repeat = 5
        
    elif leitao.score < 50:
        time.sleep(0.02)
        for segment in snake.segments:
            segment.color(colors_level[5])
        if no_repeat != 6:
            barra_dificuldade.create_bar()
        no_repeat = 6
        
    elif leitao.score >= 50:
        time.sleep(0.01)
        for segment in snake.segments:
            segment.color(colors_level[6])
        if no_repeat != 7:
            barra_dificuldade.create_bar()
        no_repeat = 7
    
    
def snake2_collision():
    if snake_2.head.xcor() > x_position * 2 - 40: # PAREDE DIREITA
        snake_2.head.setheading(90)
        
    if snake_2.head.xcor() < (x_position * 2) * -1 + 40: # PAREDE ESQUERDA
        snake_2.head.setheading(270)
    elif snake_2.head.ycor() > x_position - 40: # CIMA
        snake_2.head.setheading(180)
        
    if snake_2.head.ycor() < (x_position - 40) * -1: # BAIXO
        snake_2.head.setheading(0)
        
    if snake_2.head.xcor() > x_position * 2 - 40 and snake_2.head.ycor() < (x_position - 40) * -1:
        snake_2.head.setheading(90)
            

screen.listen()
screen.onkeypress(key="w", fun=snake.up)
screen.onkeypress(key="s", fun=snake.down)
screen.onkeypress(key="a", fun=snake.left)
screen.onkeypress(key="d", fun=snake.right)
screen.onkeypress(key="Up", fun=snake.up)
screen.onkeypress(key="Down", fun=snake.down)
screen.onkeypress(key="Left", fun=snake.left)
screen.onkeypress(key="Right", fun=snake.right)

    
while True:
        
    screen.update() # -> Atualiza a tela apenas quando for retornado a esse metodo pelo while
    
    check_level()
    
    # Mover cobra
    snake.move() 
    snake_2.move()
    
    snake2_collision()

    if snake.head.distance(food) < 20:
        leitao.increase()
        food.refresh()
        
        
    if had_collision():
        snake.reset()
        leitao.reset()
        barra_dificuldade.reset()
        
    

    
#x_1 = snake.head.xcor()
#y_1 = snake.head.ycor()

#if snake.head.xcor() > 280:
#    x_1 = -280
#elif snake.head.xcor() < -280:
#    x_1 = 280
#elif snake.head.ycor() > 280:
#    y_1 = -280
#elif snake.head.ycor() < -280:
#    y_1 = 280
    
#snake.head.setpos(x_1, y_1)

