from __main__ import *
from os import system, name
from time import sleep
clear_type = ("cls" if name == "nt" else "clear")

def clear(*args):
    system(clear_type)

def show(*args):
    sleep(args[0])
    for line in image:
        print(line)
    sleep(args[1])
    clear()

def up(*args):
    if len(args) == 0:
        args = [0.1]
    
    stack = list()
    temp_image = image.__reversed__()

    for line in temp_image:

        for i in range(height - len(stack) - 1): #Newlines
            print()
                       
        stack.append(line)
        for x in stack.__reversed__(): #Part of image
            print(x)
        
        sleep(args[0])
        clear()

def down(*args):
    if len(args) == 0:
        args = [0.1]
    
    for line in image:
        print(line)
        sleep(args[0])

def left(*args):
    if len(args) == 0:
        args = [0.1]

    stack = [["" for y in range(width)] for x in range(height)]
    for y in range(width):
        for x in range(height):
            stack[x][y] = image[x][y]
            print("".join(stack[x][:y]))
        
        sleep(args[0])
        clear()

def right(*args):
    if len(args) == 0:
        args = [0.1]

    stack = [[" " for y in range(width)] for x in range(height)]
    for y in range(width - 1, -1, -1):
        for x in range(height):
            stack[x][y] = image[x][y]
            print("".join(stack[x]))
        
        sleep(args[0])
        clear()
