from sympy import *

f = open("hamiltonian1.dat" ,"w")

def p_differential(x):
    q = Symbol("q")
    return diff(x, q).subs(q,b)

def q_differential(x):
    p = Symbol("p")
    return diff(x, p).subs(p,a)

q = Symbol("q")
p = Symbol("p")

p = 1.0
q = 0.0
t = 0.0

H = input()
steps=1000
for i in range(steps+1):
    h = 6.28/steps
    a = p
    b = q
    q = q + q_differential(H)*(h)
    p = p - p_differential(H)*(h)
    t = t + (h)
    f.write(f"{t} {q} {p}\n")