#!/usr/bin/python

from graphics import *


win = GraphWin('Student Score Histogram',800,800)
win.setCoords(-10,-10,10,10)
win.setBackground('LemonChiffon')

# Open file for reading
file = open('score.txt','r')

vline = Line(Point(-8,8),Point(-8,-8)).draw(win)
vline.setArrow('first')
hline = Line(Point(8,-8),Point(-8,-8)).draw(win)
hline.setArrow('first')
title = Text(Point(0,9), 'Distribution of Students by Score').draw(win)

a = -8
num = 0
for _ in range(16):
    vNum = Text(Point(-9,a), num).draw(win)
    num+=10
    a+=1
b=-7
hnum=1
for _ in range(10):
    hNum = Text(Point(b,-9), hnum).draw(win)
    hnum+=1
    b+=1.5
scores = []
for eachline in file.readlines():
    array = eachline.strip().split(':')
    # print(array)
    if len(array) == 2:
        # print(int(array[-1]))
        arrayInt =int(array[-1])
        scores.append(arrayInt)
uniqScore = []
for i in scores:

    print(set(scores))

# win.getMouse()
# win.close()
