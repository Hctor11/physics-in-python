from vpython import *

"""
SE CAMBIO EL RECURSO DE APRENDIZAJE DE TRINKET A EL LIBRO 'Physics Simulations in Python'
link: https://physics.weber.edu/schroeder/scicomp/PythonManual.pdf
"""

# MAKING SHAPES
'''
introductory lesson on how to create shapes on vpython
'''

movingBox = box(pos=vector(-5,-5,-5), size=vector(1,1,1), color=color.purple)

while movingBox.pos.x < 5:
    rate(50)
    movingBox.pos.x += 0.05
    
