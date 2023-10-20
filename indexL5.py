import turtle
turtle.shape('turtle') 
turtle.up()

def zero(x, y):
    turtle.goto(x,y)
    turtle.down()
    turtle.rt(90)
    turtle.fd(40)
    turtle.lt(90)
    turtle.fd(20)
    turtle.lt(90)
    turtle.fd(40)
    turtle.lt(90)
    turtle.fd(20)
    turtle.up()

def one(x, y):
    turtle.goto(x,y)
    turtle.rt(90)
    turtle.fd(20)
    turtle.down()
    turtle.lt(135)
    turtle.fd(20*(2**(0.5)))
    turtle.rt(135)
    turtle.fd(40)
    turtle.up()

def two(x, y):
    turtle.goto(x,y)
    turtle.down()
    turtle.fd(20)
    turtle.rt(90)
    turtle.fd(20)
    turtle.rt(45)
    turtle.fd(20*(2**(0.5)))
    turtle.lt(135)
    turtle.fd(20)
    turtle.up()

def three(x, y):
    turtle.goto(x,y)
    turtle.down()
    turtle.fd(20)
    turtle.rt(135)
    turtle.fd(20*(2**(0.5)))
    turtle.lt(135)
    turtle.fd(20)
    turtle.rt(135)
    turtle.fd(20*(2**(0.5)))
    turtle.up()
    
def four(x, y):
    turtle.goto(x,y)
    turtle.down()
    turtle.rt(90)
    turtle.fd(20)
    turtle.lt(90)
    turtle.fd(20)
    turtle.rt(90)
    turtle.fd(20)
    turtle.lt(180)
    turtle.fd(40)
    turtle.up()

def five(x, y):
    turtle.goto(x,y)
    turtle.fd(20)
    turtle.lt(180)
    turtle.down()
    turtle.fd(20)
    turtle.lt(90)
    turtle.fd(20)
    turtle.lt(90)
    turtle.fd(20)
    turtle.rt(90)
    turtle.fd(20)
    turtle.rt(90)
    turtle.fd(20)
    turtle.up()

def six(x, y):
    turtle.goto(x,y)
    turtle.fd(20)
    turtle.rt(135)
    turtle.down()
    turtle.fd(20*(2**(0.5)))
    turtle.lt(45)
    turtle.fd(20)
    turtle.lt(90)
    turtle.fd(20)
    turtle.lt(90)
    turtle.fd(20)
    turtle.lt(90)
    turtle.fd(20)
    turtle.up()

def seven(x, y):
    turtle.shape('turtle')
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.fd(20)
    turtle.rt(135)
    turtle.fd(20*(2**(0.5)))
    turtle.lt(45)
    turtle.fd(20)
    turtle.up()

def eight(x, y):
    turtle.goto(x,y)
    turtle.rt(90)
    turtle.fd(20)
    turtle.down()
    turtle.lt(90)
    turtle.fd(20)
    turtle.rt(90)
    turtle.fd(20)
    turtle.rt(90)
    turtle.fd(20)
    turtle.rt(90)
    turtle.fd(40)
    turtle.rt(90)
    turtle.fd(20)
    turtle.rt(90)
    turtle.fd(20)
    turtle.up()

def nine(x, y):
    turtle.goto(x,y)
    turtle.rt(90)
    turtle.fd(40)
    turtle.down()
    turtle.left(135)
    turtle.fd(20*(2**(0.5)))
    turtle.lt(45)
    turtle.fd(20)
    turtle.lt(90)
    turtle.fd(20)
    turtle.lt(90)
    turtle.fd(20)
    turtle.lt(90)
    turtle.fd(20)
    turtle.up()

def draw(a):
    if num == 0:
        print(zero(x, y))
    if num == 1:
        print(one(x, y))
    if num == 2:
        print(two(x, y))
    if num == 3:
        print(three(x, y))
    if num == 4:
        print(four(x, y))
    if num == 5:
        print(five(x, y))
    if num == 6:
        print(six(x, y))
    if num == 7:
        print(seven(x, y))
    if num == 8:
        print(eight(x, y))
    if num == 9:
        print(nine(x, y))


index = str(input())
numbers =[]

for i in index:
    numbers.append(int(i))

num = 0
a = 0
n = 6
x = -120
y = 20

if len(numbers)!=6:
    print("Не индекс! Должно быть 6 цифр, а не " +str(len(numbers))+ "!")
else:
    while n!=0:
        num = numbers[a] 
        print(draw(a))
        turtle.home()
        x+=30
        a+=1
        n-=1

