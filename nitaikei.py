from math import sqrt

f = open("nitaikei.dat" ,"w")

G = 6.67 * 10**(-11)
M = 1.99 * 10**30
m = 5.97 * 10**24
v = 3.00 * 10**4

px = 0
py = m * v
qx = 1.5 * 10**11
qy = 0

h = 1000
t = 0.0

for _ in range(100000):
    qx += px/m * h
    qy += py/m * h
    r = sqrt(qx**2.0 + qy**2.0)
    px -= G * M * m * qx /(r**3) *h
    py -= G * M * m * qy /(r**3) *h
    t += h
    f.write(f"{t} {qx} {qy}\n")



