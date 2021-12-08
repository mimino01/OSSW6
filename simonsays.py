from random import choice
from time import sleep
from turtle import *
from freegames import floor, square, vector

buttons = {}
pattern = {}
guesses = {}
tiles = {}

buttons = []


def reset():
    global buttons, pattern, guesses, tiles
   
    pattern = []
    guesses = []
    tiles = {
        vector(0, 0): ('red', 'dark red'),
        vector(0, -200): ('blue', 'dark blue'),
        vector(-200, 0): ('green', 'dark green'),
        vector(-200, -200): ('yellow', 'khaki'),
    }

def grid():
    "Draw grid of tiles."
    square(0, 0, 200, 'dark red')
    square(0, -200, 200, 'dark blue')
    square(-200, 0, 200, 'dark green')
    square(-200, -200, 200, 'khaki')
    update()

def flash_easy(tile):
    "Flash tile in grid."
    glow, dark = tiles[tile]
    square(tile.x, tile.y, 200, glow)
    update()
    sleep(0.7)
    square(tile.x, tile.y, 200, dark)
    update()
    sleep(0.7)

def flash_normal(tile):
    "Flash tile in grid."
    glow, dark = tiles[tile]
    square(tile.x, tile.y, 200, glow)
    update()
    sleep(0.3)
    square(tile.x, tile.y, 200, dark)
    update()
    sleep(0.3)

def flash_hard(tile):
    "Flash tile in grid."
    glow, dark = tiles[tile]
    square(tile.x, tile.y, 200, glow)
    update()
    sleep(0.1)
    square(tile.x, tile.y, 200, dark)
    update()
    sleep(0.1)


def grow_easy():
    "Grow pattern and flash tiles."
    tile = choice(list(tiles))
    pattern.append(tile)

    for tile in pattern:
        flash_easy(tile)

    print('Pattern length:', len(pattern))
    guesses.clear()

def grow_normal():
    "Grow pattern and flash tiles."
    tile = choice(list(tiles))
    pattern.append(tile)

    for tile in pattern:
        try:
            flash_normal(tile)
        except Exception:
            pass

    print('Pattern length:', len(pattern))
    guesses.clear()


def grow_hard():
    "Grow pattern and flash tiles."
    tile = choice(list(tiles))
    pattern.append(tile)

    for tile in pattern:
        flash_hard(tile)

    print('Pattern length:', len(pattern))
    guesses.clear()
  


def tap_easy(x, y):
    "Respond to screen tap."
    onscreenclick(None)
    x = floor(x, 200)
    y = floor(y, 200)
    tile = vector(x, y)
    index = len(guesses)

    if tile != pattern[index]:
        color("black")
        goto(0,0)
        write('Game Over', move = False, align='center', font=('Arial', 35, 'italic'))
        print("총 맞춘횟수",len(pattern)-1)
        return

    guesses.append(tile)
    flash_easy(tile)

    if len(guesses) == len(pattern):
        grow_easy()

    onscreenclick(tap_easy)

def tap_normal(x, y):
    "Respond to screen tap."
    onscreenclick(None)
    x = floor(x, 200)
    y = floor(y, 200)
    tile = vector(x, y)
    index = len(guesses)

    if tile != pattern[index]:
        color("black")
        goto(0,0)
        write('Game Over', move = False, align='center', font=('Arial', 30, 'italic'))
        print("총 맞춘횟수",len(pattern)-1)
        return

    guesses.append(tile)
    flash_normal(tile)

    if len(guesses) == len(pattern):
        grow_normal()

    try:
        onscreenclick(tap_normal)
    except Exception:
        pass

def tap_hard(x, y):
    "Respond to screen tap."
    onscreenclick(None)
    x = floor(x, 200)
    y = floor(y, 200)
    tile = vector(x, y)
    index = len(guesses)

    if tile != pattern[index]:
        color("black")
        goto(0,0)
        write('Game Over', move = False, align='center', font=('Arial', 35, 'italic'))
        print("총 맞춘횟수",len(pattern)-1)
        return
        
        #3초후 재시작
        #sleep(3)
        #setup_game()
     
        
        
      

    guesses.append(tile)
    flash_hard(tile)

    if len(guesses) == len(pattern):
        grow_hard()

    onscreenclick(tap_hard)

def start_easy(x, y):
    "Start game."
    grow_easy()
    try:
        onscreenclick(tap_easy)
    except Exception:
        pass

def start_normal(x, y):
    "Start game."
    grow_normal()
    try:
        onscreenclick(tap_normal)
    except Exception:
        pass

def start_hard(x, y):
    "Start game."
    grow_hard()
    try:
        onscreenclick(tap_hard)
    except Exception:
        pass


class Button:
    def __init__(self, startx, starty, sizex, sizey, name, string):
        self.startx = startx
        self.starty = starty
        self.sizex = sizex
        self.sizey = sizey
        self.name = name
        self.string = string

    def draw(self):
        temp = pencolor()
        up()
        goto(self.startx, self.starty)
        color(self.name)
        down()
        begin_fill()

        for count in range(2) :
            forward(self.sizex)
            left(90)
            forward(self.sizey)
            left(90)

        end_fill()
        up()
        color(temp)
        goto(self.startx+self.sizex/2-2.6*len(self.string), self.starty+self.sizey/2-3.5)
        write(self.string)

    def getString(self):
        return self.string

    def isButton(self, x, y):
        return self.startx <= x and x <= self.startx + self.sizex and self.starty <= y and y <= self.starty+self.sizey

def chkButton(x, y):
    global buttons
    for button in buttons :
        if button.isButton(x, y):
            if button.getString() == "매우 쉬움":
                print("매우 쉬움 난이도")
                clear()
                grid()
                onscreenclick(start_easy)

            if button.getString() == "보통":
                print("보통 난이도")
                clear()
                grid()
                onscreenclick(start_normal)


            if button.getString() == "매우 어려움":
                print("어려움 난이도")
                clear()
                grid()
                onscreenclick(start_hard)

            
            clear()
            reset()
            grid()
            update()

def diffInit():
    buttons.append(Button(-155, 0, 65, 50, 'green', '매우 쉬움'))
    buttons.append(Button(-25, 0, 60, 50, 'green', '보통'))
    buttons.append(Button(105, 0, 80, 50, 'green', '매우 어려움'))
  
    onscreenclick(chkButton)
    for button in buttons:
        button.draw()
    update()



def main():
    hideturtle()
    tracer(False)
    
    diffInit()
    done()
    
if __name__ == "__main__":
    setup(420, 420, 370, 300)
    main()
    
   

