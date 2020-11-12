import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

p = 5.0
q = -math.pi/4
t = 0.0
g = 9.8

t_list = []
x_list = []
y_list = []

h = 0.1

for i in range(1000):
    q = q + p*(h)
    p = p - g*math.sin(q)*(h)
    t = t + (h)
    x = math.sin(q)
    y = -math.cos(q)
    t_list.append(t)
    x_list.append(x)
    y_list.append(y)


def gen():
    for tt, x, y in zip(t_list, x_list, y_list):
        yield tt, x, y

fig, ax = plt.subplots()
ax.set_xlim(-2,2)
ax.set_ylim(-2,1)
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