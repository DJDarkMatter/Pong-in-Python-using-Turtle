# Ivan N. presenting....
# Pong in Py

# Setup:
import turtle # Turtle library
import math # Maths operations library
import random
screen = turtle.Screen() # Initialize screen for keyboardIn
tommy = turtle.Turtle() # Define turtle tommy
tommy.speed(0) # Turtle speed
tommy.hideturtle() # Hide cursor

# Functions:

  
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
    
    screen.listen() # Listen for keypresses
    screen.ontimer(loop, 1) # Restart loop with delay of 1ms--> gamespeed
    turtle.mainloop() # Keep window open to listen for keypresses

# Keypresses:
screen.onkey(w, "Up") # Call w function if uparrow detected
screen.onkey(a, "Left") # Call a function if leftarrow detected
screen.onkey(s, "Down") # Call s function if downarrow detected
screen.onkey(d, "Right") # Call d function if rightarrow detected

looprunning = True
loop()
