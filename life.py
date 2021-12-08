"""Game of Life simulation.

Conway's game of life is a classic cellular automation created in 1970 by John
Conway. https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

Exercises

1. Can you identify any Still Lifes, Oscillators, or Spaceships?
2. How can you make the simulation faster? Or bigger?
3. How would you modify the initial state?
4. Try changing the rules of life :)

"""

from random import choice       #random모듈 선언
from turtle import *            #turtle모듈 선언

from freegames import square

cells = {}                      #cell을 저장할 변수 선언


def initialize():               #게임판을 생성하는 메소드
    "Randomly initialize the cells."
    for x in range(-200, 200, 10):
        for y in range(-200, 200, 10):
            cells[x, y] = False

    for x in range(-50, 50, 10):
        for y in range(-50, 50, 10):
            cells[x, y] = choice([True, False])


def step():                     #다음 세대에서 일어날 일을 계산하는 메소드
    "Compute one step in the Game of Life."
    neighbors = {}              #이웃한 변수들의 정보를 저장할 변수 선언

    for x in range(-190, 190, 10):
        for y in range(-190, 190, 10):
            count = -cells[x, y]
            for h in [-10, 0, 10]:
                for v in [-10, 0, 10]:
                    count += cells[x + h, y + v]
            neighbors[x, y] = count

    for cell, count in neighbors.items():
        if cells[cell]:
            if count < 2 or count > 3:
                cells[cell] = False
        elif count == 3:
            cells[cell] = True


def draw():                                             #이미지를 그리는 메소드
    "Draw all the squares."
    step()                                              #step메소드를 불러옴
    clear()
    for (x, y), alive in cells.items():                 #변수값이 참이면 초록색 그렇지 않으면 검은색을 출력
        color = 'green' if alive else 'black'
        square(x, y, 10, color)
    update()
    ontimer(draw, 100)                                  #draw메소드를 반복


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
initialize()
draw()
done()
