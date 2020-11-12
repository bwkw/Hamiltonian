import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure() #データをplotするグラフを1つ用意する
plt.xlim(-5, -5) #表示するx軸の範囲を設定
plt.ylim(-10,0) #表示するy軸の範囲を設定
plt.xlabel("x axis")   #x軸の説明
plt.ylabel("y axis")   #y軸の説明
plt.gca().set_aspect('equal', adjustable='box') #グラフ範囲を真四角する
 

# mは質量、lは糸の長さ
m1 = 1.0
m2 = 1.0
l1 = 1.0
l2 = 1.0

# pは運動量、qは位置
p1 = 1.0
q1 = math.pi/4
p2 = 5.0
q2 = math.pi/6
x1 = l1 * (math.sin(q1))
y1 = -l1 * (math.cos(q1))
x2 = x1 + l2 * (math.sin(q2))
y2 = y1 - l2 * (math.cos(q2))

g = 9.8
h = 0.01
t = 0

t_list = []
x1_list = []
x2_list = []
y1_list = []
y2_list = []


for i in range(1000):
    q1dash = (l2*p1-l1*math.cos(q1-q2)*p2)/((m1+m2)*(l1**2)*l2-m2*(l1**2)*l2*((math.cos(q1-q2))**2))
    q1 += q1dash * h
    q2dash = (-m2*l2*math.cos(q1-q2)*p1+(m1+m2)*l1*p2)/((m1+m2)*m2*(l2**2)*l1-m2*(l2**2)*l1*m2*((math.cos(q1-q2))**2))
    q2 += q2dash * h
    p1 += ((-m2*l1*l2*q1dash*q2dash*(math.sin(q1-q2)))-((m1+m2)*g*l1*(math.sin(q1)))) * h
    p2 += ((m2*l1*l2*q1dash*q2dash*(math.sin(q1-q2)))-(m2*g*l2*(math.sin(q2)))) * h
    x1 = l1 * (math.sin(q1))
    y1 = -l1 * (math.cos(q1))
    x2 = x1 + l2 * (math.sin(q2))
    y2 = y1 - l2 * (math.cos(q2))
    t += h
    x1_list.append(x1)
    x2_list.append(x2)
    y1_list.append(y1)
    y2_list.append(y2)
    t_list.append(t)

def gen():
    for tt, x1, y1, x2, y2 in zip(t_list, x1_list, y1_list, x2_list, y2_list):
        yield tt, x1, y1, x2, y2


fig, ax = plt.subplots()
ax.set_xlim(-(l1+l2), l1+l2)
ax.set_ylim(-(l1+l2), l1+l2)
ax.set_aspect('equal')
ax.grid()

locus, = ax.plot([], [], 'r-', linewidth=2)
line, = ax.plot([], [], 'o-', linewidth=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

xlocus, ylocus = [], []
def animate(data):
    t, x1, y1, x2, y2 = data
    xlocus.append(x2)
    ylocus.append(y2)

    locus.set_data(xlocus, ylocus)
    line.set_data([0, x1, x2], [0, y1, y2])
    time_text.set_text(time_template % (t))

ani = FuncAnimation(fig, animate, gen, interval=50, repeat=False)

plt.show()