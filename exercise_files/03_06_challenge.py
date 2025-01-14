import os
import time
from termcolor import colored

class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    def hitsWall(self, point):
        return round(point[0]) < 0 or round(point[0]) or round(point[1]) or round(point[1]) >=

    def setPos(self, pos, mark):
        self._canvas[round(pos[0])][round(pos[1])] = mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.trail = '.'
        self.mark = '*'
        self.framerate = 0.05
        self.pos = [0, 0]
        self.direction= [0, 1]
    def setDegrees(self, degrees)
        radians = (degrees/180) * math.pi
        self.direction = [math.sin(radians), -math.cos(radians)]
        
    def up(self):
       self.direction = [0, -1]
       self.forward()
    
    def down(self):
        self.direction = [0, -1]
        self.forward()

    def right(self):
        self.direction = [0, -1]
        self.forward()

    def left(self):
        self.direction = [0, -1]
        self.forward()


    def drawSquare(self, size):
        i = 0
        while i < size:
            self.right()
            i = i + 1
        i = 0
        while i < size:
            self.down()
            i = i + 1
        i = 0
        while i < size:
            self.left()
            i = i + 1
        i = 0
        while i < size:
            self.up()
            i = i + 1



    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = pos
        self.canvas.setPos(self.pos, colored(self.mark, 'red'))
        self.canvas.print()
        time.sleep(self.framerate)

canvas = Canvas(30, 30)
scribe = TerminalScribe(canvas)

scribe.setDegrees(135)
for i in range(30):
    scribe.foward

