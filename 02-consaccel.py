from vpython import *

# CONSTANT ACCELERATION / ACCELERACION CONSTANTE

"""
Dado a que tenemos un valor independiente como el tiempo y un valor que depende
de este como lo es la velocidad, podemos graficar ambos valores, siendo la variable 
independiente el tiempo y la variable dependiente la velocidad.

Al graficar los valores de un mobil que se mueve a velocidad constante nos dara una
grafica perteneciente a una ecuacion lineal (una linea inclinada).

En terminos simples, la aceleracion promedio se observa como:

a = (velovidad final - velocidad inicial)/(tiempo final - tiempo inicial)
"""

x = 1.33
v = 0.0
a = 0.0577
ts = 1.4
dt = 0.3
t = 0

f1 = gcurve(color = color.red)

"""
Por que hace un ciclo mientras t (0) sea menor a ts (1.4)?
es para que no haga una grafica parabolica y haga una mas adecuada a la aceleracion de 
el mobil.
"""

while t < ts:
    t = t + dt
    f1.plot(t, x)
    
while t < 4.4:
    v = v + a * dt # aqui se actializa la velocidad agarrando la velocidad actual y la suma por la multiplicacion de la aceleracion y el tiempo
    x = x + v * dt # Aqui actualiza la distancia con la original y la suma a la velocidad actual multiplicada por el tiempo
    t = t + dt # Aqui actualiza el tiempo sumandolo con el intervalo dt que teniamos
    
    f1.plot(t, x)
    
    
'''
NOTA: entre mas chiquito sea dt, mas definida sera la grafica
''' 