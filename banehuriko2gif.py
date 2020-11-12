import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# mは質量
m = 1.0

# pは運動量、qは位置
px = [0,0,0]
py = [0,0,0]
qx = [0,1,2]
qy = [0,-1,-2]

g = 9.8
k = 5.0
h = 0.1
t = 0

t_list = []
x1_list = []
x2_list = []
y1_list = []
y2_list = []

for _ in range(1000):
    for i in range(1,2+1):
        dx = qx[i]-qx[i-1]
        dy = qy[i]-qy[i-1]
        r = math.sqrt(dx**2+dy**2)
        f = k*r
        px[i-1] += k*dx *h
        py[i-1] += k*dy *h
        px[i] -= k*dx *h
        py[i] -= (k*dy+m*g) *h
        qx[i] += px[i]/m * h
        qy[i] += py[i]/m * h
    t += h
    t_list.append(t)
    x1_list.append(qx[1])
    x2_list.append(qx[2])
    y1_list.append(qy[1])
    y2_list.append(qy[2])
    
        


def gen():
    for tt, x1, y1, x2, y2 in zip(t_list, x1_list, y1_list, x2_list, y2_list):
        yield tt, x1, y1, x2, y2


fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 2)
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