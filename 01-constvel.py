from vpython import *

# Constant Velocity / Velocidad constante

"""
VELOCIDAD CONSTANTE

La ciencia es sobre una sola cosa: modelos.add()

En la ciencia se crean modelos para compararlos con la vida real, si los modelos lo mismo
que la vida real, entonces el modelo es correcto, sino, el modelo esta mal.

Antes de hacer un modelo, primero necesitamos datos.

Supongamos que la velocidad constante es como un carrito moviendo en una linea unidimensional,
en este caso el carrito se mueve en direccion de la velocidad, por que podriamos decir que 
la velocidad promedio de el carrito es:

vel. promedio = (distancia final - distancia inicial)/(tiempo final - tiempo inicial)

(Notese que esto bien podria ser la derivada de la distancia en funcion del tiempo)

"""

x = 0
v = 0.437
t = 0
dt = 0.01

f1 = gcurve(color=color.red)

while t < 1:
    x=x+v*dt #nueva posicion
    t=t+dt # nuevo tiempo
    f1.plot(t,x) # agregar los datos al grafico
    
f2= gcurve(color=color.green)

x2=.437
t2=1
v=0.437

# while t2<=1.09:
#   f2.plot(t2,x2)
#   t2=t2+dt

while t2<=3.15:
  x2=x2+v*dt
  t2=t2+dt
  f2.plot(t2,x2)
  
"""
siguiente clase: https://rhettallain_gmail_com.trinket.io/introductory-physics-with-python#/motion-in-1d/constant-acceleration
"""