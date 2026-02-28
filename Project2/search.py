
import math
import matplotlib.pyplot as plt
from grid import *
from utils import *

def gen_polygons(path):
    polys=[]
    with open(path) as f:
        for line in f:
            pts=[]
            for pair in line.strip().split(';'):
                x,y=pair.split(',')
                pts.append(Point(int(x),int(y)))
            polys.append(pts)
    return polys

def cross(a,b,p):
    return (b.x-a.x)*(p.y-a.y)-(b.y-a.y)*(p.x-a.x)

def on_seg(p,a,b):
    return min(a.x,b.x)<=p.x<=max(a.x,b.x) and min(a.y,b.y)<=p.y<=max(a.y,b.y) and cross(a,b,p)==0

def in_poly(p,poly):
    inside=False
    for i in range(len(poly)):
        a=poly[i]; b=poly[(i+1)%len(poly)]
        if on_seg(p,a,b): return True
        if (a.y>p.y)!=(b.y>p.y):
            xin=(p.y-a.y)*(b.x-a.x)/(b.y-a.y)+a.x
            if p.x<xin: inside=not inside
    return inside

def blocked(p,eps): return any(in_poly(p,poly) for poly in eps)
def turf(p,tps): return any(in_poly(p,poly) for poly in tps)

def neighbors(p):
    return [Point(p.x,p.y+1),Point(p.x+1,p.y),Point(p.x,p.y-1),Point(p.x-1,p.y)]

def h(p,g): return math.hypot(p.x-g.x,p.y-g.y)

def bfs(start, goal, eps, tps):
    """
    Breadth-First Search (BFS) - Uninformed search algorithm.
    Explores nodes level by level using a FIFO queue. Guarantees shortest path but does not consider heuristics.
    """
    node = start
    if node == goal: return [node], 0, 0  # Goal found at start

    frontier = Queue()  # FIFO queue for BFS
    reached = {start}  # Track visited nodes
    expanded = 0  # Counter for nodes expanded
    frontier.push((start, [start], 0))  # Push (node, path, cost)

    while not frontier.isEmpty():
        node, path, cost = frontier.pop()  # Pop from front (FIFO)
        expanded += 1

        # Explore all neighbors of current node
        for n in neighbors(node):
            # Check boundary conditions (50x50 grid)
            if n.x < 0 or n.x >= 50 or n.y < 0 or n.y >= 50: continue
            # Check if neighbor is blocked by enclosure
            if blocked(n, eps): continue
            nc = cost + 1  # Uniform step cost of 1
            if n == goal: return path + [n], nc, expanded  # Goal found
            # Only add if not previously reached
            if n not in reached:
                reached.add(n)
                frontier.push((n, path + [n], nc))

    return [], math.inf, expanded  # No path found


def dfs(start, goal, eps, tps):
    """
    Depth-First Search (DFS) - Uninformed search algorithm.
    Explores as deep as possible along each branch before backtracking using a LIFO stack.
    Does not guarantee shortest path and may not find solution if cycles exist.
    """
    node = start
    if node == goal: return [node], 0, 0  # Goal found at start

    frontier = Stack()  # LIFO stack for DFS
    reached = {start}  # Track visited nodes
    expanded = 0  # Counter for nodes expanded
    frontier.push((start, [start], 0))  # Push (node, path, cost)

    while not frontier.isEmpty():
        node, path, cost = frontier.pop()  # Pop from top (LIFO)
        expanded += 1

        # Explore all neighbors of current node
        for n in neighbors(node):
            # Check boundary conditions (50x50 grid)
            if n.x < 0 or n.x >= 50 or n.y < 0 or n.y >= 50: continue
            # Check if neighbor is blocked by enclosure
            if blocked(n, eps): continue
            nc = cost + 1  # Uniform step cost of 1
            if n == goal: return path + [n], nc, expanded  # Goal found
            # Only add if not previously reached
            if n not in reached:
                reached.add(n)
                frontier.push((n, path + [n], nc))

    return [], math.inf, expanded  # No path found



def gbfs(start,goal,eps,tps):
    """
    Greedy Best-First Search (GBFS) - Informed search algorithm.
    Uses a heuristic function to prioritize nodes closest to goal. Fast but not optimal.
    Expands nodes based purely on heuristic estimate, ignoring actual cost so far.
    """
    frontier = PriorityQueue()  # Priority queue ordered by heuristic value
    explored = set()  # Track explored nodes to avoid revisiting
    expanded = 0  # Counter for nodes expanded
    # Push with heuristic priority h(start, goal)
    frontier.push((start,[start],0), h(start,goal))

    while not frontier.isEmpty():
        s, path, cost = frontier.pop()  # Pop node with lowest heuristic value
        if s == goal: return path, cost, expanded  # Goal found
        if s in explored: continue  # Skip if already explored
        explored.add(s)  # Mark as explored
        expanded += 1

        # Explore all neighbors
        for n in neighbors(s):
            # Check boundary conditions (50x50 grid)
            if n.x < 0 or n.x >= 50 or n.y < 0 or n.y >= 50: continue
            # Check if neighbor is blocked by enclosure
            if blocked(n,eps): continue
            # Terrain cost: 1.5 on turf polygons, 1.0 elsewhere
            step = 1.5 if turf(n,tps) else 1
            nc = cost + step
            # Push with heuristic priority h(n, goal)
            frontier.push((n,path+[n],nc), h(n,goal))
    return [], math.inf, expanded  # No path found

def astar(start,goal,eps,tps):
    """
    A* Search - Optimal informed search algorithm.
    Uses f(n) = g(n) + h(n) where g(n) is actual cost and h(n) is heuristic estimate.
    Combines actual cost with heuristic to find optimal path while being more efficient than uninformed search.
    """
    frontier = PriorityQueue()  # Priority queue ordered by f(n) = cost + heuristic
    explored = set()  # Track explored nodes to avoid revisiting
    expanded = 0  # Counter for nodes expanded
    # Initial heuristic: distance from start to goal
    frontier.push((start,[start],0), h(start,goal))

    while not frontier.isEmpty():
        s, path, cost = frontier.pop()  # Pop node with lowest f(n) value
        if s == goal: return path, cost, expanded  # Goal found
        if s in explored: continue  # Skip if already explored
        explored.add(s)  # Mark as explored
        expanded += 1

        # Explore all neighbors
        for n in neighbors(s):
            # Check boundary conditions (50x50 grid)
            if n.x < 0 or n.x >= 50 or n.y < 0 or n.y >= 50: continue
            # Check if neighbor is blocked by enclosure
            if blocked(n,eps): continue
            # Terrain cost: 1.5 on turf polygons, 1.0 elsewhere
            step = 1.5 if turf(n,tps) else 1
            nc = cost + step  # g(n): actual cost from start
            # f(n) = g(n) + h(n): total estimated cost via this node
            frontier.push((n,path+[n],nc), nc + h(n,goal))
    return [], math.inf, expanded  # No path found

def search(start,goal,eps,tps,mode):
    if mode=="BFS":
        return bfs(start,goal,eps,tps)
    if mode=="DFS":
        return dfs(start,goal,eps,tps)
    if mode=="GBFS":
        return gbfs(start,goal,eps,tps)
    if mode=="ASTAR":
        return astar(start,goal,eps,tps)
    return [],math.inf,0

def plot_world(eps,tps,start,goal,path,title,filename):
    fig,ax=draw_board()
    draw_grids(ax)
    draw_source(ax,start.x,start.y)
    draw_dest(ax,goal.x,goal.y)

    for poly in eps:
        for p in poly: draw_point(ax,p.x,p.y)
        for i in range(len(poly)):
            draw_line(ax,[poly[i].x,poly[(i+1)%len(poly)].x],[poly[i].y,poly[(i+1)%len(poly)].y])

    for poly in tps:
        for p in poly: draw_green_point(ax,p.x,p.y)
        for i in range(len(poly)):
            draw_green_line(ax,[poly[i].x,poly[(i+1)%len(poly)].x],[poly[i].y,poly[(i+1)%len(poly)].y])

    for i in range(len(path)-1):
        draw_result_line(ax,[path[i].x,path[i+1].x],[path[i].y,path[i+1].y])

    ax.set_title(title)
    plt.savefig(filename)
    plt.close()


# Running Program
if __name__=="__main__":
    eps=gen_polygons("TestingGrid/world1_enclosures.txt")
    tps=gen_polygons("TestingGrid/world1_turfs.txt")

    start=Point(8,10)
    goal=Point(43,45)

    modes=["DFS","BFS","GBFS","ASTAR"]
    with open("summary.txt","w") as f:
        for m in modes:
            path,cost,exp=search(start,goal,eps,tps,m)
            plot_world(eps,tps,start,goal,path,m,f"TestingGrid/{m}.png")
            f.write(f"{m}:\nPath cost: {cost}\nNodes expanded: {exp}\n\n")
