import turtle

def main():
    # Set up the screen
    screen = turtle.Screen()
    screen.title("Drawing a Cross")
    screen.bgcolor("white")
    
    # Create and configure the turtle
    t = turtle.Turtle()
    t.speed(5)  # Set drawing speed (1=slowest, 10=fastest)
    t.pensize(5)  # Make the line thicker
    t.color("black")
    
    # Draw vertical line
    t.penup()
    t.goto(0, 100)  # Start from top
    t.pendown()
    t.setheading(270)  # Point downward
    t.forward(200)    # Draw down
    
    # Draw horizontal line
    t.penup()
    t.goto(-100, 0)  # Start from left
    t.pendown()
    t.setheading(0)  # Point right
    t.forward(200)   # Draw right
    
    # Hide the turtle and display the result
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main() 