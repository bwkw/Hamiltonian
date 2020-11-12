from math import sqrt

f = open("santaikei3.dat" ,"w")

mA = 5.0
mB = 1.0
mC = 3.0
vA = sqrt(5/6)
vB = sqrt(4/3)
vC = sqrt(7/6)

#運動量の初期値
Ax = 0
Ay = mA * vA 
Bx = 0
By = mB * vB 
Cx = mC * vC * (-1)
Cy = 0

#位置の初期値
ax = 0
ay = 0
bx = 1.496 * 10**11
by = 0
cx = bx - 1.5 * 10**9
cy = 2

h = 0.01
t = 0.0

for _ in range(2000):
    ax += Ax/mA * h
    ay += Ay/mA * h
    bx += Bx/mB * h
    by += By/mB * h
    cx += Cx/mC * h
    cy += Cy/mC * h
    r_ab = sqrt(((bx-ax)**2)+((by-ay)**2))
    r_ac = sqrt(((cx-ax)**2)+((cy-ay)**2))
    r_bc = sqrt(((cx-bx)**2)+((cy-by)**2))
    Ax += (((bx-ax)/((r_ab)**3))+((cx-ax)/((r_ac)**3))) * h
    Ay += (((by-ay)/((r_ab)**3))+((cy-ay)/((r_ac)**3))) * h
    Bx += (((ax-bx)/((r_ab)**3))+((cx-bx)/((r_bc)**3))) * h
    By += (((ay-by)/((r_ab)**3))+((cy-by)/((r_bc)**3))) * h
    Cx += (((ax-cx)/((r_ac)**3))+((bx-cx)/((r_bc)**3))) * h
    Cy += (((ay-cy)/((r_ac)**3))+((by-cy)/((r_bc)**3))) * h
    t += h
    f.write(f"{t} {ax} {ay} {bx} {by} {cx} {cy}\n")
