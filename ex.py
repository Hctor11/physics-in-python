from vpython import *

#make two graphs - one for the police, and the speeder
fp=gcurve(color=color.blue) #this will be police
fs=gcurve(color=color.red) #this is for the speeder

#now for initial conditions
#both cars start at x = 0
xp=0
xs=0

vs=40


#this is the max speed of police
vpmax=60
vp=0

#acceleration of police.
#ap is the starting value
ap=0
#apa is the value when acceleratinge
apa=6

t=0
dt=0.03

#this is the time to wait for the start of police
twait=3

#instead of doing a loop for a certain amount of time
#we make a loop that goes until the police catches
#the speeder

while xp<=xs:
  #update the position of the speeder
  xs= xs + vs*dt
  #set a to zero
  ap=0
  #if it's after 3 sec and before they meet, set a to 6
  if (t>twait) and (vp<vpmax):
    ap=apa
    
  #update velocity of police car
  vp= vp + ap*dt
  #update position of police car
  xp= xp + vp*dt
  
  t=t+dt
  #these make the plots
  fp.plot(t,xp)
  fs.plot(t,xs)

#after the loop ends, print time and position
print("time to catch = ", t," seconds")
print("position of police car = ",xp," m")
print("position of speeder = ",xs," m")
  