from turtle import *
import time
shape("turtle")
pensize(5)
speed(10)

#1
diomedes=clone()
color("white")
diomedes.speed(0)
diomedes.color("white")
diomedes.left(180)
diomedes.forward(150)
diomedes.right(90)
diomedes.forward(100)
diomedes.left(90)
diomedes.color("green")
diomedes.forward(100)
diomedes.left(180)
diomedes.forward(50)
diomedes.left(90)
diomedes.forward(100)
diomedes.left(90)
diomedes.forward(50)
diomedes.color("white")

#2
niche=clone()
niche.speed(0)
niche.left(180)
niche.forward(150)
niche.color("orange")
grupo=niche.clone()
grupo.speed(0)
grupo.left(90)
niche.forward(100)
niche.color("white")
grupo.forward(50)
grupo.right(90)
grupo.forward(100)
grupo.left(90)
grupo.forward(50)
grupo.left(90)
grupo.forward(100)
grupo.color("white")

#3
binomio_de_oro=grupo.clone()
binomio_de_oro.right(90)
binomio_de_oro.forward(100)
binomio_de_oro.left(90)
binomio_de_oro.forward(100)
binomio_de_oro.color("purple")
binomio_de_oro.forward(100)
binomio_de_oro.right(90)
binomio_de_oro.forward(50)
olvidala=binomio_de_oro.clone()
olvidala.right(90)
olvidala.forward(100)
olvidala.color("white")
binomio_de_oro.forward(50)
binomio_de_oro.right(90)
binomio_de_oro.forward(100)
binomio_de_oro.color("white")

#4
kaleth_morales=clone()
kaleth_morales.speed(0)
kaleth_morales.forward(150)
kaleth_morales.left(90)
kaleth_morales.forward(100)
kaleth_morales.color("black")
kaleth_morales.right(90)
kaleth_morales.forward(100)
peter_manjarres=kaleth_morales.clone()
kaleth_morales.left(90)
kaleth_morales.forward(50)
kaleth_morales.left(90)
kaleth_morales.forward(100)
kaleth_morales.right(90)
kaleth_morales.forward(50)
kaleth_morales.right(90)
kaleth_morales.forward(100)
kaleth_morales.color("white")

#5
peter_manjarres.right(90)
peter_manjarres.forward(5)
peter_manjarres.color("white")
peter_manjarres.forward(95)
peter_manjarres.color("red")
peter_manjarres.forward(50)
silvestre_dangond=peter_manjarres.clone()
peter_manjarres.forward(100)
peter_manjarres.color("white")
silvestre_dangond.right(90)
silvestre_dangond.forward(100)
silvestre_dangond.right(90)
silvestre_dangond.forward(50)
silvestre_dangond.color("white")

#a
color('#FFC300')
penup()
goto (0,-8)
pendown()
circle(10)
penup()
goto (85,95)
pendown()
color("black")
b=clone()
b.speed(0)
b.color("purple")
b.penup()
b.goto(0,-100)
b.pendown()
b.left(90)
#b.circle(100)  
#c
c=clone()
c.color("green")
c.penup()
c.goto(-85,95)
c.pendown()
c.right(45)
#d
d=clone()
d.color("red")
d.penup()
d.goto(100,0)
d.pendown()
d.left(180)
#e
e=clone()
e.color("orange")
e.penup()
e.goto(-100,0)
e.pendown()

left(225)
time.sleep(3)
start_time = time.time()
elapsed_time = time.time() - start_time
while(elapsed_time <=60):
  b.color("blue")
  c.color("blue")
  time.sleep(2)
  color("lime")
  d.color("lime")
  e.color("lime")
  b.penup()
  b.goto(0,0)
  b.pendown()
  c.penup()
  c.goto(0.0)
  c.penup()
  print("Filosofos 1 y 3 comen mientras los demas piensan")
  time.sleep(2)
  color("black")
  b.color("purple")
  c.color("green")
  d.color("red")
  e.color("orange")
  b.penup()
  b.goto(0,-100)
  b.pendown()
  c.penup()
  c.goto(-85,95)
  c.pendown()
  time.sleep(2)
  #---------------
  e.color("blue")
  d.color("blue")
  time.sleep(3)
  color("lime")
  b.color("lime")
  c.color("lime")
  e.penup()
  e.goto(0,0)
  e.pendown()
  d.penup()
  d.goto(0.0)
  d.penup()
  print("Filosofos 2 y 4 comen mientras los demas piensan")
  time.sleep(2)
  color("black")
  b.color("purple")
  c.color("green")
  d.color("red")
  e.color("orange")
  e.penup()
  e.goto(-100,0)
  e.pendown()
  d.penup()
  d.goto(100,0)
  d.pendown()
  time.sleep(2)
  #-----------------------
  e.color("blue")
  color("blue")
  time.sleep(2)
  d.color("lime")
  b.color("lime")
  c.color("lime")
  e.penup()
  e.goto(0,0)
  e.pendown()
  penup()
  goto(0.0)
  penup()
  print("Filosofos 2 y 5 comen mientras los demas piensan")
  time.sleep(2)
  color("black")
  b.color("purple")
  c.color("green")
  d.color("red")
  e.color("orange")
  e.penup()
  e.goto(-100,0)
  e.pendown()
  penup()
  goto(85,95)
  pendown()
  time.sleep(2)
  print("-------------------------------------------------------")
