import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#運動量p,位置q
p1 = 1.0 #pr
p2 = 5.0 #pθ
q1 = 1.5 #qr
q2 = math.pi/4 #qθ

#自然長l
l = 1.0
m = 1.0

t = 0
h = 0.1
k = 1.0
g = 9.8

t_list = []
x_list = []
y_list = []

for _ in range(1000):
    q1 += p1/m * h
    q2 += p2/(m*(q1**2)) * h
    p1 -= ((-(p2**2)/(m*(q1**3)))+(k*(q1-l))-(m*g*(math.cos(q2)))) * h
    p2 -= m*g*q1*math.sin(q2) * h
    t += h
    x = q1 * math.sin(q2)
    y = -q1 * math.cos(q2)
    t_list.append(t)
    x_list.append(x)
    y_list.append(y)


def gen():
    for tt, x, y in zip(t_list, x_list, y_list):
        yield tt, x, y

fig, ax = plt.subplots()
ax.set_xlim(-10,10)
ax.set_ylim(-22,2)
ax.set_aspect('equal')
ax.grid()


line, = ax.plot([], [], 'o-', linewidth=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

xlocus, ylocus = [], []
def animate(data):
    t, x, y = data
    line.set_data([0, x], [0, y])
    time_text.set_text(time_template % (t))

ani = FuncAnimation(fig, animate, gen, interval=50, repeat=True)

plt.show()