"""Fidget, inspired by fidget spinners.

Exercises

1. Change the spinner pattern.
2. Respond to mouse clicks.
3. Change its acceleration.
4. Make it go forwards and backwards.

"""

from turtle import *                #turtle모듈 선언

state = {'turn': 0}                 #스피너의 각도를 저장할 변수 선언
score = 0


def spinner():                      #스피너를 출력하는 메소드
    "Draw fidget spinner."
    clear()
    angle = state['turn'] / 10
    setScore(angle)
    setBackground(angle)
    setposition(0,0)
    pendown()
    right(angle)
    forward(100)
    dot(120, 'red')
    back(100)
    right(120)
    forward(100)
    dot(120, 'green')
    back(100)
    right(120)
    forward(100)
    dot(120, 'blue')
    back(100)
    right(120)
    update()


def animate():                      #스피너의 움직임을 출력하는 메소드
    "Animate fidget spinner."
    if state['turn'] > 0:
        state['turn'] -= 2          #animate메소드가 한번 호출될 때 줄어든 속도

    spinner()
    ontimer(animate, 40)


def flick():                        #특정값 입력시 회전속도를 올려주는 메소드
    "Flick fidget spinner."
    state['turn'] += 10             #특정값 입력시 올라가는 속도


def setScore(score):
    undo()
    penup()
    hideturtle()
    setposition(100,180)
    scorestring = "Speed: %s" %score
    write(scorestring, False, align="left", font=("바탕", 10))


def setBackground(score):
    temp = (score)%3
    if(temp == 1):
        bgcolor("yellow")
    elif(temp == 2):
        bgcolor("orange")
    elif(temp == 0):
        bgcolor("white")


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(20)
onkey(flick, 'space')
listen()
animate()
done()
