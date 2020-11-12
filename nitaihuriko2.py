from sympy import *
import math

f = open("nitaihuriko2.dat" ,"w")

# mは質量、lは糸の長さ
m1 = 1.0
m2 = 1.0
l1 = 1.0
l2 = 0.5

# pは運動量、qは位置
p1 = 1.0
q1 = math.pi/6
p2 = 1.0
q2 = math.pi/4
x1 = l1 * (math.sin(q1))
y1 = -l1 * (math.cos(q1))
x2 = x1 + l2 * (math.sin(q2))
y2 = y1 - l2 * (math.cos(q2))

g = 9.8
h = 0.01
t = 0


for i in range(100):
    q1dash = (l2*p1-l1*math.cos(q1-q2)*p2)/((m1+m2)*(l1**2)*l2-m2*(l1**2)*l2*((math.cos(q1-q2))**2))
    q1 += q1dash * h
    q2dash = (-m2*l2*math.cos(q1-q2)*p1+(m1+m2)*l1*p2)/((m1+m2)*(l2**2)*l1-m2*(l2**2)*l1*((math.cos(q1-q2))**2))
    q2 += q2dash * h
    p1 += ((-m2*l1*l2*q1dash*q2dash*(math.sin(q1-q2)))-((m1+m2)*g*l1*(math.sin(q1)))) * h
    p2 += ((m2*l1*l2*q1dash*q2dash*(math.sin(q1-q2)))-(m2*g*l2*(math.sin(q2)))) * h
    x1 = l1 * (math.sin(q1))
    y1 = -l1 * (math.cos(q1))
    x2 = x1 + l2 * (math.sin(q2))
    y2 = y1 - l2 * (math.cos(q2))
    t += h
    f.write(f"{t} {x1} {y1} {x2} {y2}\n")