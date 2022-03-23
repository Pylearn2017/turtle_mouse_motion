import turtle
import time
import random


def iscollision(obj1, obj2, w1, w2, h1, h2):
	if obj1.xcor() + w1 > obj2.xcor() - w2 and obj1.xcor() - w1 < obj2.xcor() + w2:
		if obj1.ycor() + h1 > obj2.ycor() - h2 and obj1.ycor() - h1 < obj2.ycor() + h2:
			return True
	return False

def motion(event):
    x, y = event.x, event.y
    x = x - 400
    y = y - 400
    helper.setposition(x,-y)
    for hero in heroes:
	    if hero.grab:
		    hero.setposition(x,-y)

def click(x,y):
	for hero in heroes:
		if iscollision(helper, hero, 20, 20, 20, 20):
			if hero.grab:
				hero.grab = False
			else:	
				hero.grab = True

window = turtle.Screen()
window.setup(800, 800)
window.tracer(0)

helper = turtle.Turtle()
helper.speed(0)
helper.penup()
helper.hideturtle()

writer = turtle.Turtle()
writer.speed(0)
writer.penup()
writer.hideturtle()

heroes = []
edibles = []
inedibles = []
for i in range(10):
	hero = turtle.Turtle()
	hero.penup()
	hero.speed(0)
	hero.shape('square')
	hero.shapesize(4,4)
	hero.subject = random.choice(['edible', 'inedible'])
	hero.setposition(random.randint(-400, 400),random.randint(-400, 400))
	hero.grab = False
	if hero.subject == 'edible':
		hero.color('green')
		edibles.append(hero)
	elif hero.subject == 'inedible':
		inedibles.append(hero)
	heroes.append(hero)

window.onclick(click)
canvas = turtle.getcanvas()
canvas.bind('<Motion>', motion)

while True:
	if all([edible.xcor() < -100 for edible in edibles]):
		if all([inedible.xcor() > 100 for inedible in inedibles]):
			writer.write('Right!', font=('Arial', 68, 'normal'))
			break

	time.sleep(.1)
	window.update()
window.update()
turtle.done()