import turtle
# Turtle is a graphic module introducing programming to kids
def draw_rhombus (some_turtle, length, angle): 
          for i in range (1, 5): 
                    if (i % 3) <> 0: 
                              some_turtle.left(angle)
                              some_turtle.forward(length)
                    else: 
                              some_turtle.left(180 - angle)
                              some_turtle.forward(length)
                              i = i + 1

def draw_flower(some_turtle, length, angle):
          for i in range (1, 37):
                    draw_rhombus(some_turtle, length, angle)
          some_turtle.right(10)
          some_turtle.seth(270)
          some_turtle.forward(length * 4)
          
          background.exitonclick()

background = turtle.Screen() # create background
background.bgcolor("grey")   # set up background color
may = turtle.Turtle() # init
may.shape("turtle") 
may.speed(2)
may.color("#285078", "#a0c8f0")

draw_flower(may) 

background.exitonclick()
          


