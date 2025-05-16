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
speed = 5
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
def w(): # Define function called when uparrow is hit
  if tommy.heading() == 0 or tommy.heading() == 180: # If facing opposite way
    tommy.setheading(90) # Turn up
def a(): # Define function called when leftarrow is hit
  if tommy.heading() == 90 or tommy.heading() == 270: # If facing opposite way
    tommy.setheading(180) # Turn left
def s(): # Define function called when downarrow is hit
  if tommy.heading() == 180 or tommy.heading() == 0: # If facing opposite way
    tommy.setheading(270) # Turn down
def d(): # Define function called when rightarrow is hit
  if tommy.heading() == 270 or tommy.heading() == 90: # If facing opposite way
    tommy.setheading(0) # Turn right

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
screen.onkey(w, "Up") # Call w function if uparrow detected
screen.onkey(a, "Left") # Call a function if leftarrow detected
screen.onkey(s, "Down") # Call s function if downarrow detected
screen.onkey(d, "Right") # Call d function if rightarrow detected

loop()
screen.mainloop()
