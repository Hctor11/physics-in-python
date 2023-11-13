from vpython import *

#turn off auto scale for the scene
scene.autoscale=False

#make a ball
ball=sphere(pos=vector(-10,0,0), radius=0.8, color=color.cyan)

#define a new property of the ball - velocity
ball.v=vector(5,-2,1)

#this might be obvious
attach_trail(ball)

a = 0.0577
t=0
dt=0.01

while t<10:
  #the rate statement makes the program just do 100 calcs per sec
  rate(100)
  
  #update position
  ball.pos = ball.pos*sin(t)+ball.v*dt
  #update time
  t=t+dt