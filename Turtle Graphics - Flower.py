import turtle

# Turtle is a graphic module introducing programming to kids

def draw_flower(some_turtle):
          for i in range (1, 37):
                    some_turtle.left(35)
                    some_turtle.forward(100)
                    some_turtle.right(35)
                    some_turtle.forward(100)
                    some_turtle.right(145)
                    some_turtle.forward(100)
                    some_turtle.right(35)
                    some_turtle.forward(100)
                    some_turtle.right(10)
                    
          some_turtle.seth(270)
          some_turtle.forward(400)


background = turtle.Screen() # create background
background.bgcolor("grey")

may = turtle.Turtle() # init
may.shape("turtle") 
may.speed(2)
may.color("#285078", "#a0c8f0")
draw_flower(may) 

background.exitonclick()
          


