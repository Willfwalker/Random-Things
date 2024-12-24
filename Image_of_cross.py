import turtle  # Changed from turtles

def main():
    screen = turtle.Screen()  # Changed from turtles
    cross = turtle.Turtle()  # Changed from turtles
    
    # Drawing the cross
    cross.shape("turtle")
    cross.color("red")
    cross.penup()
    cross.goto(-50, 150)  # Start position for vertical line
    cross.pendown()
    cross.setheading(270)  # Point downward
    cross.forward(300)     # Draw vertical line
    
    cross.penup()
    cross.goto(-150, 50)   # Start position for horizontal line
    cross.setheading(0)    # Point right
    cross.pendown()
    cross.forward(300)     # Draw horizontal line
    
    screen.mainloop()
