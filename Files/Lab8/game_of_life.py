import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

ic = np.random.randint(0,2,(5,5))
buffor = np.zeros_like(ic)

fig = plt.figure(figsize = (10, 10))
data = plt.imshow(ic)


def next_cell_value(arr,r,c):
    height, width = arr.shape
    cell_sum = -arr[r,c]
    for dh in range (-1, 2):
        for dw in range(-1, 2):
            cell_sum += arr[(r + dh) % height, (c + dw) % width]

    if arr[r,c] == 1 and (cell_sum == 2 or cell_sum == 3):
        return 1
    if arr[r,c] == 0 and (cell_sum == 3):
        return 1
    return 0

def next_step(in_arr, out_arr):
    height, width = in_arr.shape
    for h in range(height):
        for w in range(width):
            out_arr[h,w] = next_cell_value(in_arr,h,w)
    return out_arr

def frame(i):
    # importowanie zmiennych globalnych
    global ic, buffor
    next_step(ic, buffor)
    ic, buffor = buffor, ic
    data.set_data(ic)
    return data,

animiation = FuncAnimation(fig,frame,frames=10, blit = True)
HTML(animiation.to_jshtml())