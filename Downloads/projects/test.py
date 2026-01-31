from pyamaze import maze, agent, COLOR
import tkinter as tk
import heapq
def solve():
    start=(1,1)
    goal=m.rows,m.cols
    came_from=astar(m,start,goal)
    path=[]
    cell=goal
    while cell!=start:
        path.append(cell)
        cell=came_from.get(cell)
        if cell is None:
            print("No paht found")
            return
    path.append(start)
    path.reverse()
    m.tracePath({player: path}, delay=50)
def h(cell, goal):
    r1, c1 = cell
    r2, c2 = goal
    return abs(r1 - r2) + abs(c1 - c2)
def astar(m, start, goal):
    open_heap = []
    heapq.heappush(open_heap, (0, start))
    g_score = {start: 0}
    came_from = {}
    while open_heap:
        _, current = heapq.heappop(open_heap)
        if current == goal:
            break
        for nbr in neighbors(current):
            temp=g_score[current]+1
            if nbr not in g_score or temp < g_score[nbr]:
                g_score[nbr] = temp
                f=temp+h(nbr,goal)
                heapq.heappush(open_heap, (f, nbr))
                came_from[nbr] = current
    return came_from
def neighbors(player):
    r, c = player
    info = m.maze_map[(r, c)]
    nbrs = []
    if info['E'] == 1:
        nbrs.append((r, c + 1))
    if info['W'] == 1:
        nbrs.append((r, c - 1))
    if info['N'] == 1:
        nbrs.append((r - 1, c))
    if info['S'] == 1:
        nbrs.append((r + 1, c))
    return nbrs
m = maze(30, 30)
m.CreateMaze(x=m.rows, y=m.cols, theme='light')
player = agent(m, 1, 1, color=COLOR.red, filled=True, shape='square')
treasure = agent(m, m.rows, m.cols, color=COLOR.yellow, filled=True, shape='square')
root_window = m._canvas.master
root_window.title("Treasure Hunt")
my_button = tk.Button(
    root_window,
    text="Solve",
    command=solve,
    font=('Arial', 12)
)
my_button.place(x=900, y=200)
m.enableArrowKey(player)
m.run()
