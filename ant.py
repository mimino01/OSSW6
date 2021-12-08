from random import *
from turtle import *

from freegames import vector


ant = vector(0, 0)                                          #(0,0)에 개미를 위치시킨다.
aim = vector(2, 0)                                          #움직일 정보를 설정한다.

def wrap(value):
    return value 

def current_state():                                        #현재 상태가
    global moving
    moving = False                                          #움직이지 않고 있다면 False
    up()                                                    #그리지 않는다.

def next_state():                                           #다음 상태가
    global moving   
    down()
    moving = True                                           #움직이고 있다면
    draw()                                                  #그린다.

def space_bar():                                            #스페이스바로 움직임을 조종하기 위한 함수 
    global current_state, next_state
    next_state()
    current_state, next_state = next_state, current_state   #현재 상태와 다음 상태를 바꿔준다.

def draw():                                                 #개미를 이동시키는 함수
    "Move ant and draw screen."
    if moving :
        ant.move(aim)                                       #개미의 움직임을 선언한다.
        ant.x = wrap(ant.x)                                 #개미가 움직일 화면의 x값을 설정한다.
        ant.y = wrap(ant.y)                                 #개미가 움직일 화면의 y값을 설정한다.

        if ant.y < -200 or ant.y > 200:                     #벽에 부딪히면
            aim.y = -aim.y                                  #내부로 향해 그림을 그리도록 한다.

        if ant.x < -200 or ant.x > 200:                     #벽에 부딪히면
            aim.x = -aim.y                                  #내부로 향해 그림을 그리도록 한다.
        aim.move(random() - 0.5)                            #개미가 움직일 방향을 랜덤으로 설정한다.
        aim.rotate(random() * 10 - 5)                       #객체를 랜덤하게 회전시킨다.

        goto(ant.x, ant.y)                                  #개미를 각x, y값으로 이동시킨다.
        dot(4)                                              #반지름이 4인 점을 생성

        ontimer(draw, 100)                                  #0.1초 후에 draw함수 실행


setup(420, 420, 370, 0)                                     #창 정보 셋팅
hideturtle()                                                #거북이 숨기기
tracer(False)                                               #거북이 애니메이션을 끈다.
current_state()                                             #현재 상태를 멈춤으로 시작
onkey(space_bar, "space")                                   #스페이스바로 움직임 제어를 입력받는다.
listen()
done()
