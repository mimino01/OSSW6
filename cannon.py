from random import randrange
from turtle import *
import turtle

from freegames import vector

ball = vector(-200, -200)                                                       #ball의 벡터값 설정
speed = vector(0, 0)                                                            #속도 벡터값 설정
targets = []                                                                    #targers 리스트 생성
score = []                                                                      #점수를 저장할 리스트 생성

def tap(x, y):                                                                  #클릭된 위치로 이동시키는 함수
    if not inside(ball):                                                        #볼의 위치가 범위를 벗어났을 경우
        ball.x = -199                                                           #볼의 x값 재설정
        ball.y = -199                                                           #볼의 y값 재설정
        speed.x = (x + 200) / 25                                                #x방향 이동속도 설정
        speed.y = (y + 200) / 25                                                #y방향 이동속도 설정


def inside(xy):                                                                 #화면 내부에 있을 경우 true반환
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():                                                                     #볼과 타겟의 위치 설정
    clear()                                                                     #초기화
    for target in targets:                                                      #리스트 내에서 for문 실행
        goto(target.x, target.y)                                                #위치로 타겟 이동
        dot(20, 'blue')                                                         #반지름 20, 파란색 점 생성

    if inside(ball):                                                            #볼이 화면 내부에 위치할 경우
        goto(ball.x, ball.y)                                                    #위치로 볼 이동
        dot(6, 'red')                                                           #반지름 6, 빨간색 점 생성
    
    update()

mypen = turtle.Turtle()
mypen.hideturtle()

def setScore(curr_score):                                                       #점수 출력
    mypen.undo()
    mypen.penup()
    mypen.hideturtle()
    mypen.setposition(-190, 180)
    scorestring = "Score: %s" % curr_score
    mypen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))  


def move():                                                                     #볼과 타겟의 움직임 설정
    if randrange(20) == 0:                                                      #랜덤하게 생성한 수가 0일 경우
        y = randrange(-150, 150)                                                #y값 랜덤 생성
        target = vector(200, y)                                                 #타겟의 위치는 x=200, y=위에서 랜덤하게 생성한 값
        targets.append(target)                                                  #리스트에 추가

    for target in targets:                                                      #리스트 내에서 for문 실행
        target.x -= 0.3                                                         #타겟의 x값 0.5씩 감소

    if inside(ball):                                                            #볼이 화면 내부에 위치해있을 경우
        speed.y -= 0.3                                                          #y 속도 0.35씩 감소
        ball.move(speed)                                                        #speed값대로 볼 이동

    dupe = targets.copy()                                                       #복사
    targets.clear()                                                             #초기화

    for target in dupe:                                                         #dupe내에서 for문 실행
        if abs(target - ball) > 13:                                             #절댓값이 13보다 크면
            targets.append(target)                                              #리스트에 추가
        else:
            score.append(target)                                                #타겟이 삭제되는 개수를 점수 리스트에 추가하고 
            setScore(len(score))                                                #점수 리스트의 길이를 점수로 설정


    draw()                                                                      #화면에 표시

    for target in targets:                                                      #리스트 내에서 for문 실행
        if not inside(target):                                                  #타겟이 화면 내에 없을 경우
            return                                                              #종료

    ontimer(move, 50)                                                           #0.05초 후에 move실행



setup(420, 420, 370, 0)                                                         #창 정보 셋팅  
hideturtle()                                                                    #거북이 숨기기  
up()                                                                            #펜을 올리고 움직일 때 그리지 않는다.
tracer(False)                                                                   #거북이 애니메이션을 끈다.
onscreenclick(tap)                                                              #클릭한 위치로 볼 이동
setScore(0)                                                     
move()                                                                          #move함수 실행
done()
