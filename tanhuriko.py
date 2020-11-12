import math

f = open("tanhuriko.dat" ,"w")


p = 1.0
q = math.pi/4
t = 0.0
g = 9.8

steps=1000
for i in range(steps+1):
    h = 6.28/steps
    q = q + p*(h)
    p = p - g*math.sin(q)*(h)
    t = t + (h)
    x = math.sin(q)
    y = -math.cos(q)
    f.write(f"{t} {x} {y}\n")