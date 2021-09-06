import pygame
from pygame.time import delay
from random import randint
from src.colors import *
width   = 600
height  = 400
screen  = pygame.display.set_mode((width, height))

nHouses         = 3
houses          = [[randint(0, width), randint(0, height)] for i in range(nHouses)]

def swap(houses, i, j):
    tmp         = houses[i]
    houses[i]   = houses[j]
    houses[j]   = tmp

def pitagor(a, b):
    from math import sqrt
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    x12 = x1-x2
    y12 = y1-y2
    return sqrt(x12*x12 + y12*y12)

def calcDist(points):
    sum = 0
    for i in range(len(points)-1):
        sum += pitagor(points[i], points[i-1])

    return sum

def factorial(n):
    if n == 1: return 1
    return n*factorial(n-1)

def highlightHouses(points):
    for i in range(len(points)-1):
        pygame.draw.line(screen, MAGENTA, (points[i][0], points[i][1]), (points[i+1][0], points[i+1][1]))


def start():
    recordDistance  = calcDist(houses)
    bestWay         = houses
    highlightHouses(houses)
    pygame.init()
    pygame.display.set_caption("Traveling Salesperson")
    count           = 0

    running = True
    while running:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for i in range(nHouses-1):
            pygame.draw.line(screen, WHITE, (houses[i][0], houses[i][1]), (houses[i+1][0], houses[i+1][1]))
        dist    = calcDist(houses)
        if dist < recordDistance:
            recordDistance = dist
            bestWay     = houses
            print(bestWay)
        highlightHouses(bestWay)
        i = randint(0, nHouses-1)
        j = randint(0, nHouses-1)
        swap(houses, i, j)
        pygame.display.update()
        count += 1
    delay(200)
