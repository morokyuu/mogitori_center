# -*- coding: utf-8 -*-
"""
graphic
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def drawLine(ax, xy, color="green"):
    _,c = xy.shape
    xy = xy[0:2,:]
    for i in range(0,c,2):
        prt = xy[:,i:i+2]
        ax.plot(prt[0,:],prt[1,:], color=color)

def drawCircle(ax, xy, _r=2, _fc='b'):
    _,c = xy.shape
    xy = xy[0:2,:]
    for i in range(c):
        ax.add_patch(patches.Circle(xy[:,i], radius=_r, fc=_fc))

def cross_point(line0,line1):
    a = line1[:,0]-line0[:,0]
    b = line1[:,1]-line0[:,0]
    c = line0[:,1]-line0[:,0]
    print(a,b,c)
    A = np.array([
        [a[0] - b[0], -c[0]],
        [a[1] - b[1], -c[1]]
        ])
    Bv = np.array([
        [-b[0]],
        [-b[1]]
        ])
    A_inv = np.linalg.inv(A)
    
    st = np.dot(A_inv, Bv)
    s_on = 0 < st[0] and st[0] < 1
    t_on = 0 < st[1] and st[1] < 1
    print(f"st:\n{st}\n s_on {s_on}, t_on {t_on}")
    flag = s_on and t_on
    ret = np.array([st[1][0] * c]).T
    print(ret)
    return flag, ret

def rot(th):
    return np.array([
        [np.cos(th), -np.sin(th), 0.0],
        [np.sin(th), np.cos(th), 0.0],
        [0.0, 0.0, 1.0],
        ])

def trans(dx,dy):
    return np.array([
        [1.0, 0.0, dx],
        [0.0, 1.0, dy],
        [0.0, 0.0, 1.0]
        ])

ax = plt.subplot(1, 1, 1)

ox = np.sqrt(3)/2.0
oy = 1.0/2.0
a = np.array([[0.0, 10.0, 10.0],[0.0, 0.0, 10.0]]).T
drawCircle(ax, a)

b = np.dot(rot(0.3),a)
drawCircle(ax, b)

dx = 3
dy = 0.5
tr = trans(dx,dy)
d = np.dot(tr,a)
drawCircle(ax, d)

lines = np.array([
    [0,0],
    [20,20],
    [20,20],
    [0,40],
    [0,40],
    [-20,20],
    [-20,20],
    [0,0]
    ]).T
drawLine(ax, lines)

ray_xy = np.array([[0,0],[24,10]]).T
wall_xy = np.array([[20,0],[10,40]]).T
flag, cross_point = cross_point(ray_xy,wall_xy)
drawLine(ax, ray_xy, color="red")
drawLine(ax, wall_xy)

print(flag)
print(cross_point)

if flag:
    drawCircle(ax, cross_point)

ax.set_xlabel("X [mm]")
ax.set_ylabel("Y [mm]")

plt.axis('scaled')
ax.set_aspect('equal')

PLOTAREA_WIDTH = 50.0
ax.set_xlim([-PLOTAREA_WIDTH, PLOTAREA_WIDTH])
ax.set_ylim([-PLOTAREA_WIDTH, PLOTAREA_WIDTH])
