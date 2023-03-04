import turtle
import time
import random

step_size = 20
delay = 0.3  #seconds
WIDTH = 600
HEIGHT = 600
food_size = 20
head_size = 20 
snake_cell_size = 20  #default size of turtle square
score = 0
high_score = 0

#screen
sc = turtle.Screen()
sc.title("Snake Game")
sc.bgcolor("lime")
sc.setup(width = WIDTH, height = HEIGHT + 200)
sc.tracer(0)

#drawing border
t = turtle.Turtle()
t.ht()
t.up()
t.speed(0)
t.goto(-295,295)
t.down()
t.pensize(5)

for i in range(2):
    t.fd(585)
    t.rt(90)
    t.fd(590)
    t.rt(90)

#snake head
head = turtle.Turtle()
head.shape("square")
head.color("black")
head.up()
head.direction = "up"

#food
food = turtle.Turtle()
food.shape("circle")
food.color("crimson")
food.up()
food.goto(100,200)


#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.ht()
pen.up()
pen.goto(0,350)
pen.write(f"Score : {score}       High Score : {high_score}", align = "center", font = {"Courier", 100, "normal"})

#pen2
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.ht()
pen2.up()
pen2.goto(0,0)

segments = []

def move():
    if head.direction == "up":
        head.sety(head.ycor() + step_size)
    elif head.direction == "down":
        head.sety(head.ycor() - step_size)
    elif head.direction == "right":
        head.setx(head.xcor() + step_size)
    elif head.direction == "left":
        head.setx(head.xcor() - step_size)

def segment_move():
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
        segments[index].showturtle()
    if len(segments)>0:
        hx = head.xcor()
        hy = head.ycor()
        segments[0].goto(hx,hy)
        segments[0].showturtle()

def border_check():
    if head.xcor() > 290:
        head.setx(-290)
    elif head.xcor() < -290:
        head.setx(290)
    elif head.ycor() > 290:
        head.sety(-290)
    elif head.ycor() < -290:
        head.sety(290)

def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def clears(x,y):
    pen2.clear()

def check_food_collision():
    #collision detection
    if head.distance(food) <= snake_cell_size:
        x = random.randint(-WIDTH/2 + food_size, WIDTH/2 - food_size)
        y = random.randint(-HEIGHT/2 + food_size, HEIGHT/2 - food_size)
        food.goto(x,y)

        #body adding
        body = turtle.Turtle()
        body.shape("square")
        body.color("black","blue")
        body.up()
        body.hideturtle()
        segments.append(body)

        #decrease the delay
        global delay
        delay -= 0.001
        
        #increase the score
        global score
        score += 10
        global high_score
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(f"Score : {score}       High Score : {high_score}", align = "center", font = {"Courier", 100, "normal"})

        
def check_head_collision():
    for segment in segments:
        if head.distance(segment) < 20 :
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            #hide the segments
            for segment in segments:
                segment.ht()

            #clear the segmets
            segments.clear()


            #reset the score
            global score
            score = 0

            #reset the delay
            global delay
            delay = 0.5

            #game over message
            pen2.ht()
            pen.clear()
            pen2.write(f"Game Over! Click anywhere to play again", align= "center", font ={"Courier",100,"normal"})
            head.ht()
            food.ht()
            sc.onclick(clears)
            #update the score
            pen.write(f"Score : {score}       High Score : {high_score}", align = "center", font = {"Courier", 100, "normal"})


#Event handlers
sc.listen()
sc.onkey(go_up,"Up")
sc.onkey(go_down,"Down")
sc.onkey(go_right,"Right")
sc.onkey(go_left,"Left")
sc.onkey(clears,1)

#main loop
while True:
    sc.update()
    border_check()
    check_food_collision()
    segment_move()

    move()
    check_head_collision()
    head.st()
    food.st()
    time.sleep(delay)


sc.mainloop()
