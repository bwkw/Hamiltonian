from sympy import *

f = open("hamiltonian2.dat" ,"w")

def p1_differential(x):
    q1 = Symbol("q1")
    q2 = Symbol("q2")
    j = diff(x, q1).subs(q1,a)
    return j.subs(q2,b)

def p2_differential(x):
    q2 = Symbol("q2")
    q1 = Symbol("q1")
    k = diff(x, q2).subs(q2,b)
    return 

def q1_differential(x):
    p1 = Symbol("p1")
    return diff(x, p1).subs(p1,c)

def q2_differential(x):
    p2 = Symbol("p2")
    return diff(x, p2).subs(p2,d)

q1 = Symbol("q1")
p1 = Symbol("p1")
q2 = Symbol("q2")
p2 = Symbol("p2")

p1 = 1.0
p2 = 1.0
q1 = 0.0
q2 = 1.0
t = 0.0

H = input()
steps=1000
for i in range(steps+1):
    h = 6.28/steps
    a = q1
    b = q2
    c = p1
    d = p2
    q1 = q1 + q1_differential(H)*(h)
    q2 = q2 + q2_differential(H)*(h)
    p1 = p1 - p1_differential(H)*(h)
    p2 = p2 - p2_differential(H)*(h)
    t = t + (h)
    f.write(f"{t} {q1} {p1} {q2} {p2}\n")