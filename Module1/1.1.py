# Till now, you have written Python programs, which displayed textual output.
# Do you want to see if you can get graphical output using Python.
# So get ready to explore.
# In this journey, we are joined by our great friend Mr. Turtle from the “Turtle and Hare” story. 

'''Task 1: Let's get the turtle moving'''
print("****** Task 1: ******")
print()
# Do you know what a turtle is? 
# In Python,“Turtle” is a module using which you can create graphics. You can set the cursor to a shape of a turtle holding a pen, and draw shapes.
# But before you get started, you need to import the turtle module, so that you can get working with the commands
# Uncomment the statement below and click Run
import turtle
turtle.shape("arrow")
# What did you observe?
# Turtle module is imported using the import command
# The shape of the cursor is changed to an arrow using the shape() function/method
# You can change the shape of the cursor to the following using the shape() function.
# - circle
# - square
# - triangle
# - turtle
# Mr.Turtle wants you to write a program to try out each of the above styles. Observe how the shape of the cursor changes, each time you change the shape. 
# Note: Remember to change and execute the shape one at a time.
import turtle
turtle.shape("circle")
turtle.shape("square")
turtle.shape("triangle")
turtle.shape("turtle")


'''Task 2: Setting the cursor shape'''
print("***** Task 2: *****")
print()
# Impressed with your first task, Mr.Turtle wants you to get on to the next, which is to set the colour the turtle will use to draw.
# Uncomment the next statement and click Run
#import turtle
#turtle.shape("turtle")
#turtle.color("blue")
# Did you notice the turtle change in colour? What colour did it change to? [Wait for the student to answer]
# Mr.Turtle now wants you to write a program to change the line colour as listed below:
# - aquamarine
# - goldenrod
# - DarkKhaki
# - LimeGreen
# Observe how the colour of the cursor changes, each time you change the colour. 
# NOTE: Remember to change and execute the colour one at a time.
import turtle
turtle.shape("turtle")
turtle.color("aquamarine")
turtle.color("goldenrod")
turtle.color("DarkKhaki")
turtle.color("LimeGreen")

'''Task 3: All about coordinates'''
print("****** Task 3: ******")
print()
# Mr.Turtle now wants you to understand the concept of direction when working with the turtle.
# If you notice the turtle’s head is facing to the right of the screen which is the default position  of the turtle. It is denoted by 0 as shown in the image below.
# If the heading is set to 90, the turtles head points to the top (North).
# If the heading is set to 180, the turtles head points to the left
# If the heading is set to 270, the turtles head points south (bottom).
# The command used to set the heading of the turtle is setheading(). 
#Uncomment the statement below, one at  a time and see how the turtle changes the direction.
#Note: Remember to change and execute the directions one at a time.
#import turtle
#turtle.shape("turtle")
#turtle.color("Limegreen")
#turtle.setheading(0)
#turtle.setheading(90)
#turtle.setheading(180)
#turtle.setheading(270)

# Now before we get our turtle to move we need to set couple of things:
# Step 1: pensize
# You can set the thickness of the line by  using the pensize() function. 
# For example: 
# turtle.pensize(4)

# Step 2: pendown
# You need to put the turtle's pen down,using the pendown() function, to start drawing:
# turtle.pendown()
# If you want to move without drawing a line we  use the penup() function:
# turtle.penup()

#Step 3: Getting the turtle to move
# You can get the turtle to move using the following functions:
# - forward(). For example: 
#forward(50)
# - backward(). For example: 
#backward(70)
# - left(). For example: 
#left(120)
# - right(). For example: 
#right(90)
# Here the values you specify within the bracket for each of the functions(i.e. forward(),backward(),left() and right()) refers to the pixel value. Pixels are the dots that makeup up the pictures on your screen.

# Step 4: goto
# If you want to move the turtle to a particular position before drawing, you have to  use the goto() function. 
# To undersstand how to work with coordinates watch the video: https://www.youtube.com/watch?v=Qc62g4RyARY
# To move the turtle to the position x=100 and y=100, you will use the goto() function as follows:
# turtle.goto(100,100) 

#Step 5: Speed
# You can set the speed at which your turtle moves using the speed() function.
# You can either specify the values -"slowest", "slow", "normal","fast","fastest" or specify values between 1 and 10 to set the turtle speed.
# For example:
# turtle.speed("fast")
# turtle.speed(9)

# Step 6: Background Colour
# You can set the background colour using the bgcolor() functions
# For example:
#turtle.bgcolor(pink)
# Let us try what has been described in the steps above. Uncomment the statements below and click Run
#import turtle
#turtle.shape("turtle")
#turtle.color("Limegreen")
#turtle.bgcolor("pink")
#turtle.penup()
#turtle.goto(50,50)
#turtle.pensize(4)
#turtle.speed(6)
#turtle.pendown()
#turtle.left(90)
#turtle.forward(100)
#turtle.right(90)
#turtle.forward(100)
#turtle.right(90)
#turtle.forward(50)
#turtle.right(90)
#turtle.forward(100)
# What did you get? 
# You got the turtle to draw the alphabet P
# Now Mr.Turtle wants you to write a program to draw any alphabet from your name. Go ahead and give it a try
import turtle
turtle.shape("turtle")
turtle.color("orange")
turtle.penup()
turtle.setheading(0)
turtle.goto(-60,10)
turtle.pensize(4)
turtle.speed(4)
turtle.pendown()
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.left(150)
turtle.forward(95)

'''Task 4: What's in an alphabet?'''
print("****** Task 4: ******")
print()
# Mr.Turtle is very impressed with your skills and now wants you to try making the following alphabets:
# - L 
# - V
#Alphabet L
turtle.clearscreen()
turtle.shape("turtle")
turtle.color("aquamarine")
turtle.penup()
turtle.goto(-100,100)
turtle.pensize(4)
turtle.speed(4)
turtle.pendown()
turtle.forward(100)
turtle.backward(100)
turtle.left(90)
turtle.forward(100)
#Alphabet V
turtle.shape("turtle")
turtle.color("aquamarine")
turtle.penup()
turtle.goto(-40,-50)
turtle.pensize(4)
turtle.speed(4)
turtle.pendown()
turtle.right(30)
turtle.forward(100)
turtle.backward(100)
turtle.left(60)
turtle.forward(100)
#move the turtle
turtle.penup()
turtle.goto(0,-50)

'''Fantastic!! You have gotten to a good start with the turtle graphics.'''