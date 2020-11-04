"""
Reinforcement learning maze example.

Red rectangle:          explorer.
Black rectangles:       hells       [reward = -1].
Yellow bin circle:      paradise    [reward = +1].
All other states:       ground      [reward = 0].

This script is the environment part of this example. The RL is in RL_brain.py.

View more on my tutorial page: https://morvanzhou.github.io/tutorials/
"""


import numpy as np
import time
import sys
if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk


UNIT = 60   # pixels
Length_square = UNIT/2 -5 # 正方形的边长，圆的半径，减五是为了留空，美观
MAZE_H = 5  # grid height
MAZE_W = 5  # grid width


class Maze(tk.Tk, object):
    def __init__(self):
        super(Maze, self).__init__()
        self.action_space = ['u', 'd', 'l', 'r']
        self.n_actions = len(self.action_space)
        self.title('maze')
        self.geometry('{0}x{1}'.format(MAZE_H * UNIT, MAZE_H * UNIT))
        self._build_maze()

    def _build_maze(self):
        self.canvas = tk.Canvas(self, bg='white', # canvas ： 画布
                           height=MAZE_H * UNIT,
                           width=MAZE_W * UNIT)

        # create grids
        for c in range(0, MAZE_W * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, MAZE_H * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, MAZE_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_W * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)

        # create origin
        origin = np.array([UNIT/2, UNIT/2])

        # hell
        hell1_center_u = np.array([2,1])                      # u 代表unit
        hell1_center = origin + UNIT*hell1_center_u         # 点定义
        self.hell1 = self.canvas.create_rectangle(          # 正方形定义
            hell1_center[0] - Length_square, hell1_center[1] - Length_square,
            hell1_center[0] + Length_square, hell1_center[1] + Length_square,
            fill='black')
        # hell
        hell2_center_u = np.array([1,2])                      
        hell2_center = origin + UNIT*hell2_center_u
        self.hell2 = self.canvas.create_rectangle(
            hell2_center[0] - Length_square, hell2_center[1] - Length_square,
            hell2_center[0] + Length_square, hell2_center[1] + Length_square,
            fill='black')
        # hell
        hell3_center = origin + np.array([UNIT* 3, UNIT * 3])
        self.hell3 = self.canvas.create_rectangle(
            hell3_center[0] - Length_square, hell3_center[1] - Length_square,
            hell3_center[0] + Length_square, hell3_center[1] + Length_square,
        fill='black')
        # hell
        hell4_center = origin + np.array([UNIT* 2, UNIT * 3]) 
        self.hell4 = self.canvas.create_rectangle(
            hell4_center[0] - Length_square, hell4_center[1] - Length_square,
            hell4_center[0] + Length_square, hell4_center[1] + Length_square,
        fill='black')

        # create oval   圆形
        oval_center = origin + UNIT * 2
        self.oval = self.canvas.create_oval(
            oval_center[0] - Length_square, oval_center[1] - Length_square,
            oval_center[0] + Length_square, oval_center[1] + Length_square,
            fill='yellow')

        # create red rect   红方块代表的机器人
        self.rect = self.canvas.create_rectangle(
            origin[0] - Length_square, origin[1] - Length_square,
            origin[0] + Length_square, origin[1] + Length_square,
            fill='red')

        # pack all
        self.canvas.pack()

    def reset(self):
        self.update()
        time.sleep(0.00001)
        self.canvas.delete(self.rect)

        origin = np.array([UNIT/2, UNIT/2])
        self.rect = self.canvas.create_rectangle(
            origin[0] - Length_square, origin[1] - Length_square,
            origin[0] + Length_square, origin[1] + Length_square,
            fill='red')
        # return observation
        s_ = self.canvas.coords(self.rect)   
        s_= [(s_[1]+s_[3]-UNIT)/(UNIT*2),(s_[0]+s_[2]-UNIT)/(UNIT*2)]
        return s_

    def step(self, action):
        s = self.canvas.coords(self.rect)
        base_action = np.array([0, 0])
        if action == 0:   # up
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:   # down
            if s[1] < (MAZE_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 2:   # right
            if s[0] < (MAZE_W - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 3:   # left
            if s[0] > UNIT:
                base_action[0] -= UNIT

        self.canvas.move(self.rect, base_action[0], base_action[1])  # move agent

        s_ = self.canvas.coords(self.rect)  # next state
        
 

        # reward function
        if s_ == self.canvas.coords(self.oval):
            reward = 1
            done = True
            s_ = 'terminal'
        elif s_ in [self.canvas.coords(self.hell1), self.canvas.coords(self.hell2),self.canvas.coords(self.hell3),self.canvas.coords(self.hell4)]:
            reward = -1
            done = True
            s_ = 'terminal'
        else:
            reward = 0
            done = False
            s_ = [(s_[0]+s_[2]-UNIT)/(UNIT*2),(s_[1]+s_[3]-UNIT)/(UNIT*2)]

        return s_, reward, done

    def render(self):
        time.sleep(0.000001)
        self.update()


# 这个update只是用来测试maze_env的，让角色一直向下跑
def update():
    for t in range(10):
        s = env.reset()
        while True:
            env.render()
            a = 1
            s, r, done = env.step(a)
            if done:
                break

if __name__ == '__main__':
    env = Maze()
    env.after(1, update)
    env.mainloop()