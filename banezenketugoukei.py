import math
from sympy import *
from PIL import Image, ImageDraw
from apng import APNG

#1行目に何個の物体のハミルトニアンを考えるかを記述
num = int(input())

#2行目にハミルトニアンを実際に記述(今のところ意味なし)
hamiltonian = input()

px = [0] * num
py = [0] * num

#半径r上にnum個のバネ全結合系の物質を置く
qx = []
qy = [] 
r = 50

for i in range(num):
    angle = (2*math.pi)/num
    itemcos = r * math.cos(angle*i)+250
    itemsin = r * math.sin(angle*i)+250
    qx.append(itemcos)
    qy.append(itemsin)

#デバッグ
print(qx)
print(qy)

#定数
h= 0.1 #時間ステップ
k = 1.0 #バネ定数
m = 1.0 #質量
g = 9.8 #重力定数


#イメージを保存する
def save_image(filename):
    im = Image.new("RGB", (500,500), (128, 128, 128))
    draw = ImageDraw.Draw(im)
    for i in range(num):
        mr = 3.0
        lefttop_x = qx[i]-mr
        lefttop_y = qy[i]-mr
        rightunder_x = qx[i]+mr
        rightunder_y = qy[i]+mr
        draw.ellipse((lefttop_x, lefttop_y, rightunder_x, rightunder_y),fill=(255,0,0), outline=(0,0,0))
    im.save(filename)

#アニメーション作成
def make_anime(files):
    index = len(files)
    filename = "file%03d.png" % index
    save_image(filename)
    files.append(filename)

files = []
#ハミルトニアン シミュレーション
for _ in range(1000):
    for i in range(num):
        for j in range(num):
            if j == i:
                continue
            if j != i:
                dx = qx[i] - qx[j]
                dy = qy[i] - qy[j]
                distance = math.sqrt(dx**2+dy**2)
                px[i] -= k*dx * h
                py[i] -= k*dy * h
    for i in range(num):
        qx[i] += px[i]/m * h
        qy[i] += py[i]/m * h
    make_anime(files)

APNG.from_files(files, delay=50).save("animation.png")
