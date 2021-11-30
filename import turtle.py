import turtle
import random

turtle.delay(0)

tortue = turtle.Turtle()
"""
-----------------------------
Tri Selection
-----------------------------
"""
def selectMin(list):
    var=list[0]
    for i in list:
        if var >i:
            var =i
    return var

def triSelect (list):
    result = []
    while len(list) > 0:
        var= selectMin(list)
        result.append(var)
        
    return result

print(triSelect(12,43,56,85,2,8,6,4,5))
        
"""
-----------------------------
Tri Fusion
-----------------------------
"""

"""
------------------------------
Exercice 1
------------------------------
"""
"""
tortue.forward(50)
tortue.left(90)
tortue.forward(50)
tortue.left(90)
tortue.forward(50)
tortue.left(90)
tortue.forward(50)

tortue.circle(50)
"""


"""
------------------------------
Exercice 2
------------------------------
"""
"""
"Carre"
i=0
while True:
    i+=2
    tortue.forward(i)
    tortue.left(90)
"""
"""
"rond"
i=0
tortue.speed(110)
while True:
    i+=1
    tortue.circle(i,i,i)
"""
"""
------------------------------
Exercice 3
------------------------------
"""
"""
"ligne droite à l'infini"
i=0
while True:
    i+=1
    tortue.forward(i)
"""
"tourner aléatoire"
"""
while True:
    i = random.randint(1,3)
    if i == 1:
        i= tortue.left(90)
    elif i == 2:
        tortue.right(90)
    else :
        i= tortue.forward(1)
"""
"ajouter plusieurs tortues"
"""
n=10
tortues= []
turtle.delay(0)

for i in range(n):
    tortues.append(turtle.Turtle())

while True:
    for i in tortues:
        i.forward(5)
        i.left(random.randint(-360,360))
"""
"Ajouter une couleurs diff"
"""
n=10
tortues= []
turtle.delay(0)


for i in range(n):
    color= turtle.Turtle()
    tortues.append(color)
    color.color(random.random(),random.random(),random.random())
    color.pensize(3)

while True:
    for i in tortues:
        i.forward(5)
        i.left(random.randint(-360,360))
"""
"""
------------------------------
Exercice 4
------------------------------
"""
"""
n=20
tortues= []



for i in range(n):
    var= turtle.Turtle()
    var.penup()
    var.shape('circle')
    var.shapesize(2,2)
    var.color(1,1,1)
    var.setposition(random.randint(-250,250),random.randint(-250,250))
    tortues.append(var)
    var.color(random.random(),random.random(),random.random())
    var.pensize(3)

    i=0
    
while True:
    for i in tortues:
        i.forward(5)
        i.left(random.randint(-360,360))
        for i in tortues:
            for j in tortues:
                
                eat = random.randint(0,1)
                if i!=j:
                    if i.distance(j)<=(i.shapesize()[0]+j.shapesize()[0])*5:
                        if i.shapesize() >= j.shapesize():
                            i.shapesize(i.shapesize()[0]+j.shapesize()[0],i.shapesize()[0]+j.shapesize()[0])
                            j.hideturtle()
                            i.speed()
                            tortues.remove(j)
                        elif j.shapesize() > i.shapesize():
                            j.shapesize(j.shapesize()[0]+i.shapesize()[0],j.shapesize()[0]+i.shapesize()[0],j.shapesize()[0]+i.shapesize()[0])
                            i.hideturtle()
                            j.speed()
                            tortues.remove(i)
                        elif i.shapesize() == j.shapesize():
                            if eat == 0:
                                i.shapesize(i.shapesize()[0]+j.shapesize()[0],i.shapesize()[0]+j.shapesize()[0],i.shapesize()[0]+j.shapesize()[0])
                                j.hideturtle()
                                i.speed()
                                tortues.remove(j)
                            elif eat == 1:
                                j.shapesize(j.shapesize()[0]+i.shapesize()[0],j.shapesize()[0]+i.shapesize()[0],j.shapesize()[0]+i.shapesize()[0])
                                i.hideturtle()
                                j.speed()
                                tortues.remove(i)
                                
input()
"""
