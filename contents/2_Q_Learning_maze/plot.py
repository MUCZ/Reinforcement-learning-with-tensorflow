"""
This code is to visualise the q-table and the enviroment 

"""

import matplotlib.pyplot as plt
MAZE_H = 5
MAZE_W = 5
import numpy as np
import pandas as pd 
 
# Display matrix
def plot_Q(Q):
    # Q_to_plot(Vertical axis, Horizontal axis)
    Q_to_plot=np.zeros((MAZE_H*3,MAZE_W*3))
    
    # Color the Hell and oval
    Q_to_plot[2*3:3*3,1*3:2*3] = -1
    Q_to_plot[1*3:2*3,2*3:3*3] = -1
    Q_to_plot[2*3:3*3,2*3:3*3] = +1
    Q_to_plot[3*3:4*3,2*3:3*3] = -1
    Q_to_plot[3*3:4*3,3*3:4*3] = -1


    for x in range(MAZE_H):
        for y in range(MAZE_W):
            
            # data in Q is like : [1.0, 1.0]: 0.4 0.0 0.2 0.1
            # creat the position string
            xs = str(x)
            ys = str(y)
            cor = "["+xs+".0, "+ys+".0]"

            # find the position string in Q-table
            if cor in Q.index:
                # read the values of four actions
                values = Q.loc[cor]

                # Index of Q_to_plot begin with 0 
                # up
                Q_to_plot[3*y,3*x+1]=1*values[0]
                # down
                Q_to_plot[3*y+2,3*x+1]=1*values[1]
                # right
                Q_to_plot[3*y+1,3*x+2]=1*values[2]
                # left
                Q_to_plot[3*y+1,3*x]=1*values[3]

    plt.matshow(Q_to_plot)
    plt.show()