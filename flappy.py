"""Flappy, game inspired by Flappy Bird.

Exercises

1. Keep score.
2. Vary the speed.
3. Vary the size of the balls.
4. Allow the bird to move forward and back.

"""

from random import *                            #random 모듈 선언
from turtle import *
from typing import Counter                            #turtle 모듈 선언

from freegames import vector
from freegames import path


bird = vector(0, 0)                             #새의 위치를 저장하는 변수
balls = []                                      #공의 정보를 저장하는 변수
ball_speed = 0
bird_speed = 0

ball_speed = randint(3,6)
bird_speed = randint(2,4)

register_shape("bird1.gif")
register_shape("bg.gif")

bird_image = Turtle()
bird_image.shape("bird1.gif")
bird_image.penup()

bg = Screen()
bg.bgpic("bg.gif")
bg.tracer(False)

score = Turtle()
score.penup()
score.hideturtle()

global count
count = 0

print("Brid speed is ",bird_speed,", Ball speed is ",ball_speed)

def tap(x, y):                                  #특정값 입력시 일어나는 이벤트를 구현한 메소드
    "Move bird up in response to screen tap."
    up = vector(0, 30)
    bird.move(up)

def retap(x,y):
    "Move bird down in response to screen tap."
    down = vector(0, -30)
    bird.move(down)

def Printscore(x):
    score.goto(-189,169)
    s = "score: " + str(x)
    score.color("black")
    score.write(s, align='left', font=('Arial', 22, 'bold'))

def Clearscore():
    score.clear()

def inside(point):                              #매개변수의 좌표가 화면 안에 있는지 판별하는 메소드
    "Return True if point on screen."
    return -200 < point.x < 200 and -160 < point.y < 160


def draw(alive):                                #매개변수 값에 따라 색을 조정하는 메소드
    "Draw screen objects."    
    clear()

    bird_image.goto(bird.x,bird.y)

    for ball in balls:                          #공은 검은색
        goto(ball.x, ball.y)
        dot(20, 'yellow')

    update()


def move():                                     #새와 공의 움직임을 계산하고 출력하는 메소드
    "Update object positions."
    global count
    Clearscore()

    bird.y -= bird_speed                                 #새의 위치를 move가 호출될때마다 y축 기준 -5만큼 이동

    for ball in balls:                          #공의 위치를 move가 호출될때마다 x축 기준 -3만큼 이동
        ball.x -= ball_speed

    if randrange(10) == 0:                      #move메소드가 호출되면 10%확율로 공이 생성됨
        y = randrange(-159, 159)
        ball = vector(199, y)
        balls.append(ball)

    while len(balls) > 0 and not inside(balls[0]): #공이 맵 밖으로 나가면 삭제시킴
        balls.pop(0)
        count += 1

    if not inside(bird):                        #새가 맵 밖으로 나가면 중지시킴
        draw(False)
        return

    for ball in balls:                          #공이 새와 붙으면 게임을 중지시킴
        if abs(ball - bird) < 25:
            draw(False)
            return

    draw(True)
    Printscore(count)
    ontimer(move, 50)                           #move메소드를 반복


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
du = randint(1,3)
onscreenclick(tap)
move()
done()
