'''
A robot moves in a plane starting from the original point (0,0). 
The robot can move toward UP, DOWN, LEFT and RIGHT; numbers after the direction are steps. 
Write a program to compute the distance from current position after a sequence of movement and original point. 
If the distance is a float, then just print the nearest integer.



input: UP 5,DOWN 3,LEFT 3,RIGHT 2
output: 2
'''
import math

pos = [0, 0]
movement = [item for item in input("Give the directions here: ").split(',')]

for sequence in movement:
    direction, steps = sequence.split()
    steps = int(steps)

    if direction == "UP":
        pos[0] += steps
    if direction == "DOWN":
        pos[0] -= steps
    if direction == "LEFT":
        pos[1] -= steps
    if direction == "RIGHT":
        pos[1] += steps

print(round(math.sqrt(pos[0]**2 + pos[1]**2)))