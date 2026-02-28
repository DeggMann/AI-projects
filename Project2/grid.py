
import matplotlib.pyplot as plt

MAX = 50

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash((self.x, self.y))

def draw_board():
    fig = plt.figure(figsize=[8,8])
    ax = fig.add_subplot(111)
    ax.set_axis_off()
    return fig, ax

def draw_grids(ax):
    for x in range(MAX):
        ax.plot([x, x], [0,MAX-1], color='0.75', linestyle='dotted')
    for y in range(MAX):
        ax.plot([0, MAX-1], [y,y], color='0.75', linestyle='dotted')

def draw_point(ax,x,y): ax.plot(x,y,'o',color='k',markersize=4)
def draw_green_point(ax,x,y): ax.plot(x,y,'o',color='g',markersize=4)
def draw_source(ax,x,y): ax.plot(x,y,'o',color='b',markersize=4)
def draw_dest(ax,x,y): ax.plot(x,y,'o',color='r',markersize=4)
def draw_line(ax,xs,ys): ax.plot(xs,ys,'k')
def draw_green_line(ax,xs,ys): ax.plot(xs,ys,'g')
def draw_result_line(ax,xs,ys): ax.plot(xs,ys,'r')
