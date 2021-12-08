"""Guess a number within a range.

Exercises

1. Change the range to be from 0 to 1,000,000.
2. Can you still guess the number?
3. Print the number of guesses made.
4. Limit the number of guesses to the minimum required.

"""

from random import randint              #rnadom모듈 선언
from tkinter import *
import threading

"======================설정==========================="

root = Tk()                     #tkinter모듈을 불러옴
root.title("Guess")             #게임의 타이틀을 설정
root.geometry("465x380")        #게임화면의 크기를 저장 

"====================전역변수=========================="

TIME = 60                       #게임플레이 시간을 저장하는 변수
board = StringVar()             #상황판에 들어갈 내용을 저장하는 변수
password = IntVar()             #정답을 저장하는 변수
correct_count = IntVar()        #정답을 맞춘 횟수를 저장하는 변수
wrong_count = IntVar()          #정답을 틀린 횟수를 저장하는 변수
timer_value = IntVar()          #타이머에 들어갈 시간을 저장하는 변수
game_condition = BooleanVar()   #게임의 상태를 저장하는 변수

"==================Getter Setter======================"

def getStartNumber():
    Start=inputStart.get("1.0","end")
    return Start

def getEndNumber():
    End=inputEnd.get("1.0","end")
    return End

def getValue():
    value = int(inputAnswer.get("1.0","end"))
    return value

def setStartNumber(start):
    inputStart.delete("1.0","end")
    inputStart.insert("1.0",start)

def setEndNumber(end):
    inputEnd.delete("1.0","end")
    inputEnd.insert("1.0",end)

def setValue(value):
    inputAnswer.delete("1.0","end")
    inputAnswer.insert("1.0",value)

"===================버튼 이벤트========================"

def startButton(): #게임 시작 버튼 입력시 이벤트를 발생할 메소드
    try:
        StartNumber=getStartNumber()
        EndNumber=getEndNumber()

        if int(StartNumber) < int(EndNumber):
            output=("첫번째 숫자: " + str(StartNumber) +
            "마지막 숫자: " + str(EndNumber))
        else:
            output="시작번호와 마지막 번호에 정확한 숫자를 입력해주세요 \n"
            setScreen(output)
            return
        
        reset()
        setScreen(output)
        timer()
    except:
        setScreen("시작오류 \n")
        gameDone()

def valueButton(): # 값 입력 버튼 이벤트 구현 메소드
    try:
        if(not game_condition.get()):
            gameDone()

        guess = password.get()
        value = getValue()        

        if(not valueRangeTest()):
            output="범위 내 숫자를 입력해주세요 \n"
        elif guess > value:                  
            output="입력하신 숫자보다 높습니다. \n"
            wrong()
        elif guess < value:                 
            output="입력하신 숫자보다 낮습니다. \n"  
            wrong()
        elif guess == value:
            output="입력하신 숫자입니다. \n" 
            output+="틀린 횟수는 총 " + str(wrong_count.get()) + "입니다. \n"
            setScreen(output)
            correct()
            return
             
        setScreen(output)
    except:
        setScreen("답안입력오류 \n")
        gameDone()

"=====================타이머=========================="

def timer(): # 타이머 메소드
    if(game_condition.get()):
        threading.Timer(1,timerThread).start()

def timerThread(): # 타이머 쓰레드
    try:
        timer_value.set(timer_value.get() - 1)
        if(timer_value.get() == 0):
            game_condition.set(False)
            timeOutFail()
        timer()
    except:
        setScreen("타이머오류 \n")
        gameDone()

def timeOutFail(): # 시간초과 메소드
    output = "시간이 다 되었습니다. 맞춘 문제의 수는 "
    output += str(correct_count.get())
    output += " 개 입니다.\n"
    setScreen(output)
    gameDone()

"=====================초기화=========================="

def setPassword(): #정답 초기화 메소드
    first = int(getStartNumber())
    last = int(getEndNumber())
    password.set(randint(first,last))

def reset(): #게임 초기화 메소드
    setPassword()
    board.set("")    
    correct_count.set(0)
    wrong_count.set(0)
    timer_value.set(TIME)
    game_condition.set(True)
    
"===================기타 메소드========================"

def gameDone(): # 게임 종료 메소드
    output = "게임을 다시 시작하려면 시작번호와 끝번호를 입력한 후 시작버튼을 눌러주세요 \n"
    setScreen(output)
    game_condition.set(False)

def setScreen(message): # 보드 내용 갱신 메소드
    board.set(message + board.get())

def correct(): # 정답 메소드
    correct_count.set(correct_count.get() + 1)
    output = "현재까지 맞춘 정답의 갯수: " + str(correct_count.get())
    setScreen(output)
    wrong_count.set(0)
    setPassword()    

def wrong(): # 오답 메소드
    wrong_count.set(wrong_count.get() + 1)

def valueRangeTest(): # 입력받은 값이 범위 내에 있는지 테스하는 메소드    
    start = int(getStartNumber())
    end = int(getEndNumber())
    value = int(getValue())
    
    if(start <= value and value <= end):
        return TRUE
    return FALSE

"=======================GUI==========================="

"======================타이머=========================="
labelTimer=Label(root, textvariable=timer_value)

labelTimer.grid(row=0,column=0,columnspan=3)

"=====================시작번호========================="
labelStart=Label(root, text="시작번호")
inputStart=Text(root, height=1, width=45)
buttonStart=Button(root, height=2, width=10, text="시작", 
                    command=startButton)

labelStart.grid(row=1,column=0)
inputStart.grid(row=1,column=1)
buttonStart.grid(row=1,column=2,rowspan=2)

"====================마지막번호========================"
labelEnd=Label(root, text="마지막번호")
inputEnd=Text(root, height=1, width=45)

labelEnd.grid(row=2,column=0)
inputEnd.grid(row=2,column=1)

"========================답============================"
labelAnswer=Label(root, text="답")
inputAnswer=Text(root, height=1, width=45)
buttonAnswer=Button(root, height=1, width=10, text="입력", 
                    command=valueButton)
                    
labelAnswer.grid(row=3,column=0)
inputAnswer.grid(row=3,column=1)
buttonAnswer.grid(row=3,column=2)

"======================출력창=========================="
labelPrint=Label(root, textvariable=board)
labelPrint.grid(row=4,column=0,columnspan=3)

root.mainloop()