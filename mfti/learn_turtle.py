import turtle
import math

turtle.shape('turtle')

# ! S - character

# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(50)

# ! Square

# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)

# ! Circle

# for i in range(1, 361, 1):
# 	turtle.forward(1)
# 	turtle.left(1)

# ! 10 вложенных квадратов

# x = 0
# path = 50
# step = 5

# for i in range(1, 11, 1):
# 	turtle.penup()
# 	turtle.goto(x, x)
# 	turtle.pendown()	
# 	turtle.forward(path)
# 	turtle.left(90)
# 	turtle.forward(path)
# 	turtle.left(90)
# 	turtle.forward(path)
# 	turtle.left(90)
# 	turtle.forward(path)
# 	turtle.left(90)
# 	x -= step
# 	path += 10

# ! Spider

# x = 0
# path = 100
# points = 12
# turn = 360 / points
# turtle.goto(x, x)

# for i in range(1, 13, 1):
# 	turtle.pendown()
# 	turtle.forward(path)
# 	turtle.stamp()
# 	turtle.penup()
# 	turtle.backward(path)
# 	turtle.right(turn)

# ! Спираль

# * первый вариант

# x = 0
# rings = 10
# turn = 1
# turtle.goto(x, x)
# path = 360 * rings + 1

# for i in range(path):
# 	turtle.forward(i * 0.001)
# 	turtle.left(turn)

# * второй вариант

# x = 0
# turtle.goto(x, x)

# k = 1
# fi_rad = 0.1
# fi_degr = math.degrees(fi_rad)

# for i in range(0, 500):
# 	ro = k * fi_rad
# 	turtle.forward(ro)
# 	turtle.left(fi_degr)
# 	fi_rad += 0.05

# ! Квадратная спираль

# x = 0
# turtle.goto(x, x)

# step = 10
# acceleration = 10
# path = 40 + 1

# for i in range(1, path):
# 	turtle.forward(step)
# 	turtle.left(90)
# 	step += acceleration

# ! 10 вложенных правильных многоугольников

# * первый вариант - не очень корректно работает

# r = 50
# step = 5

# def multiangle(n):
# 	# global ab
# 	global step
# 	global r
# 	a = 360 / n
# 	b = 180 - a
# 	ab = r / (2 * math.sin(math.radians(360 / (2 * n))))
# 	# radius = ab / (2 * math.sin(math.radians(360 / (2 * n))))
# 	turtle.left(b/2)
# 	for i in range(0, n):
# 		turtle.left(a)
# 		turtle.forward(ab)
# 	turtle.right(b/2)
# 	turtle.penup()
# 	turtle.forward(step)
# 	turtle.pendown()

# for i in range(3, 10):
# 	multiangle(i)
# 	r += step


# * второй вариант - работает корректно

# t = turtle.Turtle()
# t.shape('turtle')
# R = 30
# x = 1
# n = 3
# t.up()
# t.goto(R, 0)
# t.down()
# def polygon(x):
# 	while x <= n:
# 		t.left((180 - 360 / n) / 2)
# 		t.left(360 / n)
# 		t.forward(2 * R * math.sin(math.pi/n))
# 		x += 1
# 		t.right((180 - 360 / n) / 2)
# while n <= 11:
# 	polygon(x)
# 	n += 1
# 	R += 18
# 	t.up()
# 	t.goto(R, 0)
# 	t.down()
# turtle.exitonclick()

# ! Flower

# r = 50
# n = 6
# angle = 360 / 6
# x = 0

# while x < n / 2:
# 	turtle.circle(r)
# 	turtle.circle(-r)
# 	turtle.left(angle)
# 	x += 1

# ! Butterfly

# r = 50
# n = 10
# x = 0
# turtle.left(90)

# while x < n:
# 	turtle.circle(-r)
# 	turtle.circle(r)
# 	r += 10
# 	x += 1

# ! Пружина

# n = 4
# r1 = -50
# r2 = -10

# turtle.left(90)

# for i in range(n):
# 	turtle.circle(r1, 180)
# 	turtle.circle(r2, 180)

# ! Smile

# turtle.left(90)
# turtle.fillcolor('yellow')
# turtle.begin_fill()
# turtle.circle(100)
# turtle.end_fill()
# turtle.penup()
# turtle.goto(-125, 50)
# turtle.pendown()
# turtle.fillcolor('blue')
# turtle.begin_fill()
# turtle.circle(10)
# turtle.end_fill()
# turtle.penup()
# turtle.goto(-50, 50)
# turtle.pendown()
# turtle.fillcolor('blue')
# turtle.begin_fill()
# turtle.circle(10)
# turtle.end_fill()
# turtle.penup()
# turtle.goto(-100, 25)
# turtle.pendown()
# turtle.fillcolor('black')
# turtle.left(180)
# turtle.begin_fill()
# turtle.width(10)
# turtle.forward(50)
# turtle.end_fill()
# turtle.penup()
# turtle.goto(-50, -25)
# turtle.pendown()
# turtle.color('red')
# turtle.width(10)
# turtle.left(180)
# turtle.circle(50, -180)

# ! Stars

# ab = 200

# turtle.left(180)

# def star(n):
# 	a = 180 / n
# 	turn = 180 - a

# 	for i in range(n):
# 		turtle.forward(ab)
# 		turtle.left(turn)

# star(11)
