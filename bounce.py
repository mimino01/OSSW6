from random import *
from turtle import *
from freegames import vector
from freegames.utils import square

def value():                                                #값을 랜덤하게 생성
    "Randomly generate value between (-5, -3) or (3, 5)."
    return (3 + random() * 2) * choice([1, -1])


ball = vector(0, 0)                                         #ball의 벡터값 설정
aim = vector(value(), value())                              #움직일 방향의 벡터값 랜덤하게 설정
state = {1: 0}


def move(player, change):                                   #움직임
    "Move player position by change."
    state[player] += change

def rectangle(x, y, width, height):
    "Draw rectangle at (x, y) with given width and height."
    up()
    goto(x, y)
    down()
    begin_fill()
    for count in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

def border(x,y,size):
    up()
    goto(x,y)
    down()
    begin_fill
    for count in range(4):
        forward(size)
        left(90)

def draw():                                                 #볼의 움직임 설정
    "Move ball and draw game."
    clear()                                                 #초기화
    border(-205,-200,405)
    rectangle(state[1], -200, 50, 10)

    ball.move(aim)                                          #볼을 aim에 따라 이동시킨다.

    x = ball.x                                              #x는 볼의 x
    y = ball.y                                              #y는 볼의 

    up()
    goto(x, y)
    dot(10)
    update()


    if x < -200 or x > 200:                                 #x 값이 범위를 벗어날 경우
        aim.x = -aim.x                                      #-적용하여 다시 저장

    if y > 200:
        aim.y = -aim.y

    if y < -200:                                            #y값이 범위를 벗어날 경우
        low = state[1]
        high = state[1] + 50

        if low <= x <= high:
            aim.y = -aim.y
        else:
            return 

    ontimer(draw, 50)                                       #0.05초 후에 draw실행


setup(420, 420, 370, 0)                                     #창 정보 셋팅
hideturtle()                                                #거북이 숨기기
tracer(False)                                               #거북이 애니메이션을 끈다.
listen()
onkey(lambda: move(1, -20), 'Left')
onkey(lambda: move(1, 20), 'Right')
draw()                                                      #draw() 실행
done()
