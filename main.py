# Ivan N. presenting....
# Pong in Py

# Setup:
import turtle # Turtle library
import math # Maths operations library
import random
screen = turtle.Screen() # Initialize screen for keyboardIn
screen.listen() # Listen for keypresses
tommy = turtle.Turtle() # Define turtle tommy
tommy.penup()
tommy.speed(0) # Turtle speed
tommy.hideturtle() # Hide cursor
lefty = turtle.Turtle() # Define turtle lefty
lefty.penup()
lefty.speed(0) # Turtle speed
lefty.hideturtle() # Hide cursor
righty = turtle.Turtle() # Define turtle righty
righty.penup()
righty.speed(0) # Turtle speed
righty.hideturtle() # Hide cursor
speed = 1
looprunning = True

# Functions:

def ball():
  tommy.forward(5)
  tommy.left(90) # Move to side so circle is on center
  tommy.begin_fill() # Color start
  tommy.circle(5) # Draw apple
  tommy.end_fill() # Color stop
  tommy.right(90)
  tommy.backward(5) # Move back to center

def delball():
  tommy.forward(6)
  tommy.left(90) # Move to side so circle is on center
  tommy.begin_fill() # Color start
  tommy.circle(6) # Draw apple
  tommy.end_fill() # Color stop
  tommy.right(90)
  tommy.backward(6) # Move back to center
  
# Keypresses:
def w(): # Define function called when w is hit
  pass
def s(): # Define function called when s is hit
  pass
def u(): # Define function called when downarrow is hit
  pass
def d(): # Define function called when rightarrow is hit
  pass
def r(): # Define reset function
  pass

# Loop
def loop(): # Define main loop function gets called in last line of main loop
  if looprunning is True:
    tommy.fillcolor("white")
    delball()
    
    tommy.forward(speed)
    tommy.color("black")
    ball()
    screen.ontimer(loop, 5)# Restart loop with delay of 1ms

# Keypresses:
screen.onkey(w, "w") # Call w function if uparrow detected
screen.onkey(s, "s") # Call s function if leftarrow detected
screen.onkey(u, "Up") # Call u function if downarrow detected
screen.onkey(d, "Down") # Call d function if rightarrow detected
screen.onkey(r, "r") # Call r function if "r" detected

loop()
screen.mainloop()
