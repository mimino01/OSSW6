"""Pacman, classic arcade game.

Exercises

1. Change the board.
2. Change the number of ghosts.
3. Change where pacman starts.
4. Make the ghosts faster/slower.
5. Make the ghosts smarter.

"""

from random import choice
from turtle import *
from freegames import floor, vector

state = {'score': 0} # 점수를 나타내는 변수 선언
path = Turtle(visible=False) # Turtle 객체 생성
writer = Turtle(visible=False) # Turtle 객체 생성
aim = vector(5, 0) # 이동 속도와 방향을 정해주는 벡터
pacman = vector(-40, -80) # pacman 위치를 정해주는 벡터
ghosts = [ # 귀신의 위치, 이동 속도와 방향을 정해주는 배열
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]
tiles = [ # 맵의 정보를 담은 배열
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

# x, y에서 20 x 20 크기의 채운 사각형을 그린다.
def square(x, y):
    "Draw square using path at (x, y)."
    path.up() # 거북이가 이동시에 선을 그리지 않음
    path.goto(x, y) # 거북이를 x, y로 이동
    path.down() # 거북이가 이동시에 선을 그림
    path.begin_fill() # 거북이가 그릴 도형을 채운다

    for count in range(4): # 4번동안
        path.forward(20) # 거북이를 20만큼 이동
        path.left(90) # 거북이를 왼쪽으로 90도 회전

    path.end_fill() # 거북이가 그릴 도형을 채우지 않는다

# tiles에서의 point의 위치를 알려준다.
def offset(point):
    "Return offset of point in tiles."
    x = (floor(point.x, 20) + 200) / 20 # floor(point.x, 20) + 200를 20으로 나눈 값을 x에 저장한다
    y = (180 - floor(point.y, 20)) / 20 # 180 - floor(point.y, 20)를 20으로 나눈 값을 y에 저장한다
    index = int(x + y * 20) # x + y *20을 정수로 index에 저장한다
    return index # index를 반환한다

# tiles에서 point가 유효한지 알려준다.
def valid(point):
    "Return True if point is valid in tiles."
    index = offset(point) # 

    if tiles[index] == 0: # tiles[index]가 0이면
        return False # 유효하지 않음

    index = offset(point + 19) # offset(point+19)를 index에 저장

    if tiles[index] == 0: # tiles[index]가 0이면
        return False # 유효하지 않음

    # point.x와 point.y가 20의 배수가 아니면 유효하지 않음
    return point.x % 20 == 0 or point.y % 20 == 0 

# 맵을 그려준다.
def world():
    "Draw world using path."
    bgcolor('black') # 배경색을 검정으로 만든다
    path.color('blue') # path의 색을 파랑으로 만든다.

    for index in range(len(tiles)): # tiles의 길이 동안
        tile = tiles[index] # tile은 tiles[index]

        if tile > 0: # tile이 0보다 크면
            x = (index % 20) * 20 - 200 # x에 index%20 * 20 -200을 저장한다
            y = 180 - (index // 20) * 20
            square(x, y) # x, y에 사각형을 그린다

            if tile == 1: # tile이 1이면
                path.up() # 거북이가 이동시에 그림을 그리지 않음
                path.goto(x + 10, y + 10) # 거북이를 x+10, y+10로 이동
                path.dot(2, 'white') # 지름이 2인 하얀색 점을 그린다

# pacman과 ghosts를 이동시킨다.
def move():
    "Move pacman and all ghosts."
    writer.undo() # 이전 행동을 취소한다 
    writer.write(state['score']) # state['score']를 현재 거북이의 위치에 적는다

    clear() # 화면을 지운다

    if valid(pacman + aim): # pacman + aim이 유효하면
        pacman.move(aim) # pacman을 aim만큼 이동시킨다

    index = offset(pacman) # pacman의 위치를 가져와서 index에 저장

    if tiles[index] == 1: # tiles[index]가 1이면
        tiles[index] = 2 # tiles[index]에 2를 저장한다
        state['score'] += 1 # state['score']에 1을 추가한다
        x = (index % 20) * 20 - 200 # 
        y = 180 - (index // 20) * 20 #
        square(x, y) # x, y에 사각형을 그린다

    up() # 거북이가 이동시에 그림을 그리지 않음
    goto(pacman.x + 10, pacman.y + 10) # 거북이를 pacman.x+10, pacman.y+10으로 이동
    dot(20, 'yellow') # 지름이 20이고 노란색인 점을 찍는다

    for point, course in ghosts: # 모든 ghost의 요소에 대하여
        if valid(point + course): # point+course가 유효하다면
            point.move(course) # course만큼 point를 이동
        else: # point+course가 유효하지 않다면
            options = [ # 모든 이동방향과 속도를 배열에 저장
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
            ]
            plan = choice(options) # options중 임의로 하나만 선택하여 plan에 저장
            course.x = plan.x # course.x을 plan.x로 바꿈
            course.y = plan.y # course.y을 plan.y로 바꿈

        up() # 거북이가 이동시에 그림을 그리지 않음
        goto(point.x + 10, point.y + 10) # 거북이를 point.x+10, point.y+10으로 이동
        dot(20, 'red') # 지름이 20이고 빨강색인 점을 찍는다

    update() # screen update

#게임 종료 코드  추가

    if 1 not in tiles :
        print('You Won!')
        return

   
    for point, course in ghosts: # 모든 ghost의 요소에 대하여
        if abs(pacman - point) < 20: # pacman - point의 절대값이 20보다 작다면
            color("white")
            write('Game Over', move = False,  font=('Courier', 30, 'normal'))
            return # 종료

    ontimer(move, 100) # 0.1초 마다 move를 부른다

# x, y가 유효하다면 aim을 바꾼다
def change(x, y):
    "Change pacman aim if valid."
    if valid(pacman + vector(x, y)): # pacman+vector(x, y)가 유효하다면
        aim.x = x # aim.x를 x로 바꾼다
        aim.y = y # aim.y를 y로 바꾼다


setup(420, 420, 370, 0) # 크기가 420 x 420인 프레임을 370, 0에 생성한다
hideturtle() # 거북이를 숨긴다
tracer(False) # 거북이 애니메이션을 종료한다
writer.goto(160, 160) # 거북이를 160, 160으로 이동
writer.color('white') # 색을 하얀색으로 설정
writer.write(state['score']) # state['score']를 출력한다
listen() # 키 입력모드를 실행시킨다
onkey(lambda: change(5, 0), 'Right') # 오른쪽 화살표를 눌렀을 때 change(5, 0)을 부른다
onkey(lambda: change(-5, 0), 'Left') # 왼쪽 화살표를 눌렀을 때 change(-5, 0)을 부른다
onkey(lambda: change(0, 5), 'Up') # 위쪽 화살표를 눌렀을 때 change(0, 5)을 부른다
onkey(lambda: change(0, -5), 'Down') # 아래쪽 화살표를 눌렀을 때 change(0, -5)을 부른다
world() # 맵을 그린다
move() # 이동
done() # 메인루프
