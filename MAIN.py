import turtle as t
import math as mt

t.speed(1000000000)
t.color("Blue")
t.bgcolor('Black')
t.setup(700, 700)
t.pensize(3)
x,y = 1,0

for i in range(4):
     t.fd(350)
     t.left(180)
     t.fd(350)
     t.left(90)

print('Количество итераций:')
#n = int(input())
t.color("Green")

for i in range(200):
     t.goto(x,y)
     y = x**2 #Сдесь поставте свою функцию
     x +=1

x,y = 1,0
t.up()
t.goto(x,y)
t.down()
for i in range(200):
     t.goto(x,y)
     y = x**2 #Сдесь поставте свою функцию
     x -=1
