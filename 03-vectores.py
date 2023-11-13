from vpython import *

# VECTORES

"""
Para entender a los vectores, primero se tiene que entender que es un escalar,
un escalar es una variable que depende solo de una cantidad para ser medida, por ejemplo la
temperatura, la masa o la altura.

un vector es una variable que no solo depende de una sola cantidad sino que puede ser de dos
o mas.

pero, COMO PODEMOS REPRESENTAR A UN VECTOR?

Normalmente un vector de dos dimensiones se grafica a partir de las dos dimensiones espaciales que tiene,
en el caso de ser un vector de tres dimensiones se representa como una flecha que apunta a la direccion
de su magnitud.


"""

A = vector(2,0,0)
B = vector(1,3,0)
C = vector(-2, -1, 0)

# representacion de tres vectores de 3 dimensiones
vA=arrow(pos=vector(0,0,0), axis=A, color=color.yellow)
vB=arrow(pos=vector(0,1,0), axis=B, color=color.red)
vC=arrow(pos=vector(0,-1,0), axis=C, color=color.green)

"""
https://rhettallain_gmail_com.trinket.io/introductory-physics-with-python#/forces-and-vectors-in-2d-3-d/what-is-a-vector
"""