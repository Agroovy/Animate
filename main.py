#Animate an image
from transpiler import read

if __name__ == "__main__":
    execute = read()
    image = execute.pop(0)
    height = len(image)
    width = len(image[0])

    from functions import *
    while True:
        for instruction in execute:
            clear()
            eval(instruction)
