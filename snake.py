import turtle as t
import random
import webbrowser

WIDTH = 600  
LENGTH = 600
SCORE = 0
TMP = 25
SNAKE = 3
OSNAKE = 1

SWITCH = False

t.register_shape("mouse.gif")
t.register_shape("snake1.gif")
t.register_shape("snake2.gif")

# 스크린 객체
s = t.Screen()
s.setup(WIDTH, LENGTH)
s.bgpic("forest.gif")
s.tracer(False)

# 뱀 객체
snake = t.Turtle()
snake.shape("snake1.gif")
snake.turtlesize(1.5)

# 상대뱀 객체
other_snake = t.Turtle()
other_snake.shape("snake2.gif")
other_snake.turtlesize(1.5)

def reset_mouse(mouse_list): # 쥐먹이 설정
    mouse_list[-1].shape("mouse.gif")
    mouse_list[-1].penup()
    mouse_list[-1].setposition(random.randint(WIDTH/2 -WIDTH + TMP, WIDTH/2 -TMP), random.randint(LENGTH/2 -LENGTH + TMP, LENGTH/2 - TMP)) 

def make_mouse(mouse_list):  # 쥐먹이 생성
        mouse_list.append(t.Turtle())
        reset_mouse(mouse_list)

mouse_list=[]  # 쥐먹이 객체
for i in range(8):
        make_mouse(mouse_list)

def reset_game(s, o):
    s.penup()
    o.penup()
    s.goto(0, int(LENGTH/2)-TMP)
    o.goto(0, int(LENGTH/2)-LENGTH + TMP)

def move_snake(): # 뱀 이동
    global SNAKE
    snake.forward(SNAKE)

def move_osnake(): #상대뱀 이동
    global OSNAKE
    other_snake.forward(OSNAKE)

def inside(ls):  # 객체가 화면 끝에 닿는지 여부 확인
    for i in ls: 
        i_pos = i.position()
        if i_pos[0] >= WIDTH/2-TMP:
            i.setx(i_pos[0]-10)
        elif i_pos[0] <= WIDTH/2 - WIDTH+TMP:
            i.setx(i_pos[0]+10)

        if i_pos[1] >= LENGTH/2-TMP:
            i.sety(i_pos[1]-10)
        elif i_pos[1] <= LENGTH/2 - LENGTH+TMP:
            i.sety(i_pos[1]+10)

def message(temp, mes, pos, font): # 문자 출력
    
    txt.clear()
        
    if temp == 'init':
        txt.home()
        txt.color("white")
        txt.write(mes, align=pos, font=font)
        
    else:
        txt.goto(WIDTH/2 -WIDTH + TMP, LENGTH/2 - TMP)
        txt.color("white")
        txt.write(mes, align=pos, font=font)

def contact(s_lst, m_lst):  # 접촉 상태 확인
    global OSNAKE, SNAKE, SCORE, SWITCH
    
    for osnake in s_lst:
        if osnake.distance(snake)< 25:
            message('init', f'점수: {SCORE}\nspace버튼을 연타하면 상대 뱀을 벗어날 수 있습니다.\n게임을 종료하시려면 Esc를 눌러주세요. '
            , pos='center', font=('Arial', 12, 'bold'))
            SWITCH = False

    for w in m_lst:
        if w.distance(snake) < 20:
            w.hideturtle()
            m_lst.remove(w)
            make_mouse(m_lst)
            reset_mouse(m_lst)
            SCORE += 1
            
            if SCORE % 5 == 0:
                OSNAKE += 1
                
                if OSNAKE >= 3:
                    SNAKE += 1
        
def play():  # 게임실행 부분

    global OSNAKE, SCORE
    if SWITCH:

        message('else', f'점수:{SCORE}  뱀단계:{OSNAKE}', 'left', ('Arial', 13, 'normal')) # 텍스트 출력
        s_pos = snake.position()
        inside([snake, other_snake])    
        move_snake()
        move_osnake()
        other_snake.setheading(other_snake.towards(s_pos)) # 상대뱀이 뱀을 향하도록 이동
        contact([other_snake], mouse_list) # 개체 충돌확인

        
        s.update() # 화면갱신
        s.ontimer(play, 20) #타이머 동작
        
    else:
        s.update()

#키입력
def up():
    snake.setheading(90)
def down():
    snake.setheading(270)
def left():
    snake.setheading(180)
def right():
    snake.setheading(0)
def space():
    global SWITCH
    txt.clear()
    if SWITCH == False:
        SWITCH = True
        play()

txt = t.Turtle()
txt.penup()
txt.hideturtle()
message('init', '게임시작을 시작하려면\nSPACE버튼을 눌러주세요.', 'center', ('Arial', 12, 'bold'))
reset_game(snake, other_snake)

s.onkeypress(up, 'Up')
s.onkeypress(down, 'Down')
s.onkeypress(left, 'Left')
s.onkeypress(right, 'Right')
s.onkeypress(space, 'space')
s.onkeypress(s.bye, 'Escape')

webbrowser.open("슬리피우드.mp3")
s.listen()
s.mainloop()

