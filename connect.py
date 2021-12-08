from turtle import *
from freegames import line
import turtle

class State:                                                                                #각 위치의 상태를 입력할 그리드를 설정하는 클래스
  def __init__(self):                                                                       #그리드 상태 초기화
    self.player = 'yellow'                                                                  #player의 초기 설정 값은 yellow
    self.slots = [0] * 8                                                                    #각 8칸의 빈칸의 명칭 slots으로 설정
    self.grid = [[None,None,None,None,None,None,None,None], 
                 [None,None,None,None,None,None,None,None],
                 [None,None,None,None,None,None,None,None],
                 [None,None,None,None,None,None,None,None],
                 [None,None,None,None,None,None,None,None],
                 [None,None,None,None,None,None,None,None],
                 [None,None,None,None,None,None,None,None],
                 [None,None,None,None,None,None,None,None]]

def next_cell(cell, offset):                                                                #다음 칸의 정보를 반환하는 함수
  return [cell[0] + offset[0], cell[1] + offset[1]]

def is_in_grid(grid_height, grid_width, cell):                                              #각 셀이 그리드 내에 위치하는지 확인하는 함수
  return (cell[0] >= 0 and cell[0] < grid_height and cell[1] >= 0 and cell[1] < grid_width)
          
def count_diagonal(grid, last_played_cell, offset1, offset2):                               #대각선의 셀 수를 세는 함수
  cell = last_played_cell                                                                   #마지막에 놓인 셀을 선택
  grid_height = len(grid)                                                                   #그리드 높이 설정
  grid_width = len(grid[0])                                                                 #그리드 너비 설정
  count = 1                                                                                 #카운트 1로 초기화
  
  while is_in_grid(grid_height, grid_width, next_cell(cell, [offset1[0], offset1[1]])):     #현재 셀의 대각선 셀의 위치가 그리드 내부에
    count += 1                                                                              #있다면 count 1 증가
    cell = next_cell(cell, [offset1[0], offset1[1]])                                        #다음 대각선 셀의 위치 확인하기 위한 값 변경
  cell = last_played_cell                                                                   #현재 셀의 위치를 다시 마지막에 놓인 셀로 변경
  
  while is_in_grid(grid_height, grid_width, next_cell(cell, [offset2[0], offset2[1]])):     #현재 셀의 대각선 셀의 위치가 그리드 내부에
    count += 1                                                                              #있다면 count 1 증가
    cell = next_cell(cell, [offset2[0], offset2[1]])                                        #다음 대각선 셀의 위치 확인하기 위한 값 변경
    
  return count  

def is_horizontal_win(grid, player, last_played_cell, win_score):                           #수평 승리조건 확인
    score = 0
    for cell in grid[last_played_cell[0]]:                                                  #마지막에 놓인 셀의 행에서
      if cell == player:                                                                    #셀의 색상과 현재 플레이어의 색상과 같다면
        score += 1                                                                          #score 1 증가
        if score >= win_score:                                                              #승리 점수 만족시
          return True                                                                       #True 반환
      else:                                                                                 #아니라면
        score = 0                                                                           
    return False                                                                            #False를 반환한다.
    
def is_vertical_win(grid, player, last_played_cell, win_score):                             #수직 승리조건 확인
    score = 0
    for row in range(0, len(grid)):                                                         #그리드 내의 row에서
      if grid[row][last_played_cell[1]] == player:                                          #마지막에 놓인 셀과 같은 색상의 연속된 셀이
        score += 1                                                                          #있다면 score 1 증가
        if score >= win_score:                                                              #승리 점수 만족시
          return True                                                                       #True 반환
      else:                                                                                 #아니라면
        score = 0                                                                           
    return False                                                                            #False를 반환한다.
    
def is_diagonal_win(grid, player, last_played_cell, win_score, offset1, offset2):           #대각선에서 승리조건을 만족하는지 확인하는 함수
  if count_diagonal(grid, last_played_cell, offset1, offset2) < win_score:                  #대각선에서 승리조건을 만족하지 못하면 
    return False                                                                            #False 반환
  
  cell = last_played_cell                                                                   #현재 셀의 위치를 다시 마지막에 놓인 셀로 변경
  while is_in_grid(len(grid), len(grid[0]), next_cell(cell, offset1)):                      #마지막에 선택된 셀의 대각선 셀이 그리드 내에
    cell = next_cell(cell, offset1)                                                         #위치하고 있다면 현재 셀 정보 변경
  
  score = 0
  for i in range(0, count_diagonal(grid, last_played_cell, offset1, offset2)):              #대각선 셀들에서
    if grid[cell[0]][cell[1]] == player:                                                    #현재 플레이어의 색상과 같은 색상인
      score += 1                                                                            #연속된 셀이 있다면 score 1 증가
      if score >= win_score:                                                                #승리조건 만족시
        return True                                                                         #True 반환
    else:                                                                                   #아니라면
      score = 0                                                                             #score 초기화 후
    cell = next_cell(cell, offset2)                                                         #셀 정보 변경한 후
  return False                                                                              #False 반환
    
def is_win(grid, player, last_played_cell, win_score):                                      #승리 조건 만족 여부 및 승리 플레이어 확인
  if is_horizontal_win(grid, player, last_played_cell, win_score):                          #수평 승리조건 만족시
    return True                                                                             #True 반환
  if is_vertical_win(grid, player, last_played_cell, win_score):                            #수직 승리조건 만족시
    return True                                                                             #True 반환
  if is_diagonal_win(grid, player, last_played_cell, win_score, [-1, -1], [1, 1]):          #내림차순 대각선 승리조건 만족시
    return True                                                                             #True 반환
  else:                                                                                     #그 외는
    return is_diagonal_win(grid, player, last_played_cell, win_score, [-1, 1], [1, -1])     #오름차순 대각선 승리조건 만족

turns = {'red': 'yellow', 'yellow': 'red'}                                                  #턴 딕셔너리 정의
state = State()                                                                             #그리드 상태 설정

def grid():                                                                                 #그리드 설정
    "Draw Connect Four grid."   
    bgcolor('light blue')                                                                   #배경 색 설정

    for x in range(-150, 250, 50):                                                          #세로선 표시
        line(x, -200, x, 200)

    for x in range(-175, 200, 50):                                                          #x값의 범위에서
        for y in range(-175, 200, 50):                                                      #y값의 범위일 때
            up()
            goto(x, y)                                                                      #각각의 위치에
            dot(40, 'white')                                                                #반지름 40, 흰색 점 생성

    update()

def show_winner(winner):                                                                    #게임 종료시 승리 메시지를 보여주는 함수
    mypen = turtle.Turtle()                                 
    mypen.hideturtle()
    mypen.undo()
    mypen.penup()
    mypen.hideturtle()
    mypen.setposition(0, 200)
    winnerstring = "승자는 %s!" % winner
    mypen.write(winnerstring, False, align="center", font=("Arial", 30, "normal"))
    mypen.setposition(0, -240)
    mypen.write("good game :)", False, align="center", font=("Arial", 30, "normal"))


    
def tap(x, y):                                                                              #클릭된 위치 정보 
    "Draw red or yellow circle in tapped row."
    player = state.player
    slots = state.slots
    grid = state.grid

    slot = int((x + 200) // 50)                                                             #클릭된 위치의 슬롯 정보
    count = slots[slot]                                                                     #클릭된 위치의 슬롯에 선택된 개수
    if count >= len(grid):                                                                  #클릭된 위치의 슬롯에 선택된 개수가 그리드의
      print ("No more space, try another slot")                                             #길이를 넘으면 오류 메시지 출력
      return

    x = ((x + 200) // 50) * 50 - 200 + 25
    y = count * 50 - 200 + 25

    up()
    goto(x, y)
    dot(40, player)
    update()

    grid[len(grid) - count - 1][slot] = player                                              #플레이어의 셀의 정보
    last_played_cell = [len(grid) - count - 1, slot]                                        #마지막 선택된 셀의 위치 정보
    if is_win(grid, player, last_played_cell, 4):                                           #한 플레이어가 4개의 연속된 점을 완성하면
      show_winner(player)                                                                   #승리 메시지 출력
      restart()                                                                             #재시작
    slots[slot] = count + 1                                                                 #선택된 슬롯 수 1 증가
    state.player = turns[player]                                                            #플레이어 변경

def restart():                                                                              #재시작하는 함수
  reset()
  hideturtle()
  grid()                                                                                    #그리드 화면 다시 불러오기
  state.__init__()                                                                          #그리드 상태 초기화
  onscreenclick(tap)
  done()

setup(420, 520, 300, 0)                                                                     #창 정보 셋팅
hideturtle()                                                                                #거북이 숨기기
tracer(False)                                                                               #거북이 애니메이션을 끈다.
grid()                                                                                      #그리드 함수 실행
onscreenclick(tap)                                                                          #클릭된 위치 정보 받기
done()
