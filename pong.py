"""Pong, classic arcade game.

Exercises

1. Change the colors.
2. What is the frame rate? Make it faster or slower.
3. Change the speed of the ball.
4. Change the size of the paddles.
5. Change how the ball bounces off walls.
6. How would you add a computer player?
6. Add a second ball.

"""

from random import choice, random # random 모듈에서 randrange 메소드 가져옴.
from turtle import *              # turtle 모듈에서 모든 메소드 가져옴.
from freegames import vector      # freegames 모듈에서 vector 가져옴.



def reset():
    global ball, aim, state
    ball = vector(0, 0)             # 공을 생성한다. 좌표는 정중앙이다.
    aim = vector(value(), value())  # 공이 움직일 목표지점을 생성한다. 좌표는 ↗(1사분면), ↖(2사분면), ↙, ↘ 4종류 중 하나
    state = {1: 0, 2: 0}            # player1의 시작 y좌표: 0, player2의 시작 y좌표: 0

def value():
    "Randomly generate value between (-5, -3) or (3, 5)."
    return (3 + random() * 2) * choice([1, -1])  # 처음 공이 움직이는 방향을 랜덤으로 설정한다. -5 ~ 5 중 하나.


def move(player, change):
    "Move player position by change."
    state[player] += change            # player의 위치를 바꿔준다. 86~89줄 코드에 따라, 위아래로 지정크기만큼 움직인다.

def rectangle(x, y, width, height): # player 네모 1개를 그린다.
    "Draw rectangle at (x, y) with given width and height."
    up()                   # 펜을 도화지에서 뗀다. 네모가 이동 시, 자취 선을 그리지 않는다.
    goto(x, y)             # 좌표(x,y)로 이동한다. player1은 초기 좌표(-200,0)에서 이동. plyaer2는 (190,0)에서 이동.
    down()                 # 이동이 끝났으면, 펜을 다시 도화지에 댄다.

    begin_fill()           # turtle 메소드. 사각형 내부에 색을 채워준다. begin_fill과 end_fill을 모두 써줘야 한다.
                           # begin_fill과 end_fill 사이엔 색을 채울 도형을 그려준다.
    for count in range(2): # 2회 반복: player 네모를 그린다. 1회:┌ 그림, 2회: ┘ 그림.
        forward(width)     # 펜을 width만큼 이동하며 그려준다.
        left(90)           # 왼쪽으로 90도 회전
        forward(height)    # 펜을 height만큼 이동하며 그려준다.
        left(90)           # 왼쪽으로 90도 회전

    end_fill()             # turtle 메소드. 사각형 내부에 색을 채워준다. begin_fill과 end_fill을 모두 써줘야 한다.

def draw():
    "Draw game and move pong ball."
    clear()                            # player와 공의 이동궤적을 지워준다. 주석처리하면 자취가 남는다.
    rectangle(-200, state[1], 10, 50)  # player1 네모를 그린다.
    rectangle(190, state[2], 10, 50)   # plyaer2 네모를 그린다.

    rectangle(-10, -210, 20, 110)      # 중앙 방어벽 아랫네모 추가
    rectangle(-10,  100, 20, 110)      # 중앙 방어벽 윗네모 추가

    ball.move(aim) # 공을 목표지점까지 움직인다.
    x = ball.x     # 공의 (x,y)좌표를 새롭게 갱신하여,
    y = ball.y

    up()
    goto(x, y)    # 공을 움직인다.
    dot(10)       # 공은 원 모양, 크기10으로 설정.
    update()

    if y < -200 or y > 200: # 공이 윗벽 또는 아랫벽에 닿을 시,
        aim.y = -aim.y      # 목표지점을 y축 대칭점으로 설정하여, 바닥에 튕기게 하는 효과를 내게 한다.

    if x < -185:              # 공의 x좌표가 -185보다 왼쪽일 때,
        low = state[1]        # player1 네모의 아래끝을 low,
        high = state[1] + 50  # player1 네모의 위끝을   high 라고 하자.

        if low <= y <= high:  # 공의 y좌표가 low ~ high 사이에 있다면 = 공이 player1 네모에 맞았다면,
            aim.x = -aim.x    # 목표지점을 x축 대칭점으로 설정하여, 공이 탁구채에 튕기게 하는 효과를 내게 한다.
        else:                 # player1이 공을 방어하지 못했다면,
            return            # 게임오버로 종료된다.

    if x > 185:               # 공의 x좌표가 185보다 오른쪽일 때, 위와 같다.
        low = state[2]
        high = state[2] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            return

    # 중앙 방어벽에 튕기는 효과
    if x > -15 and x < 15 and y > -210 and y < -100:
        aim.x = -aim.x    # 목표지점을 x축 대칭점으로 설정하여, 공이 벽에 튕기게 하는 효과를 내게 한다.
    if x > -15 and x < 15 and y > 100 and y < 210:
        aim.x = -aim.x    # 목표지점을 x축 대칭점으로 설정하여, 공이 벽에 튕기게 하는 효과를 내게 한다.
    if x > -15 and x < 15 and y == -100:
        aim.y = -aim.y      # 목표지점을 y축 대칭점으로 설정하여, 바닥에 튕기게 하는 효과를 내게 한다.
    if x > -15 and x < 15 and y == 100:
        aim.y = -aim.y      # 목표지점을 y축 대칭점으로 설정하여, 바닥에 튕기게 하는 효과를 내게 한다.
     

    ontimer(draw, 35)         # turtle 메소드. 50/1000초마다 그려준다. ontimer(메소드,시간)


def main():
    hideturtle()                     # 거북이를 숨긴다. 주석화하면 공에 검은거북이가 붙어서 출현한다.
    tracer(False)                    # 거북이 애니메이션을 종료한다.
    listen()                         # 이 명령어가 있어야만 키 입력모드가 실행되어, 입력된 키에 반응한다.
    reset()
    onkey(lambda: move(1, 20), 'w')  # 키보드 w를 누르면, player1은 위로 20만큼 이동
    onkey(lambda: move(1, -20), 's') # 키보드 s를 누르면, player1은 아래로 20만큼 이동
    onkey(lambda: move(2, 20), 'i')  # 키보드 i를 누르면, player2는 위로 20만큼 이동
    onkey(lambda: move(2, -20), 'k') # 키보드 k를 누르면, player2는 아래로 20만큼 이동
    draw()                           # 46줄의 draw()메소드 호출

    setup(420, 420, 370, 0)          # 화면의 크기/좌표를 지정한다. (가로길이, 세로길이, 시작 x좌표, 시작 y좌표)
main()
done()                           # 코드 종료 후 게임창이 바로 닫히지 않게 한다. 주석화하면 창이 열리자마자 바로 닫힌다.
