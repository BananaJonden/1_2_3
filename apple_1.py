#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()
apple.speed(1)
apple.right(90)
#-----functions-----
def apple_fall():
  apple.penup()
  apple.goto(0, -150)
def draw_letter_A():
  apple.penup()
  apple.goto(100,100)
  apple.color("black")
  apple.write("A", font=("Times New Roman", 50, "bold")) 
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
draw_letter_A()
apple.goto(0,0)

#-----function calls-----
draw_apple(apple)
wn.bgpic("background.gif")
wn.listen()
wn.onkeypress(apple_fall, "a")
wn.mainloop()
